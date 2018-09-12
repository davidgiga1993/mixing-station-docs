pipeline {
	agent any

	stages {
		stage('Trigger setup') {
			steps {
				script {
					properties([pipelineTriggers([githubPush()])])
				}
			}
		}
		stage('Checkout') {
			steps {
				git branch: 'master', url: 'https://github.com/davidgiga1993/mixing-station-docs.git'
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