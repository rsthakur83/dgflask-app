node {
   
   	stage 'Checkout'
   		git url: 'https://github.com/rsthakur83/dgflask-app.git'
   
      stage 'Execute'
         sh 'chmod +x docker.sh'
      stage 'Deploy in Test Env'
         sh './docker.sh'
 
 }
