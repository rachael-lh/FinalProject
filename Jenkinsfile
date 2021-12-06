pipeline{
        agent any
        stages{
            stage('build'){
                steps{
                    //sh "curl https://get.docker.com | sudo bash"
                    sh "sudo update -y"
                    sh "sudo upgrade -y"
                    sh "sudo apt install -y python3-pip"
                    sh "sudo pip3 install --upgrade pip"
                    sh "sudo pip install docker-compose"
                    sh "sudo docker-compose up -d --build"
                }
            }
        }    
}