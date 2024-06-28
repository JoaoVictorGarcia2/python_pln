pipeline {
    agent any

    parameters {
        string(name: 'Pergunte_aqui', description: 'Insira a pergunta no campo abaixo.')
    }

    environment {
        PATH = "C:\\Windows\\System32;C:\\windows;C:\\windows\\Scripts;${env.PATH}"
    }

    stages {
        stage('Preparação do Ambiente') {
            steps {
                echo 'Instalando...'
            }
        }

        stage('Execução do Teste Levenshtein') {
            steps {
                bat 'python levenshtein_teste.py'
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
                    def pergunta = params.Pergunte_aqui
                    bat "python chat_bot.py \"${pergunta}\""
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline concluído.'
            emailext(
                to: 'joaovictorgarcia514@gmail.com',
                subject: "Pipeline: ${currentBuild.fullDisplayName}",
                body: """
                <p>O pipeline foi concluído com o seguinte status: ${currentBuild.currentResult}</p>
                <p>Verifique os detalhes do build <a href="${env.BUILD_URL}">aqui</a>.</p>
                """
            )
        }
        success {
            echo 'Pipeline executado com sucesso!'
        }
        failure {
            echo 'Pipeline falhou. Verificar logs para mais detalhes.'
        }
    }
}
