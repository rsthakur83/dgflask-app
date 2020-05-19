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
      
      stage ('Deploy"') {
         steps {
             sh 'echo "${environment}"'
         sh './docker.sh'
     }
    }
  }
}
