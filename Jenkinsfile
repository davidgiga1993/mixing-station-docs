pipeline {
	agent any

	stages {
		stage('Checkout') {
			steps{
				checkout scm
			}
		}
		stage('Building') {
			steps {
				sh '/usr/local/bin/mkdocs build'
			}
		}
		stage('Deploy') {
			steps {
				sh 'rsync -avh --no-perms --no-owner --no-group --delete site/ /var/www/wordpress/ms-docs/'
			}
		}
	}
}