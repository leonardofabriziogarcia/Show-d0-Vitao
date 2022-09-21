ja_foi_perg = []
def gera_pergunta(ja_foi_perg):
    from gera_lista_pergunta import gera_lista_pergunta
    lista = gera_lista_pergunta()
    import random
    ja_foi_resp = []
    lista_pergunta = []
    dic_pergunta = {}
    alternativas = 1
    perguntas=True
    while  perguntas:
        questao = random.randint(0,len(lista)-1)
        if ja_foi_perg.count(questao) == 0:
            ja_foi_perg.append(questao)
            for pergunta in (lista[questao]['pergunta']):
                lista_pergunta.append(pergunta)
                dic_pergunta['pergunta']=lista_pergunta
            perguntas = False
    while len(ja_foi_resp)!=4:
        alternativa = random.randint(0,3)
        if ja_foi_resp.count(alternativa) == 0:
            if alternativa != 0:
                ja_foi_resp.append(alternativa)
                dic_pergunta[alternativas]= lista[questao]['resposta'][alternativa]
                alternativas +=1
            else:
                ja_foi_resp.append(alternativa)
                dic_pergunta[alternativas]= lista[questao]['resposta'][alternativa]
                certa = alternativas
                alternativas +=1


        
    return dic_pergunta,ja_foi_perg,certa

if __name__ == '__main__':
    gera_pergunta(ja_foi_perg)
