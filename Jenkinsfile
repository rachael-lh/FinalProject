pipeline{
        agent any
        stages{
            stage('build'){
                steps{
                    sh "bash docker-compose up -d --build"
                }
            }
        }    
}