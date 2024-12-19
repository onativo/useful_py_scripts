# Rastrear Objeto dos Correios

Este script em Python realiza o rastreamento de objetos nos Correios usando o site [Link Correios](https://www.linkcorreios.com.br).
Ele extrai o último status e os detalhes do rastreamento, como data, origem e destino.

## Funcionalidades
- Obtém o último status do objeto a partir do elemento `h2` da div com a classe `main_title_3`.
- Extrai e exibe os detalhes do rastreamento, incluindo:
  - Data
  - Origem
  - Destino
- Tratamento de erros para garantir que o script continue funcionando mesmo em caso de falhas na requisição ou alterações no formato do site.

## Dependências
Antes de usar o script, certifique-se de que as seguintes bibliotecas estão instaladas:

```bash
pip install requests beautifulsoup4
```
# Como usar
Edite o Script e substitua o código de rastreamento pela identificação do objeto que deseja rastrear:

```python
codigo = "AA361458846BR"
rastrear_objeto(codigo)
```

Execute o script diretamente:
```python
python rastrear_objeto.py
```

# Exemplo de Saída
📦 Último Status do Objeto: Objeto em transferência - por favor aguarde

📋 Detalhes do Rastreamento:
- 📅 Data  : 17/12/2024 | Hora: 17:41

  📍 Origem: Agência dos Correios - Sao Paulo / SP
  
  🎯 Destino: Unidade de Tratamento - Sao Paulo / SP
