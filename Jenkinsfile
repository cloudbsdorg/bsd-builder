pipeline {
    agent {
    	label 'freebsd_12_1'
    }
	stages {
		stage('Install Dependencies') {
			steps {
				sh 'sudo pkg install -y python3'
			}
		}
		stage('Build') {
			steps {
				 sh 'echo "Buld"'
			}
		}
        stage('Unit Tests') {
			steps {
				sh 'echo "Unit Tests Here"'
			}
		}
		stage('Publish') {
			steps {
				sh 'echo "Publish Here"'
			}
		}
    }
}

