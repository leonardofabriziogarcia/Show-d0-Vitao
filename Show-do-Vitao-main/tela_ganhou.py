
def ganhou(login,senha):
    import pygame
    from tela_comeco import tela_comeco
    from SQL import SomarPontosSQL

    ganhaste = True
    fundo_ganhou = pygame.image.load(r'tela_ganhaste_SDV.jpg')
    screen = pygame.display.set_mode([fundo_ganhou.get_width(), fundo_ganhou.get_height()])
    rect_proximo = pygame.Rect(475,480,325,100)
    clock = pygame.time.Clock()
    SomarPontosSQL(login,1000000)
    while ganhaste == True:
        for event in pygame.event.get():
    
        
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_proximo.collidepoint(event.pos):
                    tela_comeco(login,senha)
                    ganhaste = False
                    return


    
        pygame.draw.rect(screen,(255,255,255),rect_proximo)
        screen.blit(fundo_ganhou,(0,0))
        pygame.display.flip()
        clock.tick(60)
