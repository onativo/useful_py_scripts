# O que faz
Esse script apenas consulta numa das APIs do https://zenquotes.io/ e retorna três frases:
1 - Evento histórico do dia da consulta
2 - O nascimento de uma pessoa importante da história naquele dia
3 - A morte de uma pessoa importante da história naquele dia

A API do zendesk retorna os resultados em inglês, e, para resolver isso, fazemos ainda a consulta numa segunda API para que o resultado seja traduzido: https://api.mymemory.translated.net/
Desta forma, os resultados são apresentados sempre em PT-BR

# Como utilizar:
Apenas execute na linha de comando: `python3 get_phrases.py` e o resultado deve ser semelhante a isso:

- 1799 - Ranjit Singh conquista Lahore e torna-se marajá do Punjab (Império Sikh)
- Nascido(a) em 1974 - Sharon den Adel, cantora e compositora holandesa
- Falecido(a) em 2008 - Bobby Murcer, jogador de beisebol, treinador e apresentador esportivo norte-americano (n. 1946)

