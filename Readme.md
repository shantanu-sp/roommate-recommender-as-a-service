

# Instructions to run and deploy services onto google app engine.
The design consists of 3 services, below is a detailed explanation to deploy on GAE. Once you have access to the project 'RoommateRecommender', please ensure that your local google SDK is pointing towards the project 'RoommateRecommender'. Execute the following command to ensure you are pointing to the appropriate project.
* gcloud config set project RoommateRecommender
* gcloud projects list

Once you are locally pointing to the right project, you can deploy the following 3 services to GAE.

# Run Front end service
The Front end service mainly consists of an html and javascripts file. The UI is rendered via a python Flask application.
To deploy the service into Google App Engine, head into the folder which contains all the files, and run the following command.
* Unzip frontend.zip
* cd flaskproject
* gcloud app deploy --version=1

# Run the backend service
The backend service is a Spring Boot Application whose dependencies are packaged using Maven. To run the java app locally unzip the project and go into the root directory of the project. Run the following commands.
* Unizip backend.zip
* cd recommender
* mvn clean install
* mvn appengine:deploy

# Run ML service
The Machine Learning Service is written in python, with all of its core functionalities in 'main.py' Unzip 'myapp.zip' file and go into the project's root directory. This service also creates an Asynchronous task in Google Cloud functions. The function is already present in our project on GCP and does not need to be modified from this service. Run the following commands.
* Unzip ml.zip
* cd myappzip
* gcloud app deploy --version=1

# StressTest
We have also written a python script to stress test our application's performance and observe its results on the automatic scaling of instances. To run the python script you must have python2.7 running in your environment, and execute the following command.
* cd stressTest
* python script.py

# Google Cloud Function
To view the code for Asynchronous Emailing Service, unzip GCP_Function.zip and view main.py, this function is running on GCP as a function and does NOT need to be execute locally.

Once all the services have been successfully deployed, go to "https://frontend-dot-roommaterecommender.uc.r.appspot.com/", to access the UI and run the appliation.

# Instructions to run the application locally
* Run ML service
* Unzip ml.zip
* cd myappzip
* pip install -r requirements.txt
* python3 main.py

 2. Run Backend service
* Ensure maven is installed on local system
* unzip backend.zip
* cd recommender
* vi pom.xml
* Add the following snippet under the dependencies tag i.e. line number 37, which adds the dependency to run the code locally (This is a Tomcat dependency, which is intentionally removed while deploying to GAE as GAE provides a Jetty server and this tomcat server will interfere with it when deployed to GAE.)
'''
<dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-tomcat</artifactId>
  </dependency>
'''
* vi src/main/java/com/asu/recommender/constants/RecommenderConstants.java
* Comment out line 4 and uncomment line 5, save changes.
* mvn clean install
* mvn spring-boot:

3. Run Frontend service
* Unzip frontend.zip
* cd flaskproject
* vi templates/index.html
* Change the URL on line number 283 from https://recommender-dot-roommaterecommender.uc.r.appspot.com/student/getPreferences/ to http://localhost:8081/student/getPreferences/
* Save changes
* python main.py

Once all 3 services have been run successfully go to http://localhost:80 to access the UI and run the application.


![al-text](https://github.com/shantanu-sp/roommate-recommender-as-a-service/blob/master/arch.jpg)

Read more about the project [here](https://github.com/shantanu-sp/roommate-recommender-as-a-service/blob/master/Report.pdf)
