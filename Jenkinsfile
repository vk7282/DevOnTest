#!/bin/sh
node {
   checkout scm
   stage("SetUp"){
 
        echo "create a virtualenv"
        sh '''
              
              pip install -r requirements.txt
           '''
      

   }

   stage('Deploy Locally'){

       echo "Running the application"
       sh "python app.py"
 
   }

}
