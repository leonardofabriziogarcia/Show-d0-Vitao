def tela_login():
    import pygame
    from tela_comeco import tela_comeco
    from SQL import LoginSQL
    

    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    

    screen = pygame.display.set_mode([1280, 720])
    fundo_login = pygame.image.load(r'Tela_login_SDV.jpg')
    

    base_font = pygame.font.Font(None, 100)
    login = ''
    senha = ''
    
    retangulo_login = pygame.Rect(47, 150, 606, 93)
    retangulo_senha = pygame.Rect(47, 352, 625, 93)
    retangulo_comecar = pygame.Rect(42,562,290,83)
    retangulo_cadastrar = pygame.Rect(385,562,290,83)
    
    color_active = pygame.Color('green')
    color_passive = pygame.Color('cyan')
    
    active_login, active_senha = False,False
    
    login_rodando = True
    while login_rodando:
        for event in pygame.event.get():
    
        
            if event.type == pygame.QUIT:
                
                pygame.quit()
                return
                
                

            #LOGIN 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retangulo_login.collidepoint(event.pos):
                    active_login = True
                else:
                    active_login = False
    
            if event.type == pygame.KEYDOWN and active_login == True :
    
            
                if event.key == pygame.K_BACKSPACE:
                    login = login[:-1]
    
                
                else:
                    if  event.key != pygame.K_RETURN and len(login)<12:
                        login += event.unicode

                    if event.key == pygame.K_RETURN:
                        active_login = False
                        

            
            #SENHA
            if event.type == pygame.MOUSEBUTTONDOWN :
                if  retangulo_senha.collidepoint(event.pos) :
                    active_senha = True
                else:
                    active_senha = False
    
            if event.type == pygame.KEYDOWN and active_senha == True :
    
                if event.key == pygame.K_BACKSPACE :
    
                    
                    senha = senha[:-1]
    
                
                else:
                    if event.key != pygame.K_RETURN and len(senha)<24:
                        senha += event.unicode
                    else:
                        active_senha = False
            
            if event.type == pygame.MOUSEBUTTONDOWN :
                if retangulo_comecar.collidepoint(event.pos):
                    foi = LoginSQL(login,senha,False)
                    if foi == True:
                        login_rodando = False
                        tela_comeco(login,senha)
                        return
                    else:
                        login = ''
                        senha = ''
            
            if event.type == pygame.MOUSEBUTTONDOWN :
                if retangulo_cadastrar.collidepoint(event.pos):
                    foi = LoginSQL(login,senha,True)
                    if foi == True:
                        login_rodando = False
                        tela_comeco(login,senha)
                        return
                    else:
                        login = ''
                        senha = ''


            
        
    
       

        screen.blit(fundo_login,(0,0))  
        #desenha retangulo para colisao do  login e o texto dele
        pygame.draw.rect(screen, color_passive, retangulo_login)
    
        texto_login = base_font.render(login, True, (0, 0, 0))
        
        

        
        

        
        #desenha retangulo para colisao da  senha e o texto dela
        pygame.draw.rect(screen, color_active, retangulo_senha)
    
        texto_senha= base_font.render('*'*len(senha), True, (0, 0, 0))
        
        

        pygame.draw.rect(screen, color_passive,retangulo_cadastrar)
        pygame.draw.rect(screen, color_passive,retangulo_comecar)
        screen.blit(fundo_login,(0,0))
        screen.blit(texto_senha, (47,370))
        screen.blit(texto_login, (45,168))
        
        
        pygame.display.flip()
        
        
        clock.tick(60)
if __name__ == "__main__":
    tela_login()