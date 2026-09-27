#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

// Função para converter em minúsculas
void minusculas(char *texto) {
    for (int i = 0; texto[i]; i++)
        texto[i] = tolower(texto[i]);
}

// Função para Raquel falar com voz
void falar(const char *texto) {
#ifdef _WIN32
    char comando[512];
    snprintf(comando, sizeof(comando), "espeak \"%s\" -v pt+f4 -s 150", texto);
#else
    char comando[512];
    snprintf(comando, sizeof(comando), "espeak \"%s\" -v pt+f4 -s 150 2>/dev/null", texto);
#endif
    system(comando);
}

// Função para detectar emoção
const char* detectar_emocao(const char *texto) {
    if (strstr(texto, "oi") || strstr(texto, "tudo bem"))
        return "😊";
    if (strstr(texto, "triste") || strstr(texto, "mal"))
        return "😢";
    if (strstr(texto, "feliz") || strstr(texto, "ótimo"))
        return "😄";
    if (strstr(texto, "raiva") || strstr(texto, "bravo"))
        return "😠";
    if (strstr(texto, "fatec") || strstr(texto, "estudo"))
        return "🎓";
    return "🤔";
}

// Função para responder conforme emoção
const char* resposta_da_raquel(const char *texto) {
    if (strstr(texto, "oi"))
        return "Oi! Eu sou a Raquel, estudante de ADS na Fatec Campinas!";
    if (strstr(texto, "tudo bem"))
        return "Estou bem, estudando programação! E você?";
    if (strstr(texto, "fatec"))
        return "Ah, a Fatec Campinas é incrível! Eu amo estudar lá!";
    if (strstr(texto, "programar"))
        return "Adoro programar em C e Python! Você também gosta?";
    if (strstr(texto, "triste"))
        return "Poxa, não fica triste... Tudo melhora, viu?";
    if (strstr(texto, "tchau"))
        return "Tchau! Foi ótimo conversar com você!";
    return "Hmm... não sei bem o que dizer, mas estou aqui para ouvir!";
}

int main() {
    char entrada[200];

    printf("👩‍💻 Raquel: Oi! Eu sou a Raquel, estudante de ADS na Fatec Campinas.\n");
    falar("Oi! Eu sou a Raquel, estudante de A D S na Fatec Campinas.");

    printf("Vamos conversar! (digite 'sair' para encerrar)\n\n");

    while (1) {
        printf("Você: ");
        fgets(entrada, sizeof(entrada), stdin);
        entrada[strcspn(entrada, "\n")] = '\0'; // remover \n
        minusculas(entrada);

        if (strcmp(entrada, "sair") == 0) {
            falar("Até mais! Continue estudando programação!");
            printf("Raquel 🎓: Até mais! Continue estudando programação!\n");
            break;
        }

        const char *emocao = detectar_emocao(entrada);
        const char *resposta = resposta_da_raquel(entrada);

        printf("Raquel %s: %s\n", emocao, resposta);
        falar(resposta);
    }

    return 0;
}
