def perdeu(respostas,login,senha):
    import pygame
    from tela_comeco import tela_comeco
    from SQL import SomarPontosSQL

    perdeste = True
    fonte= pygame.font.Font(None, 60)
    fundo_perdeu = pygame.image.load(r'tela_perdeste_SDV.jpg')
    screen = pygame.display.set_mode([fundo_perdeu.get_width(), fundo_perdeu.get_height()])
    rect_proximo = pygame.Rect(475,480,325,100)
    clock = pygame.time.Clock()
    pontuacao = ['0','500','1000','2000','3000','5000','10000','15000','20000','30000','50000','100000','200000','300000','400000','500000','1000000']
    SomarPontosSQL(login,pontuacao[respostas])
    texto  = fonte.render(pontuacao[respostas],True,(0,0,0))
    while perdeste == True:
        for event in pygame.event.get():
    
        
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_proximo.collidepoint(event.pos):
                    tela_comeco(login,senha)
                    perdeste = False
                    return


        pygame.draw.rect(screen,(255,255,255),rect_proximo)
        screen.blit(fundo_perdeu,(0,0))
        screen.blit(texto,(510,348))
        pygame.display.flip()
        clock.tick(60)

            
