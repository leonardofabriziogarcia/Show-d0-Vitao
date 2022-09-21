def tela_comeco(login,senha):
    import pygame
    from tela_perguntas import perguntas
    from tela_placar import placar
    from SQL import PontosSQL


    pontos = PontosSQL(login)[0]
    pontos = f'{pontos}'
    fonte= pygame.font.Font(None, 60)
    texto  = fonte.render(pontos,True,(0,0,0))
    fundo_comeco = pygame.image.load(r'tela_começo_SDV.jpg')
    screen = pygame.display.set_mode([fundo_comeco.get_width(), fundo_comeco.get_height()])
    tela_de_comeco = True
    clock = pygame.time.Clock()
    retangulo_iniciar = pygame.Rect(72,175,514,168)
    retangulo_placar = pygame.Rect(72,440,514,168)
    while tela_de_comeco == True:
        for event in pygame.event.get():
    
        
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retangulo_iniciar.collidepoint(event.pos):
                    tela_de_comeco = False
                    perguntas(login,senha)
                    return
                if retangulo_placar.collidepoint(event.pos):
                    tela_de_comeco = False
                    placar()
                    tela_de_comeco = True
        
        pygame.draw.rect(screen,(100,0,0),retangulo_iniciar)
        pygame.draw.rect(screen,(100,0,0),retangulo_placar)
        screen.blit(fundo_comeco,(0,0))
        screen.blit(texto,(860,50))
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    import pygame
    pygame.init()
    tela_comeco(1,1)
    pygame.quit()