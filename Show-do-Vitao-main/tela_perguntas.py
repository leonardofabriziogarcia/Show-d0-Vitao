
import pygame
def perguntas(login,senha):
    ja_foi_perg=[]
    import random
    dica_univ = True
    dica_plateia = True
    dica_cartas = True
    pulei = True
    num_pulos =3
    respostas = 0
    sera_que_deu_certo = 101
    vai_dar_certo = 101
    quer_jogar = True
    pontuacao = ['0','500','1 mil','2 mil','3 mil','5 mil','10 mil','15 mil','20 mil','30 mil','50 mil','100 mil','200 mil','300 mil','400 mil','500 mil','1 milhão','']
    while respostas<16 and quer_jogar == True:
        tirei_perg = []
        from gera_pergunta import gera_pergunta
        from tela_perdeu import perdeu
        from tela_ganhou import ganhou
        from tela_resp_certa import acertou
        from tela_resp_erro import errou

        pygame.font.init()
        
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode([1280, 720])
        
        dic_pergunta,ja_foi_perg,certa=gera_pergunta(ja_foi_perg)
        perguntas = dic_pergunta['pergunta']
        if len(perguntas)>1:
            tamanho_fonte_pergunta = int(60/len(perguntas))+20
        else:
            tamanho_fonte_pergunta = 60
        fase = True
        branco = (255,255,255)
        tamanho_fonte =75
        tamanho_fonte_valores = 38
        fundo_perguntas = pygame.image.load(r'tela_perguntas_SDV.jpeg')
        retangulo_pergunta1 = pygame.Rect(58,201,710,119)
        retangulo_pergunta2 = pygame.Rect(58,334,710,116)
        retangulo_pergunta3 = pygame.Rect(58,464,710,115)
        retangulo_pergunta4 = pygame.Rect(58,594,710,113)
        plateia = pygame.Rect(797,260,133,100)
        universitario = pygame.Rect(964,260,120,100)
        cartas = pygame.Rect(1123,260,103,100)
        pula_questao = pygame.Rect(797,420,450,100)
        fonte_alternativa = pygame.font.Font(None, tamanho_fonte)
        fonte_pergunta = pygame.font.Font(None,tamanho_fonte_pergunta)
        fonte_pontos = pygame.font.Font(None,tamanho_fonte_valores)
        texto_alternativa_1 = fonte_alternativa.render(dic_pergunta[1],True,branco)
        texto_alternativa_2 = fonte_alternativa.render(dic_pergunta[2],True,branco)
        texto_alternativa_3 = fonte_alternativa.render(dic_pergunta[3],True,branco)
        texto_alternativa_4 = fonte_alternativa.render(dic_pergunta[4],True,branco)
        if respostas -1 >=0:
            pontos_errou =  fonte_pontos.render(pontuacao[respostas-1],True,'red')
        else:
            pontos_errou = fonte_pontos.render('0',True,'red')
        pontos_saiu = fonte_pontos.render(pontuacao[respostas],True,'red')
        pontos_acertou = fonte_pontos.render(pontuacao[respostas+1],True,'red')
        sair_perguntas = pygame.Rect(1180,0,100,100)

        while fase == True:
                coord = 50
                largura_1 = texto_alternativa_1.get_width()+160
                largura_2 = texto_alternativa_2.get_width()+160
                largura_3 = texto_alternativa_3.get_width()+160
                largura_4 = texto_alternativa_4.get_width()+160
                if largura_1 > 757:
                    tamanho_fonte -= 3
                    fonte_alternativa = pygame.font.Font(None, tamanho_fonte)
                    texto_alternativa_1 = fonte_alternativa.render(dic_pergunta[1],True,branco)
                if largura_2 > 757:
                    tamanho_fonte -= 3
                    fonte_alternativa = pygame.font.Font(None, tamanho_fonte)
                    texto_alternativa_2 = fonte_alternativa.render(dic_pergunta[2],True,branco)
                if largura_3 > 757:
                    tamanho_fonte -= 3
                    fonte_alternativa = pygame.font.Font(None, tamanho_fonte)
                    texto_alternativa_3 = fonte_alternativa.render(dic_pergunta[3],True,branco)
                if largura_4 > 757:
                    tamanho_fonte -= 3
                    fonte_alternativa = pygame.font.Font(None, tamanho_fonte)
                    texto_alternativa_4 = fonte_alternativa.render(dic_pergunta[4],True,branco)
                for event in pygame.event.get():
            
                
                    if event.type == pygame.QUIT:
                        return

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if retangulo_pergunta1.collidepoint(event.pos):
                            if dic_pergunta[1] == dic_pergunta[certa]:
                                respostas +=1
                                sera_que_deu_certo  = 101
                                vai_dar_certo = 101
                                acertou()
                                fase = False
                            else:
                                errou(respostas,dic_pergunta[certa],tamanho_fonte,login,senha)


                        if retangulo_pergunta2.collidepoint(event.pos):
                            if dic_pergunta[2] == dic_pergunta[certa]:
                                respostas +=1
                                sera_que_deu_certo  = 101
                                vai_dar_certo = 101
                                acertou()
                                fase = False
                            else:
                                errou(respostas,dic_pergunta[certa],tamanho_fonte,login,senha)



                        if retangulo_pergunta3.collidepoint(event.pos):
                            if dic_pergunta[3] == dic_pergunta[certa]:
                                respostas +=1
                                sera_que_deu_certo  = 101
                                vai_dar_certo = 101
                                acertou()
                                fase = False
                            else:
                                errou(respostas,dic_pergunta[certa],tamanho_fonte,login,senha)



                        if retangulo_pergunta4.collidepoint(event.pos):
                            if dic_pergunta[4] == dic_pergunta[certa]:
                                respostas +=1
                                sera_que_deu_certo  = 101
                                vai_dar_certo = 101
                                acertou()
                                fase = False
                            else:
                                errou(respostas,dic_pergunta[certa],tamanho_fonte,login,senha)


                        if plateia.collidepoint(event.pos) and dica_plateia == True:
                            sera_que_deu_certo = random.randint(1,100)
                            dica_plateia = False
                        

                        if universitario.collidepoint(event.pos) and dica_univ == True:
                            vai_dar_certo = random.randint(1,100)
                            dica_univ = False

                        if cartas.collidepoint(event.pos) and dica_cartas==True:
                            dica_cartas  = False
                            remocao = random.randint(1,3)
                            while len(tirei_perg)<remocao:
                                pergunta_tirada = random.randint(1,4)
                                if pergunta_tirada != certa and pergunta_tirada not in tirei_perg:
                                    tirei_perg.append(pergunta_tirada)


                        if pula_questao.collidepoint(event.pos) and pulei == True:
                            num_pulos -=1
                            if num_pulos == 0:
                                pulei = False
                            fase = False
                        
                        if sair_perguntas.collidepoint(event.pos):
                            quer_jogar = False
                            perdeu(respostas,login,senha)
                            return
                
                pygame.draw.rect(screen,branco,sair_perguntas)
                pygame.draw.rect(screen, (14,14,14,0), retangulo_pergunta1)
                pygame.draw.rect(screen, (14,14,200,0), retangulo_pergunta2)
                pygame.draw.rect(screen, (14,200,14,0), retangulo_pergunta3)
                pygame.draw.rect(screen, (200,14,14,0), retangulo_pergunta4)
                pygame.draw.rect(screen,(200,200,200),plateia)
                pygame.draw.rect(screen,(100,100,100),universitario)
                pygame.draw.rect(screen,(00,00,00),cartas)
                pygame.draw.rect(screen,(20,20,29),pula_questao)
                screen.blit(fundo_perguntas, (0, 0))
                screen.blit(pontos_saiu,(971,583))
                screen.blit(pontos_errou,(812,583))
                screen.blit(pontos_acertou,(1129,583))
                if tirei_perg.count(1) == 0:    
                    screen.blit(texto_alternativa_1,(160,230))
                if tirei_perg.count(2) == 0:    
                    screen.blit(texto_alternativa_2,(160,373))
                if tirei_perg.count(3) == 0:    
                    screen.blit(texto_alternativa_3,(160,500))
                if tirei_perg.count(4) == 0:    
                    screen.blit(texto_alternativa_4,(160,620))
                if len(perguntas)>1:
                    for i in range(len(perguntas)):
                        linha_pergunta = fonte_pergunta.render(perguntas[i],True,branco)
                        screen.blit(linha_pergunta,(0,coord))
                        coord += tamanho_fonte_pergunta
                else:
                    linha_pergunta = fonte_pergunta.render(perguntas[0],True,branco)
                    if linha_pergunta.get_width()>950:
                        tamanho_fonte_pergunta -= 5
                        fonte_alternativa = pygame.font.Font(None, tamanho_fonte_pergunta)
                        fonte_pergunta = pygame.font.Font(None,tamanho_fonte_pergunta)
                    screen.blit(linha_pergunta,(0,coord))
                if sera_que_deu_certo <= 60:
                    if certa == 1:
                        pygame.draw.circle(screen,"green",(113,263),40)
                    if certa == 2:
                        pygame.draw.circle(screen,"green",(113,394),40)
                    if certa == 3:
                        pygame.draw.circle(screen,"green",(113,524),40)
                    if certa == 4:
                        pygame.draw.circle(screen,"green",(113,654),40)
                elif sera_que_deu_certo<=100:
                    if certa == 1:
                        pygame.draw.circle(screen,"green",(113,654),40)
                    if certa == 2:
                        pygame.draw.circle(screen,"green",(113,263),40)
                    if certa == 3:
                        pygame.draw.circle(screen,"green",(113,394),40)
                    if certa == 4:
                        pygame.draw.circle(screen,"green",(113,524),40)
                if vai_dar_certo <= 80:
                    if certa == 1:
                        pygame.draw.circle(screen,"green",(113,263),40)
                    if certa == 2:
                        pygame.draw.circle(screen,"green",(113,394),40)
                    if certa == 3:
                        pygame.draw.circle(screen,"green",(113,524),40)
                    if certa == 4:
                        pygame.draw.circle(screen,"green",(113,654),40)
                elif vai_dar_certo<=100:
                    if certa == 1:
                        pygame.draw.circle(screen,"green",(113,654),40)
                    if certa == 2:
                        pygame.draw.circle(screen,"green",(113,263),40)
                    if certa == 3:
                        pygame.draw.circle(screen,"green",(113,394),40)
                    if certa == 4:
                        pygame.draw.circle(screen,"green",(113,524),40)
                if dica_cartas == False:
                    pygame.draw.line(screen,"red", (1133,270) ,(1213,360), 10)
                    pygame.draw.line(screen,"red",(1133,360) ,(1213,270), 10)
                if dica_plateia == False:
                    pygame.draw.line(screen,"red",(817,270) ,(897,360) ,10)
                    pygame.draw.line(screen,"red", (817,360),(897,270), 10)
                if dica_univ == False:
                    pygame.draw.line(screen,"red",(974,270) ,(1054,360) ,10)
                    pygame.draw.line(screen,"red", (974,360),(1054,270), 10)
                
                if num_pulos <=2:
                    pygame.draw.line(screen,"red",(817,420) ,(897,510) ,10)
                    pygame.draw.line(screen,"red", (817,510),(897,420), 10)
                    if num_pulos <=1:
                        pygame.draw.line(screen,"red",(974,420) ,(1054,510) ,10)
                        pygame.draw.line(screen,"red", (974,510),(1054,420), 10)
                        if num_pulos ==0:
                            pygame.draw.line(screen,"red", (1133,420) ,(1213,510), 10)
                            pygame.draw.line(screen,"red",(1133,510) ,(1213,420), 10)
                
                pygame.display.flip()
                
                clock.tick(60)
    ganhou(login,senha)


if __name__ == '__main__':
    pygame.init()
    perguntas('jojo','1234')
    pygame.quit()