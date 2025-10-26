pipeline {
  agent any

  triggers {
    // Poll GitHub every 2 minutes
    pollSCM('H/2 * * * *')
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
          // 🔖 Create timestamp tag and store globally
          IMAGE_TAG = new Date().format("yyyyMMddHHmmss")
          echo "🔖 Generated image tag: ${IMAGE_TAG}"

          // Switch Docker to Minikube environment
          bat '''
          call minikube docker-env --shell=cmd > docker_env.bat
          call docker_env.bat
          '''

          // Build and tag image with timestamp
          bat """
          docker build --no-cache -t mydjangoapp:${IMAGE_TAG} .
          docker tag mydjangoapp:${IMAGE_TAG} mydjangoapp:latest
          """

          echo "✅ Built image mydjangoapp:${IMAGE_TAG}"
        }
      }
    }

    stage('Deploy to Minikube') {
      steps {
        script {
          echo "🚀 Deploying to Minikube with image tag: ${IMAGE_TAG}"

          bat "kubectl apply -f deployment.yaml"
          bat "kubectl set image deployment/django-deployment django-container=mydjangoapp:${IMAGE_TAG}"
          bat "kubectl rollout status deployment/django-deployment"
          bat "kubectl get pods -o wide"
        }
      }
    }

    stage('Health Check') {
      steps {
        echo "🩺 Checking pod health..."
        bat 'kubectl get pods --no-headers | findstr /v Running && exit /b 1 || echo ✅ All pods are running.'
      }
    }
  }

  post {
    success {
      echo "🎉 Deployment completed successfully with image tag: ${IMAGE_TAG}"
    }
    failure {
      echo "❌ Deployment failed. Check logs above."
      bat 'kubectl get pods -o wide'
    }
  }
}
