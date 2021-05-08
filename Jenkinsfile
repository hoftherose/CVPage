pipeline {
  agent any
  stages {
    stage('fileView') {
      steps {
        sh 'ls -la' 
      }
    }
    stage('buildDockerImage') {
      steps {
        sh 'docker build -t hoftherose/deep-learning-showcase:latest .  '
      }
    }
    stage('pushImage') {
      steps { 
        sh 'docker push hoftherose/deep-learning-showcase:latest'
      }
    }
  }
}
