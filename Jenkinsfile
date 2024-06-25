pipeline {
    agent {
        label 'docker-agent-python'
    }

    stages {
        stage('Preparação do Ambiente') {
            steps {
                echo 'Ja instalado'
            }
        }

        stage('Instalação de Dependências') {
            steps {
                sh 'pip install -r requisitos.txt'
            }
        }

        stage('Execução do Teste Levenshtein') {
            steps {
                sh 'python3 levenshtein_teste.py'
            }
        }

        stage('Verificação do Arquivo de Perguntas') {
            steps {
                script {
                    if (fileExists('perguntas.txt')) {
                        echo 'Arquivo perguntas.txt encontrado!'
                    } else {
                        error('Arquivo perguntas.txt não encontrado. Interrompendo o pipeline.')
                    }
                }
            }
        }

        stage('Execução do Chatbot') {
            steps {
                sh 'python3 chat_bot.py'
            }
        }
    }
}
