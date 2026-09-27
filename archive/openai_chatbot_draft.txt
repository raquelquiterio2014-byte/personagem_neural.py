memoria = {"nome": "Raquel", "curso": "ADS"}

if "meu nome" in user:
    print(f"Bot: Seu nome é {memoria['nome']}, certo?")
from openai import OpenAI
client = OpenAI(api_key="SUA_CHAVE_AQUI")

while True:
    user = input("Você: ")
    if user.lower() == "sair":
        break
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user}]
    )
    print("Bot:", response.choices[0].message.content)
