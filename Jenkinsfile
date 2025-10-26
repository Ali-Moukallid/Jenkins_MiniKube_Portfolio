pipeline {
  agent any

  triggers {
    // Poll GitHub every 2 minutes
    pollSCM('H/2 * * * *')
  }

  environment {
    IMAGE_TAG = ""
  }

  stages {

    stage('Checkout') {
      steps {
        echo "📦 Checking out latest code from GitHub..."
        git branch: 'main', url: 'https://github.com/Ali-Moukallid/Jenkins_MiniKube_Portfolio'
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        script {
          // Generate a unique image tag using timestamp
          def buildTag = new Date().format("yyyyMMddHHmmss")
          env.IMAGE_TAG = buildTag

          // Switch to Minikube Docker and build the image
          bat '''
          REM === Switch Docker to Minikube Docker ===
          call minikube docker-env --shell=cmd > docker_env.bat
          call docker_env.bat
          '''

          // Build with dynamic Groovy variable injection (Windows safe)
          bat "docker build --no-cache -t mydjangoapp:${env.IMAGE_TAG} ."
          bat "docker tag mydjangoapp:${env.IMAGE_TAG} mydjangoapp:latest"

          echo "✅ Built image mydjangoapp:${buildTag}"
        }
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat '''
        REM === Apply the Kubernetes deployment manifest ===
        kubectl apply -f deployment.yaml
        '''

        // Use env var directly here too
        bat "kubectl set image deployment/django-deployment django-container=mydjangoapp:${env.IMAGE_TAG}"
        bat "kubectl rollout status deployment/django-deployment"
        bat "kubectl get pods -o wide"
      }
    }

  }

  post {
    success {
      echo "🎉 Deployment completed successfully with image tag: ${env.IMAGE_TAG}"
    }
    failure {
      echo "❌ Deployment failed. Check the logs above for details."
    }
  }
}
