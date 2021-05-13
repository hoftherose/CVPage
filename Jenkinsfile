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
        sh '''#!/bin/bash
        docker build -t hoftherose/deep-learning-showcase:$(git log -1 --pretty=%B | awk '{print $1;}') .  
        '''
      }
    }
    stage('pushImage') {
      steps { 
        sh '''#!/bin/bash
        docker push hoftherose/deep-learning-showcase:$(git log -1 --pretty=%B | awk '{print $1;}')
        '''
      }
    }
    stage('deployAppGCP') {
      steps {
        sh '''#!/bin/bash
          gcloud builds submit -t gcr.io/project-showcase-313416/deep-learning-showcase:$(git log -1 --pretty=%B | awk '{print $1;}') .
        '''
      }
    }
    stage('deployAppGCPLatest') {
      steps {
        sh '''#!/bin/bash
          gcloud builds submit -t gcr.io/project-showcase-313416/deep-learning-showcase:latest .
        '''
      }
    }
  }
}
