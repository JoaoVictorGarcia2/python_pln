pipeline {
    agent any
    stages {
        stage('Preparação do Ambiente') {
            steps {
                echo 'Instalando virtualenv...'
                script {
                    if (isUnix()) {
                        sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requisitos.txt'
                    } else {
                        bat 'python -m venv venv && venv\\Scripts\\activate && pip install -r requisitos.txt'
                    }
                }
            }
        }
        stage('Execução do Teste Levenshtein') {
            steps {
                script {
                    if (isUnix()) {
                        sh '. venv/bin/activate && python levenshtein_test.py'
                    } else {
                        bat 'venv\\Scripts\\activate && python levenshtein_test.py'
                    }
                }
            }
        }
        stage('Verificação do Arquivo de Perguntas') {
            steps {
                script {
                    if (isUnix()) {
                        sh '. venv/bin/activate && python verifica_perguntas.py'
                    } else {
                        bat 'venv\\Scripts\\activate && python verifica_perguntas.py'
                    }
                }
            }
        }
        stage('Execução do Chatbot') {
            steps {
                script {
                    if (isUnix()) {
                        sh '. venv/bin/activate && python chatbot.py'
                    } else {
                        bat 'venv\\Scripts\\activate && python chatbot.py'
                    }
                }
            }
        }
    }
}
