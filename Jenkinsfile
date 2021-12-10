pipeline{
        agent any
        stages{
            stage('Build & Deploy'){
                steps{
                   sh 'chmod +x ./builds.sh'
                   sh './builds.sh'
                }
            }
        }    
}