def computador_escolhe_jogada(n, m):
    cpuRetira = 1

    while cpuRetira != m:
        if (n - cpuRetira) % (m+1) == 0:
            return cpuRetira

        else:
            cpuRetira += 1

    return cpuRetira


def usuario_escolhe_jogada(n, m):
    jogadaValida = False

    while not jogadaValida:
        jogadorRetira = int(input('Quantas peças você vai tirar? \n'))
        if jogadorRetira > m or jogadorRetira < 1:
            
            print('Oops! Jogada inválida! Tente de novo.\n')


        else:
            jogadaValida = True

    return jogadorRetira


def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
       
        print('Rodada ', numeroRodada, '\n')

        partida()
        numeroRodada += 1

    print('Placar: Você 0 X 3 Computador \n')


def partida():
    n = 0
    m = 0
    while n <= m:
       
        n = int(input('Quantas peças? \n'))

        m = int(input('Limite de peças por jogada? \n'))

    vezDoPC = False

    if n % (m+1) == 0:
        print('Você começa!\n')

    else:

        print('Computador começa! \n')
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            cpuRetira = computador_escolhe_jogada(n, m)
            n = n - cpuRetira
            if cpuRetira == 1:

                print('O computador tirou uma peça \n')
            else:

                print('Agora restam  ', cpuRetira, ' peças no tabuleiro.\n')

            vezDoPC = False
        else:
            jogadorRetira = usuario_escolhe_jogada(n, m)
            n = n - jogadorRetira
            if jogadorRetira == 1:

                print('Você tirou uma peça \n')
            else:

                print('Você tirou', jogadorRetira, 'peças \n')
            vezDoPC = True
        if n == 1:
            print('Resta apenas uma peça no tabuleiro. \n')

        else:
            if n != 0:
                print('Restam,', n, 'peças no tabuleiro. \n')


    print('Fim do jogo! O computador ganhou!')

print('Bem-vindo ao jogo do NIM! Escolha:\n')


print('1 - para jogar uma partida isolada\n')

tipoDePartida = int(input('2 - para jogar um campeonato \n'))

if tipoDePartida == 2:

    print('Voce escolheu um campeonato!\n')

    campeonato()
else:
    if tipoDePartida == 1:

        partida()