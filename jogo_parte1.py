import pygame
from random import randint
pygame.init()

timer = 0
tempo_segundo = 0

#limite da esquerda eixo X -270
#limite da direita eixo X 200

x = -47 #posição carro vermelho ( principal )
y = 45 #posição carro vermelho ( principal )

policia2_x = -47
policia2_y = 650

pos_x = -235
pos_y = 885

ambulancia_x = 160
ambulancia_y = 885

velocidade = 15
velocidade_outros = 20

fundo = pygame.image.load('pista_pronta3.png')
carro = pygame.image.load('carro_pronto.png')
policia = pygame.image.load('policia.png')
ambulancia = pygame.image.load('ambulancia.png')
policia2 = pygame.image.load('policia2.png')

font = pygame.font.SysFont('arial black', 30)
#Definção de font, tamanho font, e coloração, e posicionemtno do texto
texto = font.render("Tempo: ", True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)

#perdeu = pygame.font.SysFont('arial black', 50)
#game_over = font.render("BATEU CUZAO", True (255, 255, 255), (0, 0, 0))
#pos_texto = texto.get_rect()
#pos_texto.center = (65, 50)


janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

#Nos if's abaixo onde possui "and" é o limitador onde o carro pode percorrer
#tanto na esquerda, quanto na direita, as limitações seria -260 pixels a esquerda
# e 190 pixels a direita
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT] and x <= 190:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= -260:
        x -= velocidade
    if comandos[pygame.K_w]:
        y -= velocidade
    if comandos[pygame.K_s]:
        y += velocidade
    if comandos[pygame.K_d] and x <= 190:
        x += velocidade
    if comandos[pygame.K_a] and x >= -260:
        x -= velocidade

    #detecta colisao
    if ((x + 80 > ambulancia_x and y + 60 > ambulancia_y)):
        y = 1200
        p = font.render("Tempo: " +str (tempo_segundo), True, (255, 255, 255), (0, 0, 0))

    if ((x - 80 < pos_x and y + 60 > pos_y)):
        y = 1200
    #colisão central
    if (x + 80 > ambulancia_x and y +180 > ambulancia_y) or (x - 80 < pos_x and y + 60 > pos_y):
         y = 1200


    if (pos_y <= -230) :
        pos_y = randint(800, 1000) #posição randomica carro preto

    if (ambulancia_y <= -230):
        ambulancia_y = randint(1350, 3000) #posição randomica ambulancia

    if (policia2_y <= -230):
        policia2_y = randint(800, 3000)

    if (timer < 20):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: " +str (tempo_segundo), True, (255, 255, 255), (0, 0, 0))
       #variavel texto acima, converte o tempo_segundo para Str e passa os parametros de posicionamento... cor etc..
       #lembrando que isso está dentro do While acima na linha 39
        timer = 0
    pos_y -= velocidade_outros +2 #carro preto
    ambulancia_y -= velocidade_outros +10 #ambulancia
    policia2_y -= velocidade_outros +7 # carro preto meio (policia2)

    janela.blit(fundo, (0, 0))
    janela.blit(carro, (x, y))
    janela.blit(policia, (pos_x, pos_y))
    janela.blit(policia2, (policia2_x, policia2_y))
    janela.blit(ambulancia, (ambulancia_x, ambulancia_y))
    janela.blit(texto, pos_texto)
    pygame.display.update()

pygame.quit()