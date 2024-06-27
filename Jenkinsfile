pipeline {
    agent any

    parameters {
        string(name: 'Pergunta', defaultValue: 'Digite sua pergunta aqui', description: 'Insira a pergunta no campo abaixo.')
    }
    environment{
        PATH = "C:\\Windows\\System32;C:\\windows;C:\\windows\\Scripts;${env.PATH}"
    }
    stages {
        stage('Preparação do Ambiente') {
            steps {
                echo 'Instalando virtualenv...'
                script {
                    bat '''
                        python -m venv venv
                        venv\\Scripts\\activate
                        pip install -r requisitos.txt
                        pip install python-Levenshtein
                    '''
                }
            }
        }
        stage('Execução do Teste Levenshtein') {
            steps {
                script {
                    bat '''
                        venv\\Scripts\\activate
                        python tests\\levenshtein_test.py
                    '''
                }
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
                script {
                    def perguntaUsuario = params.Pergunta
                    bat """
                        venv\\Scripts\\activate
                        python chat_bot.py \"${perguntaUsuario}\"
                    """
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline concluído.'
        }
        success {
            echo 'Pipeline executado com sucesso!'
        }
        failure {
            echo 'Pipeline falhou. Verificar logs para mais detalhes.'
        }
    }
}
