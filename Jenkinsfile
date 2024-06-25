pipeline {
    agent any

    stages {
        stage('Preparação do Ambiente') {
            steps {
                echo 'Instalando virtualenv...'
                sh 'python3 -m venv venv'
                sh './venv/bin/python -m ensurepip --upgrade'
                sh './venv/bin/pip install -r requisitos.txt'
                echo 'Dependências instaladas.'
            }
        }

        stage('Execução do Teste Levenshtein') {
            steps {
                echo 'Executando teste Levenshtein...'
                sh './venv/bin/python levenshtein_teste.py'
                echo 'Teste Levenshtein concluído.'
            }
        }

        stage('Verificação do Arquivo de Perguntas') {
            steps {
                echo 'Verificando arquivo de perguntas...'
                script {
                    if (fileExists('perguntas.txt')) {
                        echo 'Arquivo perguntas.txt encontrado!'
                    } else {
                        error('Arquivo perguntas.txt não encontrado. Interrompendo o pipeline.')
                    }
                }
                echo 'Verificação do arquivo de perguntas concluída.'
            }
        }

        stage('Execução do Chatbot') {
            steps {
                echo 'Executando chatbot...'
                sh './venv/bin/python chat_bot.py'
                echo 'Chatbot executado.'
            }
        }
    }
}
