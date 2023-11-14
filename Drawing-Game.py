from turtle import Turtle
t = Turtle()
t.speed(1)
print('----- Bem Vindo ao jogo dos desenhos! -----')
while True:
    jogada1 = input('Deseja ir para frente(F) ou para trás(T)? ')
    if jogada1 == 'F' or jogada1 == 'f':
            frente = int(input('Deseja se movimentar quantos pixels para frente? '))
            t.forward(frente)
    elif jogada1 == 'T' or jogada1 == 't':
            tras = int(input('Deseja se movimentar quantos pixels para trás? '))
            t.backward(tras)
    else: print('Digite um valor valido')
    jogada2 = input('Deseja rotacionar para direita(D) ou para esquerda(E)? ')
    if jogada2 == 'D' or jogada2 == 'd':
            direita = int(input('Deseja se movimentar quantos pixels para direita? '))
            t.right(direita)
    elif jogada2 == 'E' or jogada2 == 'e':
            esquerda = int(input('Deseja se movimentar quantos pixels para esquerda? '))
            t.left(esquerda)
    else: print('Digite um valor valido')
    continuar = input('Deseja continuar o jogo? (S/N) ')
    if continuar == 'S' or continuar == 's':
        continue
    else: break
print('Obrigado por jogar!')