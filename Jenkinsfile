pipeline{
        agent any
        stages{
            stage('Test'){
                steps{
                   sh 'chmod +x ./scripts/tests.sh'
                   sh './scripts/tests.sh'
                }
            }
            stage('Build & Deploy'){
                steps{
                   sh 'chmod +x ./scripts/builds.sh'
                   sh './scripts/builds.sh'
                }
            }
        }    
}