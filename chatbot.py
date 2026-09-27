"""Small rule-based study companion; no neural model is used here."""


def respond(message):
    text = message.strip().casefold()
    if not text:
        return "Escreva uma mensagem para começarmos."
    if any(word in text for word in ("tchau", "até mais")):
        return "Tchau! Boa sorte nos seus estudos!"
    if "como você está" in text:
        return "Estou bem, obrigada! E você?"
    if "fatec" in text or "ads" in text:
        return "Sou uma personagem estudante de ADS na Fatec Campinas."
    if "python" in text or "programação" in text:
        return "Gosto de praticar programação. Qual conceito você está estudando?"
    if "oi" in text or "olá" in text:
        return "Olá! Vamos conversar sobre estudos e programação?"
    return "Não tenho uma resposta preparada para isso. Pode reformular?"


def main():
    print("RaquelBot: Olá! Digite 'sair' para encerrar.")
    while True:
        try:
            message = input("Você: ")
        except (EOFError, KeyboardInterrupt):
            print("\nRaquelBot: Até a próxima!")
            break
        if message.strip().casefold() in {"sair", "fim"}:
            print("RaquelBot: Até a próxima!")
            break
        print("RaquelBot:", respond(message))


if __name__ == "__main__":
    main()
