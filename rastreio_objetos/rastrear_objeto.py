import requests
from bs4 import BeautifulSoup

def rastrear_objeto(codigo_rastreamento):
    """
    Função para rastrear um objeto nos Correios utilizando o código de rastreamento.
    
    Args:
        codigo_rastreamento (str): Código de rastreamento do objeto.
    """
    url = f"https://www.linkcorreios.com.br/?id={codigo_rastreamento}"
    
    try:
        # Fazendo a requisição à URL
        response = requests.get(url)
        response.raise_for_status()  # Gera uma exceção se o status HTTP não for bem-sucedido

        # Fazendo o parsing do HTML da página
        soup = BeautifulSoup(response.content, "html.parser")

        # Obtendo o título principal
        main_title_element = soup.find("div", class_="main_title_3")
        if main_title_element and main_title_element.h2:
            last_status_title = main_title_element.h2.text.strip()
            print(f"📦 {last_status_title}")
        else:
            print("⚠️ Div com a classe 'main_title_3' ou elemento <h2> não encontrada.")

        # Obtendo os detalhes do status
        status_list = soup.find("ul", class_="linha_status")
        if status_list:
            for li in status_list.find_all("li"):
                # Extraindo o conteúdo de cada item da lista
                text = li.text.strip()
                # Identificando se o texto possui formato de Data, Origem ou Destino
                if "Data" in text:
                    print(f"  📅 {text}")
                elif "Origem" in text:
                    print(f"  📍 {text}")
                elif "Destino" in text:
                    print(f"  🎯 {text}")
                else:
                    print(f"⚠️ {text}")  # Outros textos que não se encaixam
        else:
            print("⚠️ Lista de status ('ul' com classe 'linha_status') não encontrada.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")

# Exemplo de uso
codigo = "AA361458846BR"
rastrear_objeto(codigo)
