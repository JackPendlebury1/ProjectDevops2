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
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=app --cov-report=term-missing
                    cd ..
                    cd service-2-char-gen
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=app --cov-report=term-missing
                    cd ..
                    cd service-3-num-gen
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=app --cov-report=term-missing
                    cd ..
                    cd service-4-prize-gen
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=app --cov-report=term-missing
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
                        sh "cd ansible && ansible-playbook -i inventory.yaml playbook.yaml"
                    }
                }
            }
            stage('Deploy App'){
                steps{
                    sh '''
                    ssh -i ~/.ssh/id_rsa wistyhodgson@10.132.0.9 << EOF
                        rm -rf ProjectDevops2
                        git clone https://github.com/JackPendlebury1/ProjectDevops2.git && cd ProjectDevops2
                        export rootpass=$rootpass
                        export SECRET_KEY=$SECRET_KEY
                        export app_version=${app_version}
                        docker stack deploy --compose-file docker-compose.yaml project2
                        exit
                    EOF
                    ssh -i ~/.ssh/id_rsa wistyhodgson@10.132.0.8 << EOF
                        git clone https://github.com/JackPendlebury1/ProjectDevops2.git && cd ProjectDevops2
                        cd nginx
                        docker run -d -p 80:80 --name nginx --mount type=bind,source=$(pwd)/nginx.conf,target=/etc/nginx/nginx.conf nginx
                    '''
                }
            }
        }
}