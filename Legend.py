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
nome = input("\n"
"Olá, guerreiro... Digite o seu nome: ")
nome = nome.lower().capitalize()

print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")
print(f"\nOlá, {nome}, seja bem-vindo a Legenda City!\n")
print("A cidade precisa de um herói para enfrentar os perigos que assolam a região...\n")
print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")


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
        sleep(1)
        print(f"{key} - {value[0]}: {value[1]}")

# Escolha da classe
while True:
    print("\nClasses:")
    exibir_classes()
    
    escolha_classe = int(input("\nQual é sua escolha? (somente um número): "))

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
poções = 8  # Poções de cura

# História inicial
print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")
print(f"\nBem-vindo ao início de sua jornada, {nome}!\n")
print(f"\nAgora, {nome}, como o novo herói, você saberá o verdadeiro motivo de ter sido convocado...\n")

sleep(2)
print("\n    Há milênios, a terra de Legend City foi governada por dragões e seres mágicos imortais. Eles criaram os primeiros reinos e mantiveram o equilíbrio do mundo. No entanto, uma força sombria começou a se espalhar pelas terras, um poder desconhecido que corrompeu tudo o que tocava. Esse poder, conhecido como Magia Sombria, era alimentado pela ambição e pelo ódio de um mago que, uma vez, foi um dos sábios mais respeitados de todo o continente.")

sleep(2)
print("\n    Esse mago, chamado Zalderath, o Corrompido, buscou mais poder do que qualquer um poderia imaginar. Ele invocou o próprio Demônio da Escuridão, que lhe concedeu um poder infinito, mas também o transformou em um ser que não era mais humano. Agora, Zalderath controla um exército de monstros e criaturas deformadas, espalhando a escuridão por todo o mundo.")

sleep(2)
print("\n    No entanto, os antigos sabiam que não haveria esperança sem a chegada de um herói. A Profecia do Destino dizia que quando a cidade de Legend City fosse tomada pela escuridão e o mago corrompido estivesse perto de conquistar o mundo, um herói de coração puro e coragem inabalável surgiria para derrotá-lo e restaurar o equilíbrio.")

sleep(2)
print(f"\n    E é aqui que você entra, {nome}, um simples morador de Legend City, até o momento em que seu destino se entrelaça com a profecia. Você foi escolhido pelas forças do bem para cumprir essa missão. Mas, antes de enfrentar Zalderath, você terá de passar por várias provações, encontrar aliados poderosos, e conquistar sua verdadeira força.")

sleep(2)
print("\n    Legend City está em ruínas. As ruas que antes eram repletas de alegria, agora estão cheias de sombras e lamentos. Os habitantes estão em pânico, e os antigos templos de magia, agora corrompidos, tornaram-se esconderijos de criaturas malignas.")

sleep(2)
print("\n    Você não sabe ainda, mas o seu caminho será repleto de perigos, mistérios e revelações. Durante sua jornada, você encontrará grupos secretos, ordens antigas, e até mesmo deuses adormecidos que podem ajudar ou tentar detê-lo. Seu destino será marcado por escolhas difíceis, onde você precisará decidir até onde vai em busca de justiça. A cada vitória, você sentirá o poder crescente dentro de si, mas também o peso da responsabilidade.\n")
sleep(2)
print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")

# Inimigos da história fixa (sequência linear)
fases = [
    {"nome": "O Querubim feroz", "vida": 15, "ataque": 4, "fala": "\n😇 Minha ira cairá sobre você! 👿"},
    {"nome": "O Poltergeist", "vida": 20, "ataque": 5, "fala": "👻 UHHHH! Já vejo que está com medo..."},
    {"nome": "O Pistoleiro Plasmático", "vida": 25, "ataque": 6, "fala": "🔫 Eu vou acabar com você!"},
    {"nome": "O Mercenário Sombrio", "vida": 28, "ataque": 7, "fala": "⚰️ A morte te espera!"},
    {"nome": "O Feiticeiro das Sombras", "vida": 30, "ataque": 8, "fala": "🧙‍♂️ Sua alma me pertence!"},
    {"nome": "O Ogro Selvagem", "vida": 35, "ataque": 10, "fala": "👹 HAHA! Você é pequeno demais!"},
    {"nome": "O Assassino da Guilda", "vida": 40, "ataque": 12, "fala": "🕵️ Silêncio... Você já está morto."},
    {"nome": "O Necromante", "vida": 45, "ataque": 13, "fala": "🧟 Levantem-se, mortos! Destruam esse inseto! 🧟"},
    {"nome": "O Golem de Pedra", "vida": 50, "ataque": 14, "fala": "🪨 Vou tranformar você em calcário..."},
    {"nome": "O aralto de Zalderath", "vida": 55, "ataque": 15, "fala": "🧙 Zalderath ordenou que eu termine essa terefa!"},
]

