pipeline {
	agent any
	parameters {
		booleanParam(name: 'buildImage', defaultValue: false, description: 'Re-builds the docker image')
	}

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
		stage('Build image'){
			when {
				expression {
					return params.buildImage
				}
			}
			steps {
				sh 'docker build -t mkdocs-pdf:1.0 .'
			}
		}
		stage('Building') {
			agent {
				docker { image 'mkdocs-pdf:1.0' }
			}
			steps {
				sh '/usr/local/bin/mkdocs build'
			}
		}
		stage('Deploy') {
			steps {
				sh 'rsync -avh --no-perms --no-owner --no-group --delete site/ /var/www/ms-docs/'
			}
		}
	}
}
