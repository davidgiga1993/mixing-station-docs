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
		stage('Export Versions'){
			steps {
				script {
					docker.image('mixing-station-pc:latest').inside {
						sh 'java -jar /app/mixing-station-desktop.jar -expFw versions.json'
					}
				}
			}
		}
		stage('Building') {
			steps {
				script {
					docker.image('mkdocs-pdf:1.0').inside {
						sh 'python3 sort-nav.py'
						sh '/usr/local/bin/mkdocs build'
					}
				}
			}
		}
		stage('Deploy') {
			steps {
				sh 'rsync -avh --no-perms --no-owner --no-group --delete site/ /var/www/ms-docs/'
			}
		}

		stage('Flush cache'){
			steps {
				script {
					withCredentials([file(credentialsId: 'app-uploader-secrets', variable: 'FILE')]) {
						def secretRootDir = new File("${FILE}").getParentFile().getAbsolutePath()
						def configFiles = "${FILE},config.cfg"

						def dockerArgs = ' --mount src=' + secretRootDir + ',dst=' + secretRootDir + ',type=bind '
						docker.image('dev-core:app-uploader-1.0').inside(dockerArgs) { c ->
							dir('cicd') {
								sh 'java -jar /app/app-uploader.jar --configs ' + configFiles+ ' --call ClearCache'
							}
						}
					}
				}
			}
		}
	}
}