# Chefão Final
chefe_final = {"nome": "Zalderath, o Corrompido", "vida": 100, "ataque": 20, "fala": f"🐉 Eu esperei por você, {nome}, o heroizinho medíocre! ☠️"}

# Sistema de batalha
def batalha(inimigo):
    global vida_jogador, experiencia, poções
    vida_inimigo = inimigo["vida"]
    print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print(f"\n⚔️ {inimigo['nome']} apareceu!\n")
    sleep(2)
    print(f"{inimigo['fala']}")
    sleep(2)
    
    while vida_jogador > 0 and vida_inimigo > 0:
        print(f"\n{nome} - Vida: {vida_jogador} | Poções: {poções}")
        print(f"{inimigo['nome']} - Vida: {vida_inimigo}")
        
        print("\nO que deseja fazer?")
        print("1 - Atacar")
        print("2 - Usar Poção de Cura")
        print("3 - Recuar")
        
        escolha = input("\nEscolha sua ação: ")
        
        if escolha == "1":
            rolagem = random.randint(1, 20)
            
            if rolagem >= 17 and rolagem <= 20:
                dano = (forca + 5) * 2
                print("O dado foi jogado...")
                sleep(1)
                print("\n⚡ GOLPE CRÍTICO! Você causou um dano devastador!")
            elif rolagem <= 4:
                dano = 0
                print("O dado foi jogado...")
                sleep(1)
                print("\n❌ Você errou o ataque!")
            else:
                print("O dado foi jogado...")
                sleep(1)
                dano = forca + 5

            vida_inimigo -= dano
            sleep(1)
            print(f"\nVocê atacou e causou {dano} de dano!")
            
            if vida_inimigo <= 0:
                print(f"\n🔥 Você derrotou {inimigo['nome']}!")

                experiencia += 20
                
                if experiencia >= 40:
                    print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")
                    print("\n🎉 Você subiu de nível!")
                    print("📈 Sua vida e valor de ataque aumentaram!")
                    
                    # Melhorando o personagem ao subir de nível
                    vida_jogador += 7
                    dano = forca + 8
                    experiencia = 0  # Reseta a XP para o próximo nível
                else:
                    print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")
                    print(f"\n📊 Experiência atual: {experiencia}EXP/40EXP")

                return  # Encerra a batalha pois o inimigo foi derrotado


            dano_inimigo = random.randint(1, 6) + inimigo["ataque"]
            vida_jogador -= dano_inimigo
            sleep(1)
            print(f"{inimigo['nome']} atacou e causou {dano_inimigo} de dano em você!")

        elif escolha == "2" and poções > 0:
            if poções==0:
                print("Você não tem mais poções!")
            else:
                cura = random.randint(10, 20)
                vida_jogador += cura
                poções -= 1
                sleep(1)
                print(f"\n🧪💔 Você usou uma poção e recuperou {cura} de vida! 💖")
        
        elif escolha == "3" and inimigo != chefe_final:
                print("\n🎲 Tentando fugir...")
                sleep(1)
                if random.randint(1, 20) > 10:
                    print("\n🏃 Você conseguiu fugir com sucesso!")
                    return  # O jogador escapa e a batalha termina
                else:
                    print("\n❌ Você falhou ao fugir e o inimigo atacou!")
                    dano_inimigo = random.randint(1, 6) + inimigo["ataque"]
                    vida_jogador -= dano_inimigo
                    print(f"{inimigo['nome']} atacou e causou {dano_inimigo} de dano!")

        else:
            print("\n⚔️ Você continua lutando!")

    

# Jogando as fases
for i, fase in enumerate(fases):
    print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("\n⚔️ Prepare-se para a próxima batalha! ⚔️")
    sleep(2)
    batalha(fase)

    # Se o jogador morrer, o jogo para
    if vida_jogador <= 0:
        print("\n💀 Você foi derrotado! A escuridão triunfou... 💀")
        exit()

# Enfrentando o chefão final
batalha(chefe_final)

print(f"\n🎉{nome}, você venceu Zalderath e salvou Legend City!")