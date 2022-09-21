def gera_lista_pergunta():
    lista_perguntas = open("perguntas.txt", "r", encoding="utf-8")
    
    conteudo = "oi"
    lista = []
    dicio = {}
    resposta = []
    pergunta = []
    
    
    while conteudo != "":
            conteudo = lista_perguntas.readline()
            conteudo = conteudo.replace('\n','')
            if(conteudo == "Pergunta"):
                is_pergunta = True
                lista.append(dicio)
                resposta = []
                dicio = {}
                pergunta = []
                continue
            elif (conteudo=="Resposta"):
                is_pergunta = False
                continue
            if is_pergunta == True:
                pergunta.append(conteudo)
                dicio['pergunta'] = pergunta
            else: 
                resposta.append(conteudo)
                dicio['resposta'] = resposta
    del lista[0]
    lista_perguntas.close()
    return lista