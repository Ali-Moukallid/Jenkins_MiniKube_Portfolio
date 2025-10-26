pipeline {
  agent any

  triggers {
    // Poll GitHub every 2 minutes
    pollSCM('H/2 * * * *')
  }

  environment {
    // Use this to store and reuse your image tag within the pipeline
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

          bat """
          REM === Switch Docker to Minikube Docker ===
          call minikube docker-env --shell=cmd > docker_env.bat
          call docker_env.bat

          REM === Build Django image inside Minikube Docker ===
          docker build --no-cache -t mydjangoapp:%IMAGE_TAG% .

          REM === Tag image as latest for convenience ===
          docker tag mydjangoapp:%IMAGE_TAG% mydjangoapp:latest
          """

          echo "✅ Built image mydjangoapp:${buildTag}"
        }
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat """
        REM === Apply the Kubernetes deployment manifest ===
        kubectl apply -f deployment.yaml

        REM === Update the image to the new build tag ===
        kubectl set image deployment/django-deployment django-container=mydjangoapp:%IMAGE_TAG%

        REM === Wait for rollout to finish ===
        kubectl rollout status deployment/django-deployment

        REM === Verify pods ===
        kubectl get pods -o wide
        """
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
