import random 

print ('''Você está lutando contra um monstro, um lobo mutante! ''')

vida1 = int (350)
ataque1 = int (130)
defesa1 = int (30)
pocoesvida = int (3)
vida2 = int (825)
ataque2 = int (70)
defesa2 = int (90)
trigger1 = trigger2 = int (0)
sorteador = random.randint (1, 20)
sorteador2 = random.randint (1, 150)
sorteador3 = random.randint (1, 1500)

while vida1 > 0:

    if vida2 <= 175 and vida2 > 0 and trigger1 == 0:
        ataque2 = 95
        print (f"O lobo ficou enfurecido! Seu ataque aumentou para {ataque2}!! ")
        trigger1 = 1
    
    if vida2 <= 150 and vida2 > 0 and trigger2 == 0:
        vida2 += 150
        defesa2 += 25
        print (f'''O lobo concentra suas energias, recuperando sua vida e aumentando sua defesa!
Sua vida retorna para {vida2} e sua defesa aumenta em 25, indo para {defesa2}!!''')
        trigger2 = 1
        

    if vida1 <= 75 and vida1 > 0:
        print (f'Você está quase apagando!! Tome uma poção, depressa! ')

    choice = int (input ('''1. Executar ataque
2. Usar poção
3. Ver seu status
4. Ver status do oponente 
5. Info dos ataques e itens
'''))

    if choice == 1:
        qualataque = int (input ('''Qual ataque deseja utilizar?
1. Golpe Frontal
2. Golpe Carregado
3. Rompe-Cascos
4. Retornar para as escolhas
'''))
        if qualataque == 1:
            if sorteador == 1:
                dano2 = ataque1 * 2 - defesa2 #170
                vida2 -= dano2
                print (f'Você acertou um golpe crítico, causando o dobro de dano, tirando {dano2} de vida do oponente!')
            else:
                vida2 -= ataque1 - defesa2 #40
                print (f"Você ataca o monstro e causa {ataque1 - defesa2} de dano a ele! ")
            vida1 -= ataque2 - defesa1
            if vida2 < 0:
                vida2 = 0
            if vida1 < 0:
                vida1 = 0
            print (f"Seu oponente te ataca de volta, causando {ataque2 - defesa1} de dano! ")
            print (f"Sua vida: {vida1} ")
            print (f"Vida do openente: {vida2} ")
        
        elif qualataque == 2:
            sorteador = random.randint (1, 20)
            if sorteador not in (2, 3, 4, 5, 6, 7):
                if sorteador == 1:
                    dano2 = (ataque1 - defesa2) * 3 #120
                    dano3 = dano2 * 3 - defesa2 #270
                    vida2 -= dano3
                    print (f'UAU! Você desferiu um golpe crítico, causando um dano absurdo! Reduziu a vida do oponente em {dano3}!')
                else:
                    dano2 = (ataque1 - defesa2) * 3 #120
                    vida2 -= dano2
                    print (f"Você desfere um golpe poderoso, tão forte até quanto três golpes normais! Causou {dano2} de dano!")
            else:
                print ('Você perdeu o equilíbrio e acabou errando o ataque!')
            if vida2 < 0:
                vida2 = 0
            if vida1 < 0:
                vida1 = 0
            vida1 -= ataque2 + 10
            print (f"O golpe te causa uma exaustão, permitindo seu inimigo atacar seu ponto fraco! Ele reduz sua vida em {ataque2 + 10}! ")
            print (f"Sua vida: {vida1} ")
            print (f"Vida do openente: {vida2} ")

        elif qualataque == 3:
            dano = 20
            defesa2 -= 15
            vida2 -= dano
            vida1 -= ataque2 - defesa1
            if vida2 < 0:
                vida2 = 0
            if vida1 < 0:
                vida1 = 0
            print (f'''Você se concentra e faz um ataque para quebrar a pele enrigecida do lobo mutante.
Você quebra a defesa dele em 15, e causa {dano} pontos de dano!
O lobo revida, causando {ataque2 - defesa1} de dano! ''')
            print (f"Sua vida: {vida1} ")
            print (f"Vida do openente: {vida2} ")
            if defesa2 < 0:
                defesa2 = 0
            print (f'Defesa do opoente: {defesa2} ')

    elif choice == 2:
        confirmapocao = int (input (f'''Deseja utilizar uma poção de vida?
Você possui {pocoesvida} deste item.
1. Utilizar poção
2. Retornar para as escolhas
'''))
        if confirmapocao == 1:

            if pocoesvida <= 0:
                print ("Você não tem mais nenhuma poção!!")
                pocoesvida = 0
            else:
                vidaoriginal = vida1
                if vidaoriginal == 350:
                    print ("Você já está com sua vida máxima, portanto não usou a poção!")
                else:
                    pocoesvida -= 1
                    vida1 += 120
                    if vida1 >= 350:
                        vida1 = 350
                    if vida1 < 350:
                        print (f'Sua vida retornou para {vida1}! ')
                    else:
                        print ("Você retornou para sua vida máxima!")
                    if pocoesvida == 0:
                        print ("Essa foi sua última poção!")


    elif choice == 3:
        print(f'''Você é um cavaleiro, com uma espada e uma armadura leve.
Ataque: 130
Vida máxima = 350
Vida atual = {vida1}
Defesa = 30
Poções restantes: {pocoesvida}
''')

    elif choice == 4:
        print(f'''Seu oponente é um lobo mutante, totalmente enraivecido!
Ataque: {ataque2}
Vida máxima = 825
Vida atual = {vida2}
Defesa = {defesa2}
Drops = ????
''')

    elif choice == 5:
        print ('''Golpe Frontal:
Um golpe comum, causando seu dano natural, com a redução da defesa do oponente.
5% de chance de dano crítico.

Golpe Carregado:
Um corte poderoso, que causa até o triplo de dano do golpe anterior. Deixa você um pouco desiquilibrado, 
fazendo você tomar um pouco de dano a mais do oponente.
Tem 30% de chance de errar o golpe.
5% de chance de dano crítico.

Rompe-Cascos: 
Um golpe concentrado para quebrar a defesa do oponente, entretanto causando dano reduzido.

Poção de Vida:
Um líquido viscoso e avermelhado, provavelmente feito de frutas ou flores mágicas. Recupera 120 pontos de vida.
''')

    if vida2 <= 0:

        if vida1 <= 0:
            vida1 = 1 #Para você não morrer junto com o oponente
        print ("Parabéns, você venceu o lobo!!")
        print ('Você recebeu 150 de ouro e o item "Garra de Lobo"!')
        if sorteador2 == 1:
            print ("Você ganhou um item ULTRA RARO!")
            print ('"Pato de Borracha" adicionado ao seu inventário')
        elif sorteador3 == 777:
            print ("TA PORA MENÓ")
            print ("Você ganhou um PATO DE RATOKKKKKKKKKKKKKKKKKK")
        break

if vida1 <= 0:
    vida1 = 0
    print ("O lobo te derrota, seus olhos vão lentamente se apagando...")

