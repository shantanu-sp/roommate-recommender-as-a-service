# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_render_template]
import datetime
import os
import json

from flask import Flask, render_template, request, Response, jsonify
#from googleapiclient.discovery import build
import sqlalchemy
import pandas as pd

from sklearn.preprocessing import OneHotEncoder, QuantileTransformer
from sklearn.neighbors import NearestNeighbors
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.decomposition import TruncatedSVD

from google.cloud import tasks_v2

app = Flask(__name__)

db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")
bucket_name = os.environ.get("CS_BUCKET_NAME")

#cloud tasks
client = tasks_v2.CloudTasksClient()
project = 'roommaterecommender'
queue = 'my-queue'
location = 'us-central1'
url = 'https://us-central1-roommaterecommender.cloudfunctions.net/function-1'

parent = client.queue_path(project, location, queue)



#connect to db

# [START cloud_sql_mysql_sqlalchemy_create]
# The SQLAlchemy engine will help manage interactions, including automatically
# managing a pool of connections to your database
db = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
    sqlalchemy.engine.url.URL(
        drivername="mysql+pymysql",
        username=db_user,
        password=db_pass,
        database=db_name,
        query={"unix_socket": "/cloudsql/{}".format(cloud_sql_connection_name)},
        #host="127.0.0.1",
        #port="3306",
    ),
    # ... Specify additional properties here.
    # [START_EXCLUDE]
    # [START cloud_sql_mysql_sqlalchemy_limit]
    # Pool size is the maximum number of permanent connections to keep.
    pool_size=5,
    # Temporarily exceeds the set pool_size if no connections are available.
    max_overflow=2,
    # The total number of concurrent connections for your application will be
    # a total of pool_size and max_overflow.
    # [END cloud_sql_mysql_sqlalchemy_limit]
    # [START cloud_sql_mysql_sqlalchemy_backoff]
    # SQLAlchemy automatically uses delays between failed connection attempts,
    # but provides no arguments for configuration.
    # [END cloud_sql_mysql_sqlalchemy_backoff]
    # [START cloud_sql_mysql_sqlalchemy_timeout]
    # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
    # new connection from the pool. After the specified amount of time, an
    # exception will be thrown.
    pool_timeout=30,  # 30 seconds
    # [END cloud_sql_mysql_sqlalchemy_timeout]
    # [START cloud_sql_mysql_sqlalchemy_lifetime]
    # 'pool_recycle' is the maximum number of seconds a connection can persist.
    # Connections that live longer than the specified amount of time will be
    # reestablished
    pool_recycle=1800,  # 30 minutes
    # [END cloud_sql_mysql_sqlalchemy_lifetime]
    # [END_EXCLUDE]
)

#read and write file to cloud storage default bucket
@app.route('/matches/<id>/<knn>')
def random1(id,knn):
    resp=[]
    #id=request.args.get('id')

    with db.connect() as conn:
        persons = conn.execute("SELECT * FROM studentrecommend")
        df_org=pd.DataFrame(persons.fetchall())
        df_org.columns=persons.keys()

        #for row in persons:
        #    resp+="{Fname: "+str(row[2])+" ,Lname: "+str(row[1])+"}\n"

    qperson=df_org.loc[df_org['id']==int(id)]
    email=qperson.iloc[0]['email']      #"s.purandare226@gmail.com" 
    #minr,maxr=qperson['minrent'][0],qperson['maxrent'][0]
    df_org=df_org.loc[(df_org['id']!=int(id))&(df_org['email']!=str(email))]

    qperson=pd.concat([qperson.iloc[:,2:6],qperson.iloc[:,8:12]],axis=1)
    df=pd.concat([df_org.iloc[:,2:6],df_org.iloc[:,8:12]],axis=1)

    col=list(df.columns.values)

    numeric = [col[0],col[4],col[5]]
    numeric_transformer = Pipeline(steps=[('scaler', QuantileTransformer())])

    cat = [col[1],col[2],col[3],col[6]]
    cat_transformer = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])

    text = col[7]

    text_transformer = Pipeline(steps=[('tfidf', TfidfVectorizer()),('svd', TruncatedSVD(n_components=2))])

    prep = ColumnTransformer(transformers=[('num', numeric_transformer, numeric),
                                           ('cat', cat_transformer, cat),('text', text_transformer, text)], sparse_threshold=0) #


    X_transformed = prep.fit_transform(df)
    q_transformed = prep.transform(qperson)

    nn = NearestNeighbors(n_neighbors=int(knn))
    nn.fit(X_transformed)

    d, i = nn.kneighbors(q_transformed[0].reshape(1,-1))

    #fname="welcome.txt"

    #with open(fname,'w') as file:
    #    file.write(resp)

    #response=Response()
    #response.headers['Content-Type'] = 'text/plain'

    #storage_client = storage.Client()
    #bucket = storage_client.bucket(bucket_name)
    #blob = bucket.blob("dbdata")

    #blob.upload_from_filename(fname)

    #blob.download_to_filename("output.txt")

    #df_org['gender']=df_org['gender'].astype(bool)
    #df_org['foodpreference']=df_org['foodpreference'].astype(bool)

    email_body=json.dumps(df_org.iloc[i[0]].to_dict('records'))
    #print(email_body)
    payload=json.dumps({'receiver':email,'email_body':email_body})
    #print(payload)

    task = {
            'http_request': {  # Specify the type of request.
                'http_method': 'POST',
                'url': url,  # The full url path that the task will be sent to.
                'headers': {'Content-Type':'application/json'}
            }
    }
    if payload is not None:
        # The API expects a payload of type bytes.
        converted_payload = payload.encode()

        # Add the payload to the request.
        task['http_request']['body'] = converted_payload

    # in_seconds,task_name=None,None
    # if in_seconds is not None:
    #     # Convert "seconds from now" into an rfc3339 datetime string.
    #     d = datetime.datetime.utcnow() + datetime.timedelta(seconds=in_seconds)
    #
    #     # Create Timestamp protobuf.
    #     timestamp = timestamp_pb2.Timestamp()
    #     timestamp.FromDatetime(d)
    #
    #     # Add the timestamp to the tasks.
    #     task['schedule_time'] = timestamp
    #
    # if task_name is not None:
    #     # Add the name to tasks.
    #     task['name'] = task_name

    # Use the client to build and send the task.
    response = client.create_task(parent, task)

    print('Created task {}'.format(response.name))


    return jsonify(df_org.iloc[i[0]].to_dict('records'))


@app.route('/_ah/warmup')
def warmup():
    # Handle your warmup logic here, e.g. set up a database connection pool
    return '', 200, {}

@app.route('/')
def testFunc():
    return 'Python Service up!'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python37_render_template]
