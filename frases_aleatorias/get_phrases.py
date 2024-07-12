import random
import requests
from datetime import datetime

# URL da API do MyMemory Translation API v2
MYMEMORY_TRANSLATE_URL = 'https://api.mymemory.translated.net/get'

def translate_text(text, target_language='pt'):
    params = {
        'q': text,
        'langpair': 'en|' + target_language
    }
    response = requests.get(MYMEMORY_TRANSLATE_URL, params=params)
    if response.status_code == 200:
        translated_text = response.json()['responseData']['translatedText']
        return translated_text
    else:
        return text  # Retorna o texto original se houver erro na tradução

def get_random_events():
    # Obter data atual
    today = datetime.today()
    month = today.month
    day = today.day

    # Construir a URL da API com o dia e mês atual
    url = f"https://today.zenquotes.io/api/{month}/{day}/"

    # Fazer o request GET para a API
    response = requests.get(url)

    event_phrases = []
    birth_events = []
    death_events = []

    if response.status_code == 200:
        try:
            # Decodificar o conteúdo da resposta de bytes para string
            json_data = response.json()

            # Percorrer todas as entradas da categoria "Events" no dicionário JSON
            for event in json_data["data"]["Events"]:
                # Substituir o código HTML por um travessão real
                event_text = event["text"].replace("&#8211;", "-")
                event_phrases.append(event_text)

            for event in json_data["data"]["Births"]:
                birth_text = event["text"].replace("&#8211;", "-")
                birth_events.append(birth_text)

            for event in json_data["data"]["Deaths"]:
                death_text = event["text"].replace("&#8211;", "-")
                death_events.append(death_text)

            # Escolher aleatoriamente uma frase de evento da lista de frases
            random_event_phrase = random.choice(event_phrases)

            # Traduzir a frase escolhida
            translated_event = translate_text(random_event_phrase)

            # Escolher aleatoriamente um evento de nascimento e morte
            random_birth_event = random.choice(birth_events)
            random_death_event = random.choice(death_events)

            # Traduzir os eventos de nascimento e morte
            translated_birth_event = translate_text(random_birth_event)
            translated_death_event = translate_text(random_death_event)

            # Retornar os resultados como um dicionário
            return {
                'event': translated_event,
                'birth': f"Nascido(a) em {translated_birth_event}",
                'death': f"Falecido(a) em {translated_death_event}"
            }

        except ValueError:
            return {'error': 'Erro: Resposta não é um JSON válido.'}

    else:
        return {'error': f"Erro ao fazer request: {response.status_code}"}

# Exemplo de uso da função
if __name__ == "__main__":
    results = get_random_events()
    if 'error' in results:
        print(results['error'])
    else:
        print(results['event'])
        print(results['birth'])
        print(results['death'])
