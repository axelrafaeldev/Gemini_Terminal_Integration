#!/usr/bin/env python3
import subprocess
import google.generativeai as genai

#Chamando CowSay
cowsay_output = subprocess.run(['cowsay','-f','bud-frogs', 'Mais alguma pergunta?'], capture_output=True).stdout.decode()
def ler_chave_api(caminho_arquivo):
    """
    Função para ler a chave de API do arquivo de configuração
    """
    with open(caminho_arquivo, 'r') as file:
        return file.read().strip()

# Caminho para o arquivo de configuração
caminho_arquivo_config = '//home/aluno/Documents/config.txt'

# Ler a chave de API do arquivo de configuração
GOOGLE_API_KEY = ler_chave_api(caminho_arquivo_config)

# Configurar a chave de API
genai.configure(api_key=GOOGLE_API_KEY)

# Configurações de geração
generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}

# Configurações de segurança
safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE"
}

# Inicializar o modelo
model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)
chat = model.start_chat(history=[])

def obter_input(mensagem):
    user_input = input(mensagem)
    while user_input.strip() == "":
        user_input = input("Entrada vazia. Por favor, insira uma pergunta ou digite 'sair' para encerrar: ")
    return user_input

# Interagir com o chatbot
prompt = obter_input("-- ")
while prompt.lower() != "sair":
    response = chat.send_message(prompt)
    print("\n\n\n" + response.text + "\n\n")
    prompt = obter_input("\n" + cowsay_output + "\n=======\n=======\n========    ")
