pipeline {
    agent any

  

parameters {
    choice(
        name: 'environment',
        choices: "test\nstage\nprod",
        description: 'Deployment Environment' )
  }
   stages {
      

   
      stage ('Change permission')  {
         steps {
         sh 'chmod +x docker.sh'
    }
      }
      
      stage ('Deploy in "${env.environment}"') {
         steps {
         sh './docker.sh'
     }
    }
  }
}
