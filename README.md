# RaquelBot: experiments with conversational characters

This repository records several learning experiments in Python and C. **The maintained starter demonstration is `chatbot.py`**, a terminal chatbot using rules and keyword matching. It is not a neural network or a trained AI model. The repository name reflects the original exploration, not the technology used by every file.

## Run the starter chatbot

Requires Python 3.8+; no external packages or API key.

```bash
python chatbot.py
```

Try `oi`, `Python`, `Fatec`, an unknown topic, and `sair`.

```text
RaquelBot: Olá! Digite 'sair' para encerrar.
Você: Estou aprendendo Python
RaquelBot: Gosto de praticar programação. Qual conceito você está estudando?
```

Run the small behavior checks from the repository root:

```bash
python -m unittest discover -s tests
```

## Archived experiments

Older drafts are grouped under `archive/` so the runnable entry point is clear. These examples show exploration, not a single integrated application.

| File | What it explores | Status and requirements |
| --- | --- | --- |
| `archive/estudante_ads.py`, `archive/amiga_engracada.py` | Python keyword responses | Older drafts; `chatbot.py` is the runnable entry point. |
| `archive/raquel_voz.py` | Microphone recognition and text-to-speech | Experimental; needs `SpeechRecognition`, `pyttsx3`, a working microphone/audio stack and access to Google's recognition service. |
| `archive/dialogo_emocoes.py` | Whisper speech transcription, DialoGPT response, text-to-speech | Experimental; needs `sounddevice`, `numpy`, `openai-whisper`, `transformers`, `torch`, `pyttsx3`, audio hardware, and model downloads. Emotion labels come from **keyword rules**, not an emotion classifier; the avatar is printed text, not animation. |
| `archive/openai_chatbot_draft.txt` | OpenAI API integration draft | Historical draft; it uses a variable before initialization and is not runnable as published. Never place a real API key in a source file. |
| `archive/personagem_raquel.c`, `archive/personagem_raquel_3_1_draft.txt` | C keyword responses and eSpeak | Experimental C drafts; `3.1` has malformed formatting and must be repaired before compilation. |

The original root paths remain available in Git history as evidence of iteration. A next iteration can isolate and repair one audio pipeline, put its dependencies in a dedicated requirements file, and record a short run on the target operating system.

## What this project demonstrates

Python functions, control flow, string matching, interactive input, and the distinction between deterministic rules and model-based dialogue. The larger voice and model experiments indicate areas of study, but need reproducible installation and execution evidence before being used as a finished AI portfolio project.
