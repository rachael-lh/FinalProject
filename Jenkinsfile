pipeline{
        agent any
        stages{
            stage('build'){
                steps{
                  // sh 'usermod -G docker jenkins'
                   //sh 'chmod 666 /var/run/docker.sock'
                   //sh 'docker build -t flask-app-finalproject .'
                   // -compose up -d'
                   sh 'chmod +x ./builds.sh'
                   sh './builds.sh'
                }
            }
        }    
}