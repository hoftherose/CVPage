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
    stage('deployAppGCP') {
      steps {
        sh '''#!/bin/bash
          gcloud builds submit -t gcr.io/project-showcase-313416/deep-learning-showcase:$(git log -1 --pretty=%B | awk '{print $1;}') .
        '''
      }
    }
  }
}
