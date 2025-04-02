import random
from time import sleep

# Atributos iniciais
forca = 0
constituicao = 0
destreza = 0
inteligencia = 0
forc_de_vont = 0
carisma = 0
percepcao = 0

# Nome do jogador
nome = input("Olá, guerreiro... Digite o seu nome: ")

print(f"\nOlá, {nome}, seja bem-vindo a Legenda City!\n")
print("A cidade precisa de um herói para enfrentar os perigos que assolam a região...\n")

# Descrições das classes
classes = {
    1: ("Guerreiro", "Especialistas em combate físico, com habilidades com armas, armaduras e táticas de batalha.", 8, 8, 5, 3, 4, 3, 4),
    2: ("Ladrão", "Especialistas em furtividade e habilidades de trapaceiros, que podem desarmar armadilhas, roubar itens valiosos e se mover silenciosamente.", 4, 5, 9, 5, 3, 5, 7),
    3: ("Paladino", "Cavaleiros sagrados e defensores da justiça, que têm a capacidade de curar, lançar magias e são conhecidos por sua devoção e honra.", 7, 7, 5, 5, 8, 6, 5),
    4: ("Mago", "Usuários de magia e feitiçaria, que podem lançar feitiços de cura, bolas de fogo, entre outros.", 2, 4, 5, 10, 8, 4, 5),
    5: ("Clérigo", "Sacerdotes ou servos de deuses e têm poderes divinos, que podem curar ferimentos, banir criaturas malignas e lançar magias de proteção.", 3, 6, 4, 7, 9, 6, 5),
    6: ("Xamã", "Místicos ligados aos espíritos da natureza, que usam magias de cura, transformação e podem se comunicar com seres sobrenaturais.", 3, 5, 5, 8, 8, 4, 7),
    7: ("Druida", "Têm uma conexão especial com a natureza e podem se transformar em animais, invocar criaturas naturais e controlar elementos como o vento e a água.", 4, 5, 6, 8, 7, 5, 6),
    8: ("Bardo", "Artistas e contadores de histórias, que usam sua música e palavras para inspirar aliados, lançar feitiços e manipular emoções.", 3, 5, 6, 6, 5, 10, 5),
    9: ("Ranger", "Especialistas em sobrevivência na natureza, que são arqueiros habilidosos, rastreadores e têm uma afinidade com animais.", 5, 6, 8, 4, 4, 5, 9),
}

# Função para exibir classes e suas descrições
def exibir_classes():
    for key, value in classes.items():
        print(f"{key} - {value[0]}: {value[1]}")

# Escolha da classe
while True:
    print("\nEscolha sua classe:")
    exibir_classes()
    
    escolha_classe = int(input("\nQual é sua escolha?: "))

    if escolha_classe in classes:
        classe, descricao, forca, constituicao, destreza, inteligencia, forc_de_vont, carisma, percepcao = classes[escolha_classe]
        print(f"\nVocê escolheu a classe '{classe}': {descricao}")
        break
    else:
        print("\nOpção inválida, tente novamente...\n")

# Definições iniciais
vida_maxima = 30  # Vida cheia
vida_jogador = vida_maxima + constituicao  # Vida do jogador baseada na constituição
nivel = 1  # Nível inicial
experiencia = 0  # Experiência inicial
poções = 3  # Poções de cura

# História inicial
print(f"\nBem-vindo ao início de sua jornada, {nome}.\n")
print("Em Legenda City, a magia e os mistérios reinam. Sombras sinistras rondam as ruas, e a paz foi perdida.")
print("\nAgora, como o novo herói, você terá que ouvir a lenda...\n")

sleep(2)
print("\nHá milênios, a terra foi governada por dragões e seres mágicos imortais. Eles criaram os primeiros reinos e mantiveram o equilíbrio do mundo. No entanto, uma força sombria começou a se espalhar pelas terras, um poder desconhecido que corrompeu tudo o que tocava. Esse poder, conhecido como Magia Sombria, era alimentado pela ambição e pelo ódio de um mago que, uma vez, foi um dos sábios mais respeitados de todo o continente.")
sleep(2)
print("Esse mago, chamado Zalderath, o Corrompido, buscou mais poder do que qualquer um poderia imaginar. Ele invocou o próprio Demônio da Escuridão, que lhe concedeu um poder infinito, mas também o transformou em um ser que não era mais humano. Agora, Zalderath controla um exército de monstros e criaturas deformadas, espalhando a escuridão por todo o mundo.")

sleep(2)
print("No entanto, os antigos sabiam que não haveria esperança sem a chegada de um herói. A Profecia do Destino dizia que quando a cidade de Legenda City fosse tomada pela escuridão e o mago corrompido estivesse perto de conquistar o mundo, um herói de coração puro e coragem inabalável surgiria para derrotá-lo e restaurar o equilíbrio.")

