def placar():
    import pygame
    from SQL import PlacarSQL
    p = True
    lista_nomes,lista_pontos=PlacarSQL()
    fundo_placar = pygame.image.load(r'tela_placar_SDV.jpg')
    screen = pygame.display.set_mode([fundo_placar.get_width(), fundo_placar.get_height()])
    clock = pygame.time.Clock()
    sair_placar = pygame.Rect(1180,0,100,100)
    fonte= pygame.font.Font(None, 60)
    
    x_nome = 320
    x_ponto = 670
    nome_1 = fonte.render(lista_nomes[0],True,(0,0,0))
    nome_2 = fonte.render(lista_nomes[1],True,(0,0,0))
    nome_3 = fonte.render(lista_nomes[2],True,(0,0,0))
    nome_4 = fonte.render(lista_nomes[3],True,(0,0,0))
    nome_5 = fonte.render(lista_nomes[4],True,(0,0,0))
    ponto_1 = fonte.render(f'{lista_pontos[0]}',True,(0,0,0))
    ponto_2 = fonte.render(f'{lista_pontos[1]}',True,(0,0,0))
    ponto_3 = fonte.render(f'{lista_pontos[2]}',True,(0,0,0))
    ponto_4 = fonte.render(f'{lista_pontos[3]}',True,(0,0,0))
    ponto_5 = fonte.render(f'{lista_pontos[4]}',True,(0,0,0))

    while p == True:
        for event in pygame.event.get():
    
        
            if event.type == pygame.QUIT:
                pygame.quit()
                p = False
                return


            if event.type == pygame.MOUSEBUTTONDOWN:
                if sair_placar.collidepoint(event.pos):
                    p = False
                    return
        
        
        pygame.draw.rect(screen,(0,0,0),sair_placar)
        screen.blit(fundo_placar,(0,0))
        screen.blit(nome_1,(x_nome,240))
        screen.blit(nome_2,(x_nome,315))
        screen.blit(nome_3,(x_nome,385))
        screen.blit(nome_4,(x_nome,460))
        screen.blit(nome_5,(x_nome,535))
        screen.blit(ponto_1,(x_ponto,240))
        screen.blit(ponto_2,(x_ponto,315))
        screen.blit(ponto_3,(x_ponto,385))
        screen.blit(ponto_4,(x_ponto,460))
        screen.blit(ponto_5,(x_ponto,535))
        pygame.display.flip()  
        clock.tick(60)
        
if __name__ == '__main__':
    import pygame
    pygame.init()
    placar()
    pygame.quit()