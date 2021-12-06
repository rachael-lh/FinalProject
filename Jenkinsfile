pipeline{
        agent any
        stages{
            stage('build'){
                steps{
                    sh 'chmod +x ./builds.sh'
                    sh './builds.sh'
                }
            }
        }    
}