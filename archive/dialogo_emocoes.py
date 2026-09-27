import sounddevice as sd
import numpy as np
import whisper
from transformers import AutoModelForCausalLM, AutoTokenizer
import pyttsx3
import torch

# === 1. CAPTURA DE ÁUDIO ===
def gravar_audio(segundos=3, fs=16000):
    print("🎙️ Gravando sua fala...")
    audio = sd.rec(int(segundos * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    audio = audio.flatten().astype(np.float32) / 32768.0
    return audio, fs

# === 2. RECONHECIMENTO DE FALA (ASR) ===
print("🔊 Carregando modelo Whisper...")
asr_model = whisper.load_model("tiny")

def transcrever(audio):
    result = asr_model.transcribe(audio, fp16=False)
    return result["text"]

# === 3. MODELO DE DIÁLOGO ===
print("💬 Carregando modelo de diálogo DialoGPT...")
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
dialog_model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

def gerar_resposta(historico, entrada):
    novo_input = tokenizer.encode(entrada + tokenizer.eos_token, return_tensors='pt')
    bot_input = novo_input if historico is None else torch.cat([historico, novo_input], dim=-1)
    output = dialog_model.generate(bot_input, max_length=bot_input.shape[-1] + 50, pad_token_id=tokenizer.eos_token_id)
    resposta = tokenizer.decode(output[:, bot_input.shape[-1]:][0], skip_special_tokens=True)
    return output, resposta

# === 4. SÍNTESE DE VOZ (TTS) ===
tts = pyttsx3.init()
tts.setProperty('rate', 180)  # velocidade da fala
tts.setProperty('volume', 1.0)

def falar(texto):
    tts.say(texto)
    tts.runAndWait()

# === 5. DETECÇÃO DE EMOÇÃO SIMPLES ===
def detectar_emocao(texto):
    t = texto.lower()
    if any(p in t for p in ["feliz", "ótimo", "alegre", "adorei", "legal"]):
        return "alegria"
    elif any(p in t for p in ["triste", "chateado", "decepcionado"]):
        return "tristeza"
    elif any(p in t for p in ["raiva", "irritado", "bravo", "ódio"]):
        return "raiva"
    else:
        return "neutro"

# === 6. LOOP PRINCIPAL ===
def main():
    print("🤖 Personagem neural pronto! Fale algo para ele... (Ctrl+C para sair)\n")
    historico = None

    while True:
        audio, fs = gravar_audio()
        texto = transcrever(audio).strip()
        if not texto:
            print("❌ Não entendi, tente novamente.\n")
            continue

        print(f"🧍 Você disse: {texto}")
        historico, resposta = gerar_resposta(historico, texto)
        emocao = detectar_emocao(texto)

        # Expressão simples
        if emocao == "alegria":
            expressao = "😄 [Avatar sorri]"
        elif emocao == "tristeza":
            expressao = "😢 [Avatar olha para baixo]"
        elif emocao == "raiva":
            expressao = "😠 [Avatar franze a testa]"
        else:
            expressao = "🙂 [Avatar neutro]"

        print(f"🤖 Personagem ({emocao}): {resposta}")
        print(expressao, "\n")

        # Falar em voz alta
        falar(resposta)

if __name__ == "__main__":
    main()
