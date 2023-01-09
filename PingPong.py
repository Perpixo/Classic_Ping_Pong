import pygame 
import time
import os

from pygame.constants import KEYUP

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 800
dis_height = 600
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('PingPong Autoral')

font_style = pygame.font.SysFont("bahnschrift", 25)

#pagina final
def mensagem_Restart(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 2])
def mensagem_Quit(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 1.8])


#condição de perda de jogo
def gameLoop():
    game_over = False
    game_close = False

    #bolinha

    x4 = 395
    y4 = 300

    y4_change = 2
    x4_change = 5

    #linha do campo

    x3 = 400
    y3 = 50

    #posição do jogador 1 
    x1 = 700
    y1 = 275
        
    y1_change = 0

    #posição do jogador 2
    x2 = 100
    y2 = 275
        
    y2_change = 0
    
    while not game_over:

        while game_close == True:
            mensagem_Restart("Restart: R", white)
            mensagem_Quit("Quit: Q", white)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()


        for event in pygame.event.get():
            #track de mouse no dysplay do jogo em print para ficar mais facil de ver
            #opção de sair do jogo
            if event.type==pygame.QUIT:
                game_over=True
            #movimento do jogador 1 ao pressionar tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    y1_change = -10
                elif event.key == pygame.K_RIGHT:
                    y1_change = 10
                #movimento do jogador 2 //
                elif event.key == pygame.K_a:
                    y2_change = -10
                elif event.key == pygame.K_d:
                    y2_change = 10
                    
            #movimento do jogador 1 ao soltar tecla
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    y1_change = 0
                #movimento do jogador 2 //
                elif event.key == pygame.K_a:
                    y2_change = -0
                elif event.key == pygame.K_d:
                    y2_change = 0


        y1 += y1_change
        y2 += y2_change

        #cor do display
        dis.fill(black)
        #cor e tamanho

        esquerdo_pad = pygame.Rect (x1, y1, 10, 80)
        direito_pad = pygame.Rect (x2, y2, 10, 80)

        pads = [esquerdo_pad, direito_pad]


        for pad in pads:
            pygame.draw.rect(dis, white, pad)
    
        #bolinha

        bolinha = pygame.Rect (x4, y4, 10, 10)

        #bolinha nos pads
        if bolinha.collidelist(pads) >= 0:
            x4_change = -x4_change 
            -y4_change
            tocou = True

            if tocou == True:
                x4_change + 1
                print(x4_change)

        #se sair a bolinha na largura
        if x4 >= dis_width or x4 < 0:
            print("saiu")
            game_close = True

        #movimento da bolinha
        x4 += x4_change
        y4 += y4_change

        #quicando nas paredes
        if y4 >= 600:
            y4_change = -y4_change

        elif y4 < 0:
            y4_change = -y4_change

        #colisão dos pads
        if y1 >= 500 or y1 < 10:
            y1 -= y1_change
    
        if y2 >= 500 or y2 < 10:
            y2 -= y2_change

        pygame.draw.rect(dis, white, [x3, y3, 1, 500])
        pygame.draw.rect(dis, white, bolinha)
        pygame.display.update()
        
        clock = pygame.time.Clock()
            
        clock.tick(60)

    pygame.quit()
    quit()
gameLoop()