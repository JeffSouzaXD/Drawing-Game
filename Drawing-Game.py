from turtle import Turtle
t = Turtle()
t.speed(1)
print('----- Bem Vindo ao jogo dos desenhos! -----')

def obter_distancia():
       resposta = int(input('Deseja se movimentar quantos pixels para frente? '))
       return resposta

def rotacionar_turtle(turtle):
    movimentar_para_os_lados = input('Deseja rotacionar para direita(D) ou para esquerda(E)? ')
    if movimentar_para_os_lados == 'D' or movimentar_para_os_lados == 'd':
            rotacionar_turtle(turtle)
    elif movimentar_para_os_lados == 'E' or movimentar_para_os_lados == 'e':
            rotacionar_turtle(turtle)
    else: print('Digite um valor valido')

def rotacionar_para_direita():
       angulo = int(input('Deseja se movimentar quantos pixels para direita? '))
       t.right(angulo)

def rotacionar_para_esquerda():
      angulo = int(input('Deseja se movimentar quantos pixels para esquerda? '))
      t.left(angulo)
      
while True:
    direcao = input('Deseja ir para frente(F) ou para trás(T)? ')
    if direcao == 'F' or direcao == 'f':
            direcao = obter_distancia()
            rotacionar_turtle(t)
            t.forward(direcao)
    elif direcao == 'T' or direcao == 't':
            direcao = int(input('Deseja se movimentar quantos pixels para trás? '))
            rotacionar_turtle(t)
            t.backward(direcao)
    else: print('Digite um valor valido')
    continuar = input('Deseja continuar o jogo? (S/N) ')
    if continuar == 'S' or continuar == 's':
        continue
    else: break
print('Obrigado por jogar!')