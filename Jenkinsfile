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
                            pip install python-Levenshtein
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            venv\\Scripts\\activate
                            pip install -r requisitos.txt
                            pip install python-Levenshtein
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
                            python tests/levenshtein_test.py
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
                echo 'Verificando o arquivo de perguntas'
                script {
                    if (isUnix()) {
                        sh 'cat perguntas.txt'
                    } else {
                        bat 'type perguntas.txt'
                    }
                }
            }
        }
        stage('Execução do Chatbot') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            source venv/bin/activate
                            echo -e "qual a capital do Brasil?\nsair\n" | python chat_bot.py
                        '''
                    } else {
                        bat '''
                            venv\\Scripts\\activate
                            echo qual a capital do Brasil? > input.txt
                            echo sair >> input.txt
                            python chat_bot.py < input.txt
                        '''
                    }
                }
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
