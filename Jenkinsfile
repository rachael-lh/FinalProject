pipeline{
        agent any
        stages{
            stage('build'){
                steps{
                    sh "apt-get install sudo -y"
                    sh "sudo docker-compose up -d --build"
                }
            }
        }    
}