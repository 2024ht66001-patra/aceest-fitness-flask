pipeline {
  agent any

  parameters {
    string(name: 'GIT_REPO', defaultValue: 'https://github.com/2024ht66001-patra/aceest-fitness-flask.git', description: 'Git repository URL to clone. Leave empty to use Pipeline SCM.')
    string(name: 'GIT_CRED_ID', defaultValue: '', description: 'Optional Jenkins credentialsId for accessing the Git repo')
  }

  environment {
    IMAGE_NAME = "aceest/aceest-fitness-flask:${env.BUILD_NUMBER ?: 'latest'}"
    APP_PORT = "5000"
  }

  stages {
    stage('Checkout') {
      steps {
        script {
          if (params.GIT_REPO?.trim()) {
            if (params.GIT_CRED_ID?.trim()) {
              git url: params.GIT_REPO, credentialsId: params.GIT_CRED_ID
            } else {
              git url: params.GIT_REPO
            }
          } else {
            checkout scm
          }
        }
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          sh "docker build -t ${IMAGE_NAME} ."
        }
      }
    }

    stage('Run & Smoke Test') {
      steps {
        script {
          sh '''
            set -e
            cid=$(docker run -d -p ${APP_PORT}:5000 ${IMAGE_NAME})
            echo "Started container $cid"
            success=1
            for i in $(seq 1 15); do
              if curl -fsS http://localhost:${APP_PORT}/ >/dev/null 2>&1; then
                echo "App responded"
                success=0
                break
              fi     fi
              echo "Waiting for app... ($i)"       echo "Waiting for app... ($i)"
              sleep 1         sleep 1
            done            done
            if [ "$success" -ne 0 ]; thencess" -ne 0 ]; then
              echo "App did not start, container logs:" echo "App did not start, container logs:"
              docker logs $cid || true
              docker rm -f $cid || true       docker rm -f $cid || true
              exit 1         exit 1
            fi         fi
            docker rm -f $cid || true            docker rm -f $cid || true
          '''  '''
        }
      }
    }

    stage('Archive') {tage('Archive') {
      steps {   steps {
        archiveArtifacts artifacts: 'Dockerfile,run.py,requirements.txt', fingerprint: true       archiveArtifacts artifacts: 'Dockerfile,run.py,requirements.txt', fingerprint: true












}  }    }      }        sh "docker images --format '{{.Repository}}:{{.Tag}} {{.Size}}' || true"      script {    always {  post {  }    }      }      }
    }
  }

  post {
    always {
      script {
        sh "docker images --format '{{.Repository}}:{{.Tag}} {{.Size}}' || true"
      }
    }
  }
}