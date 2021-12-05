pipeline{
        agent any
        stages{
            stage('build'){
                steps{
                    sh "curl https://get.docker.com | sudo bash"
                    sh "sudo pip install docker-compose"
                    sh "sudo docker-compose up -d --build"
                }
            }
        }    
}