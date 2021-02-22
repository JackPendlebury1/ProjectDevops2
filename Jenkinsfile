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
            stage('Build Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            image = docker.build("neinomas/prize-gen-service1")
                            image1 = docker.build("neinomas/prize-gen-service2")
                            image2 = docker.build("neinomas/prize-gen-service3")
                            image3 = docker.build("neinomas/prize-gen-service4")
                        }
                    }
                }
            }
            stage('Tag & Push Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                                image.push("${env.app_version}")
                                image1.push("${env.app_version}")
                                image2.push("${env.app_version}")
                                image3.push("${env.app_version}")
                            }
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