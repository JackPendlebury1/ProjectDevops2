pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
            rootpass = credentials("rootpass")
            SECRET_KEY = credentials("SECRET_KEY")
        }
        stages{
            stage('testing'){
                steps{
                    sh '''
                    #!/bin/bash
                    echo testing
                    '''
                }
            }
            stage('Build Image & Tag'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            sh "echo f"
                        }
                    }
                }
            }
            stage('Push'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                                sh "docker-compose build --parallel --build-arg APP_VERSION=${app_version} && docker-compose push --ignore-push-failures"
                                sh "docker system prune -af"
                            }
                            
                        }
                    }
            }
            stage("configuration management ansible"){
                steps{
                    script{
                        sh "echo config"
                    }
                }
            }
            stage('Deploy App'){
                steps{
                    sh "export rootpass=$rootpass"
                    sh "export SECRET_KEY=$SECRET_KEY"
                    sh "docker-compose pull && docker-compose up -d"
                }
            }
        }
}