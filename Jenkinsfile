pipeline{
        agent any
        stages{
            stage('build'){
                steps{
                   sh 'docker-compose up -d'
                   // sh 'chmod +x ./builds.sh'
                   // sh './builds.sh'
                }
            }
        }    
}