sleep(2)
print("E é aqui que você entra, [Nome do Jogador], um simples morador de Legenda City, até o momento em que seu destino se entrelaça com a profecia. Você foi escolhido pelas forças do bem para cumprir essa missão. Mas, antes de enfrentar Zalderath, você terá de passar por várias provações, encontrar aliados poderosos, e conquistar sua verdadeira força.")

sleep(2)
print("Legend City está em ruínas. As ruas que antes eram repletas de alegria, agora estão cheias de sombras e lamentos. Os habitantes estão em pânico, e os antigos templos de magia, agora corrompidos, tornaram-se esconderijos de criaturas malignas.")

sleep(2)
print("Você não sabe ainda, mas o seu caminho será repleto de perigos, mistérios e revelações. Durante sua jornada, você encontrará grupos secretos, ordens antigas, e até mesmo deuses adormecidos que podem ajudar ou tentar detê-lo. Seu destino será marcado por escolhas difíceis, onde você precisará decidir até onde vai em busca de justiça. A cada vitória, você sentirá o poder crescente dentro de si, mas também o peso da responsabilidade.\n")
sleep(2)

# Inimigos da história fixa (sequência linear)
inimigos = [
    {"nome": "Ladrão de Rua", "vida": 10, "ataque": 3, "recompensa": 2, "experiencia": 10},
    {"nome": "Lobo da Floresta", "vida": 12, "ataque": 4, "recompensa": 3, "experiencia": 15},
    {"nome": "Soldado do Mago Sombrio", "vida": 15, "ataque": 5, "recompensa": 4, "experiencia": 20}
]

chefao_final = {"nome": "Mago Sombrio", "vida": 50, "ataque": 12, "recompensa": 10, "experiencia": 50}

# Função de batalha
def batalha(inimigo, poções):
    global experiencia, vida_jogador
    print(f"\nVocê encontrou um {inimigo['nome']}!")
    
    vida_inimigo = inimigo["vida"]
    
    while vida_jogador > 0 and vida_inimigo > 0:
        print(f"\n{nome} - Vida: {vida_jogador} | Poções: {poções}")
        print(f"{inimigo['nome']} - Vida: {vida_inimigo}")
        print("\nO que deseja fazer?")
        print("1 - Atacar")
        print("2 - Usar Poção de Cura")

        escolha = input("\nEscolha sua ação: ")

        if escolha == "1":
            dano_jogador = random.randint(1, 6) + forca
            dano_inimigo = random.randint(1, 6) + inimigo["ataque"]

            print(f"\nVocê atacou o {inimigo['nome']} e causou {dano_jogador} de dano!")
            vida_inimigo -= dano_jogador

            if vida_inimigo <= 0:
                print(f"\nVocê derrotou o {inimigo['nome']}!")
                experiencia += inimigo["experiencia"]
                print(f"\nVocê ganhou {inimigo['experiencia']} pontos de experiência!")
                return inimigo["recompensa"], poções

            print(f"O {inimigo['nome']} atacou e causou {dano_inimigo} de dano em você!")
            vida_jogador -= dano_inimigo

            if vida_jogador <= 0:
                print("\nVocê foi derrotado...")
                return 0, poções

        elif escolha == "2":
            if poções > 0:
                vida_jogador += 10
                if vida_jogador > vida_maxima:
                    vida_jogador = vida_maxima
                poções -= 1
                print(f"\nVocê usou uma Poção de Cura! Vida restaurada para {vida_jogador}. Poções restantes: {poções}")
            else:
                print("\nVocê não tem mais Poções de Cura!")

        else:
            print("\nEscolha inválida! Tente novamente.")

    return 0, poções

# Função para aumento de nível
def aumentar_nivel():
    global nivel, experiencia, vida_jogador, forca, constituicao, destreza, inteligencia, forc_de_vont, carisma, percepcao
    if experiencia >= 50:
        nivel += 1
        experiencia -= 50
        print(f"\nVocê subiu para o nível {nivel}!\n")
        vida_jogador = vida_maxima + constituicao  # Vida máxima ao subir de nível
        pontos_para_distribuir = 3  # Pontos para distribuir nos atributos

        print("Distribua seus pontos nos atributos: ")
        for i in range(pontos_para_distribuir):
            atributo = random.choice(["Força", "Constituição", "Destreza", "Inteligência", "Força de Vontade", "Carisma", "Percepção"])
            if atributo == "Força":
                forca += 1
            elif atributo == "Constituição":
                constituicao += 1
            elif atributo == "Destreza":
                destreza += 1
            elif atributo == "Inteligência":
                inteligencia += 1
            elif atributo == "Força de Vontade":
                forc_de_vont += 1
            elif atributo == "Carisma":
                carisma += 1
            elif atributo == "Percepção":
                percepcao += 1
            print(f"Você aumentou seu atributo '{atributo}'!")
