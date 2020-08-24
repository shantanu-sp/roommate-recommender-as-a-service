#import the Flask class from the flask module
from flask import Flask, render_template
#from google.cloud import storage

#bucket_name = "recommender-mlmodel"

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    #storage_client = storage.Client()
    #bucket = storage_client.get_bucket(bucket_name)
    #blob = bucket.blob("asu.jpeg")
    #blob.download_to_filename("/tmp/asu.jpeg")
    #logging.info('File downloaded!')
    return render_template("index.html")

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)
