pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
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
            stage('Build Image, Tag & Push'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            sh "docker-compose build --build-arg APP_VERSION=${app_version} && docker-compose push"
                            sh "docker system prune -af"
                        }
                    }
                }
            }
            stage('Deploy App'){
                steps{
                    sh "docker-compose pull && docker-compose up -d"
                }
            }
        }
}