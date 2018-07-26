node {
   checkout scm
   stage("SetUp"){
 
        echo "create a virtualenv"
        sh '''
              pip install virtualenv
              cd DevOnTest
              /home/candidate/.local/bin/virtualenv venv
              pip install -r requirements.txt
              source venv/bin/activate
           '''
      

   }

   stage('Deploy Locally'){

       echo "Running the application"
       sh "python app.py"
 
   }

}
