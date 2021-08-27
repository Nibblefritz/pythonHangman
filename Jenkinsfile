node {
   def commit_id
   stage('Preparation') {
     checkout scm
     sh "git rev-parse --short HEAD > .git/commit-id"
     commit_id = readFile('.git/commit-id').trim()
   }
   stage('test') {
     def myTestContainer = docker.image('python:3')
     myTestContainer.pull()
     myTestContainer.inside {
		//Test code here
       sh 'python3 --version'
       //sh ‘python3 -m unittest test.py’ this if we have a unit test that we’ve built with the unittest module
     }
   }                                 
   stage('docker build/push') {            
     docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
       def app = docker.build("nibblefritz/hangman:${commit_id}", '.').push()
     }                                     
   }                                       
}                   