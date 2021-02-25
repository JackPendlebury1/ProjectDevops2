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
                    cd service-1-frontend
                    virtualenv venv
                    source venv/bin/activate
                    pip3 install -r requrirements.txt
                    pytest --cov=app --cov-report=term-missing
                    deactivate
                    cd ..
                    cd service-2-char-gen
                    virtualenv venv
                    source venv/bin/activate
                    pip3 install -r requrirements.txt
                    pytest --cov=app --cov-report=term-missing
                    deactivate
                    cd ..
                    cd service-3-num-gen
                    virtualenv venv
                    source venv/bin/activate
                    pip3 install -r requrirements.txt
                    pytest --cov=app --cov-report=term-missing
                    deactivate
                    cd ..
                    cd service-4-num-gen
                    virtualenv venv
                    source venv/bin/activate
                    pip3 install -r requrirements.txt
                    pytest --cov=app --cov-report=term-missing
                    deactivate
                    cd ..
                    '''
                }
            }
            stage('Build Image & Tag'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            sh "docker-compose build --parallel --build-arg APP_VERSION=${app_version}"
                            
                        }
                    }
                }
            }
            stage('Push'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            docker.withRegistry('', 'docker-hub-credentials'){
                                sh "docker-compose push"
                                sh "docker system prune -af"
                            }
                            
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