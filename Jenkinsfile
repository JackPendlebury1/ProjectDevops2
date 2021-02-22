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
                            sh '''
                            cd service-1-frontend
                            '''
                            image = docker.build("neinomas/prize-gen-service1")
                            sh '''
                            cd ..
                            cd service-2-char-gen
                            cd ..
                            '''
                            image1 = docker.build("neinomas/prize-gen-service2")
                            sh '''
                            cd service-3-num-gen
                            cd ..
                            '''
                            image2 = docker.build("neinomas/prize-gen-service3")
                            sh '''
                            cd service-4-prize-gen
                            cd ..
                            '''
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