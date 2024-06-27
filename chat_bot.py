import sys
import Levenshtein
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def carregar_perguntas(arquivo):
    perguntas_respostas = {}
    with open(arquivo, "r") as f:
        for linha in f:
            pergunta, resposta = linha.strip().split("|")
            perguntas_respostas[pergunta.lower()] = resposta
    return perguntas_respostas

def encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia=5):
    menor_distancia = float("inf")
    melhor_resposta = ""

    perguntas = list(perguntas_respostas.keys())
    respostas = list(perguntas_respostas.values())

    # Calcular similaridade de Levenshtein
    for p, r in perguntas_respostas.items():
        distancia = Levenshtein.distance(pergunta, p)
        if distancia < menor_distancia:
            menor_distancia = distancia
            melhor_resposta = r

    if menor_distancia <= limiar_distancia:
        return melhor_resposta

    # Se não encontrar com Levenshtein, usar Cosine Similarity
    vectorizer = TfidfVectorizer().fit_transform(perguntas)
    vectors = vectorizer.transform([pergunta])
    cosine_similarities = cosine_similarity(vectors, vectorizer).flatten()
    highest_similarity_index = cosine_similarities.argmax()
    if cosine_similarities[highest_similarity_index] > 0.2:  # Ajuste este valor conforme necessário
        return respostas[highest_similarity_index]

    return "Pergunta não encontrada."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python chat_bot.py <pergunta>")
        sys.exit(1)

    pergunta = sys.argv[1].lower()
    perguntas_respostas = carregar_perguntas("perguntas.txt")
    limiar_distancia = 10

    resposta = encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia)
    print("Resposta:", resposta)
