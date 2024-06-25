pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/JoaoVictorGarcia2/python_pln']]])
            }
        }
        stage('Preparação do Ambiente') {
            steps {
                echo 'Instalando virtualenv...'
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv venv
                            source venv/bin/activate
                            pip install -r requisitos.txt
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            venv\\Scripts\\activate
                            pip install -r requisitos.txt
                        '''
                    }
                }
            }
        }
        stage('Execução do Teste Levenshtein') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            source venv/bin/activate
                            python levenshtein_test.py
                        '''
                    } else {
                        bat '''
                            venv\\Scripts\\activate
                            python tests\\levenshtein_test.py
                        '''
                    }
                }
            }
        }
        stage('Verificação do Arquivo de Perguntas') {
            steps {
                echo 'Verificação do Arquivo de Perguntas'
            }
        }
        stage('Execução do Chatbot') {
            steps {
                echo 'Execução do Chatbot'
            }
        }
    }
    post {
        failure {
            echo 'Pipeline falhou.'
        }
        success {
            echo 'Pipeline executado com sucesso.'
        }
    }
}
