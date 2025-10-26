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
          // 🔖 Generate a unique tag (e.g. 20251026190545)
          def buildTag = new Date().format("yyyyMMddHHmmss")
          echo "🔖 Generated build tag: ${buildTag}"

          // Switch Jenkins Docker daemon to Minikube
          bat '''
          call minikube docker-env --shell=cmd > docker_env.bat
          call docker_env.bat
          '''

          // Build and tag image (use Groovy interpolation, not env vars)
          bat """
          docker build --no-cache -t mydjangoapp:${buildTag} .
          docker tag mydjangoapp:${buildTag} mydjangoapp:latest
          """

          // Save tag for later stages
          env.IMAGE_TAG = buildTag

          echo "✅ Built image mydjangoapp:${buildTag}"
        }
      }
    }

    stage('Deploy to Minikube') {
      steps {
        script {
          echo "🚀 Deploying to Minikube with image tag: ${env.IMAGE_TAG}"

          // Apply manifest (creates or updates Deployment)
          bat "kubectl apply -f deployment.yaml"

          // Update the image of the existing deployment
          bat "kubectl set image deployment/django-deployment django-container=mydjangoapp:${env.IMAGE_TAG}"

          // Wait for rollout completion
          bat "kubectl rollout status deployment/django-deployment"

          // Display running pods for verification
          bat "kubectl get pods -o wide"
        }
      }
    }

    stage('Health Check') {
      steps {
        echo "🩺 Checking pod health..."
        // Check if pods are ready (avoids silent rollout hangs)
        bat 'kubectl get pods --no-headers | findstr /v Running && exit /b 1 || echo All pods are running.'
      }
    }

  }

  post {
    success {
      echo "🎉 Deployment completed successfully with image tag: ${env.IMAGE_TAG}"
    }
    failure {
      echo "❌ Deployment failed. Check the logs above for details."
      bat 'kubectl get pods -o wide'
    }
  }
}
