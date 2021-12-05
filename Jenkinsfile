pipeline{
        agent any
        stages{
            stage('build'){
                steps{
                    curl https://get.docker.com | sudo bash
                    sh "sudo docker-compose up -d --build"
                }
            }
        }    
}