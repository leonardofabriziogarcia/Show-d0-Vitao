from tela_perdeu import perdeu


def errou(resposta,alt_certa,tamanho_fonte,login,senha):
    import pygame
    erraste = True
    fundo_erro = pygame.image.load(r'tela_resp_errada_SDV.jpg')
    screen = pygame.display.set_mode([fundo_erro.get_width(), fundo_erro.get_height()])
    rect_proximo = pygame.Rect(475,530,325,100)
    base_font = pygame.font.Font(None, tamanho_fonte)
    texto = base_font.render(alt_certa,True,(0,0,0))
    if resposta-2>=0:
        resposta = resposta-2
    else:
        resposta = 0
    clock = pygame.time.Clock()
    while erraste == True:
        for event in pygame.event.get():
    
        
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_proximo.collidepoint(event.pos):
                    erraste = False
                    perdeu(resposta,login,senha)
                    return


        pygame.draw.rect(screen,(255,255,255),rect_proximo)
        screen.blit(fundo_erro,(0,0))
        screen.blit(texto,(300,370))
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    import pygame
    pygame.init()
    errou(1,'1',60)
    pygame.quit()