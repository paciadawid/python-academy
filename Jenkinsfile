pipeline {
    agent { dockerfile true }
    environment {
        MSYS_NO_PATHCONV = 1
    }
    stages {
        stage('Test') {
            steps {
                sh 'behave .'
            }
        }
    }
}
