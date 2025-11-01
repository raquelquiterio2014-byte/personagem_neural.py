import speech_recognition as sr
import pyttsx3
import time

# Inicializa o motor de voz
engine = pyttsx3.init()
engine.setProperty('rate', 180)  # velocidade da fala
engine.setProperty('volume', 1.0)

# Escolher uma voz feminina (Raquel)
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "brasil" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def falar(texto):
    """Faz o personagem Raquel falar"""
    print("Raquel:", texto)
    engine.say(texto)
    engine.runAndWait()

def ouvir():
    """Ouve o microfone e retorna o texto reconhecido"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Fale algo...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        comando = r.recognize_google(audio, language="pt-BR")
        print("Você disse:", comando)
        return comando.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        falar("Erro ao conectar com o serviço de voz.")
        return ""

def responder(frase):
    """Define as reações e respostas da Raquel"""
    if "olá" in frase or "oi" in frase:
        falar("Oi! Tudo bem? Eu sou a Raquel, sua nova amiga.")
    elif "como você está" in frase:
        falar("Estou ótima, obrigada por perguntar!")
    elif "qual o seu nome" in frase:
        falar("Meu nome é Raquel, prazer em falar com você!")
    elif "tchau" in frase or "até mais" in frase:
        falar("Tchau! Até a próxima!")
        return False
    elif frase.strip() == "":
        falar("Não consegui entender, pode repetir?")
    else:
        falar("Interessante! Conte-me mais sobre isso.")
    return True

# Loop principal
if __name__ == "__main__":
    falar("Olá! Eu sou a Raquel. Pode falar comigo.")
    ativo = True
    while ativo:
        comando = ouvir()
        ativo = responder(comando)
        time.sleep(1)
