def acertou():
    import pygame
    acertaste = True
    fundo_acertou = pygame.image.load(r'tela_resp_certa_SDV.jpg')
    screen = pygame.display.set_mode([fundo_acertou.get_width(), fundo_acertou.get_height()])
    rect_proximo = pygame.Rect(475,480,325,100)
    clock = pygame.time.Clock()
    while acertaste == True:
        for event in pygame.event.get():
    
        
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_proximo.collidepoint(event.pos):
                    acertaste = False
                    return


    
        pygame.draw.rect(screen,(255,255,255),rect_proximo)
        screen.blit(fundo_acertou,(0,0))
        pygame.display.flip()
        clock.tick(60)
