pipeline {
    agent any

  

parameters {
    choice(
        name: 'environment',
        choices: "test\nstage\nprod",
        description: 'Deployment Environment' )
  }
   stages {
      
   	stage ('Downloading Source Code')  {
         steps {
   		git url: 'https://github.com/rsthakur83/dgflask-app.git'
            
         }
      }
   
      stage ('Change permission')  {
         steps {
         sh 'chmod +x docker.sh'
    }
      }
      
      stage ('Deploy in $environment') {
         steps {
         sh './docker.sh'
     }
    }
  }
}
