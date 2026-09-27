# personagem_raquel.py
import random
import time

def falar(texto):
    """Exibe o texto com um pequeno atraso, simulando fala."""
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.02)
    print()

def resposta_raquel(mensagem):
    """Gera respostas simples baseadas na entrada do usuário."""
    mensagem = mensagem.lower()

    if "oi" in mensagem or "olá" in mensagem:
        return random.choice([
            "Oi! Tudo bem? 😊",
            "Olá! Que bom te ver por aqui!",
            "E aí! Como você está?"
        ])
    elif "fatec" in mensagem or "ads" in mensagem:
        return "Ah, sim! Eu estudo Análise e Desenvolvimento de Sistemas na Fatec Campinas. É um curso incrível! 💻"
    elif "programação" in mensagem or "python" in mensagem:
        return "Adoro programar em Python! Simples e poderosa, né? 🐍"
    elif "tchau" in mensagem or "até" in mensagem:
        return "Tchau! Boa sorte nos seus estudos! 👋"
    elif "como você está" in mensagem:
        return "Tô bem, obrigada por perguntar! E você?"
    elif "faculdade" in mensagem:
        return "A faculdade tá puxada, mas tô aprendendo muito em ADS!"
    else:
        return random.choice([
            "Interessante! Me conta mais sobre isso.",
            "Hmm, não sei se entendi bem. Pode explicar melhor?",
            "Nossa, parece algo legal! 😄"
        ])

def main():
    print("👩‍💻 Raquel (estudante de ADS na Fatec Campinas) está online!")
    print("Digite 'sair' para encerrar a conversa.\n")

    while True:
        usuario = input("Você: ")

        if usuario.lower() in ["sair", "tchau", "fim"]:
            falar("Raquel: Tchau! Até a próxima! 👋")
            break

        resposta = resposta_raquel(usuario)
        falar(f"Raquel: {resposta}")

if __name__ == "__main__":
    main()
