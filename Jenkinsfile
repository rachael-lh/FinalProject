pipeline{
        agent any
        stages{
            stage('build'){
                steps{
                   sh 'docker build -t flask-app-finalproject .'
                   // -compose up -d'
                   // sh 'chmod +x ./builds.sh'
                   // sh './builds.sh'
                }
            }
        }    
}