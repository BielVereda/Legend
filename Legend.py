import random
from time import sleep

# Atributos iniciais
forca = 0
constituicao = 0

# Nome do jogador
nome = input("\n"
"Olá, guerreiro(a)... Digite o seu nome: ")
nome = nome.lower().capitalize()

print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")
print(f"\nOlá, {nome}, seja bem-vindo a Legenda City!\n")
print("A cidade precisa de um herói para enfrentar os perigos que assolam a região...\n")

# Definições iniciais
vida_maxima = 40  # Vida cheia
vida_jogador = vida_maxima + constituicao  # Vida do jogador baseada na constituição
nivel = 1  # Nível inicial
experiencia = 0  # Experiência inicial
poções = 15  # Poções de cura

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

# Inimigos da história fixa (sequência linear)
fases = [
    {"nome": "O Querubim feroz", "vida": 15, "ataque": 4, "fala": "\nO Querubim feroz: 😇 Minha ira cairá sobre você! 👿", "frase": f"{nome}: Você não conseguirá me deter... ⚔️ "},
    {"nome": "O Poltergeist", "vida": 20, "ataque": 5, "fala": "O Poltergeist: 👻 UHHHH! Já vejo que está com medo...", "frase": f"{nome}: Será que chamo os Goosebusters? 👻"},
    {"nome": "O Pistoleiro Plasmático", "vida": 25, "ataque": 6, "fala": "O Pistoleiro Plasmático: 🔫 Headshot na certa.", "frase": f"{nome}: Não se eu me desviar..."},
    {"nome": "O Mercenário Sombrio", "vida": 28, "ataque": 7, "fala": "O Mercenário Sombrio: ⚰️ A morte te espera!", "frase": f"{nome}: 🦥 Não se eu for devagar."},
    {"nome": "O Feiticeiro das Sombras", "vida": 30, "ataque": 8, "fala": "O Feiticeiro das Sombras: 🧙‍♂️ Meus feitiços são a sua fraqueza!", "frase": f"{nome}: Eu não tenho fraquezas. 💪"},
    {"nome": "O Ogro Selvagem", "vida": 35, "ataque": 10, "fala": "O Ogro Selvagem: 👹 HAHA! Você é pequeno demais!","frase": f"{nome}: 👦 Davi e Golias... 2° Round. 🧌"},
    {"nome": "O Caçador de Zalderath", "vida": 40, "ataque": 12, "fala": "O Caçador de Zalderath: 🕵️ Silêncio... Você já está morto.","frase": f"{nome}: Bla, bla , bla..."},
    {"nome": "O Necromante", "vida": 45, "ataque": 13, "fala": "O Necromante: 🧟 Levantem-se, mortos! Destruam esse inseto! 🧟", "frase": f"{nome}: 🕸️ Quando eu virar aranha, te aviso. 🕷️"},
    {"nome": "O Golem de Pedra", "vida": 50, "ataque": 14, "fala": "O Golem de Pedra: 🪨 Vou tranformar você em calcário...","frase": f"{nome}: 🪨 Não precisa. Já sou mais forte que uma pedra... 💪"},
    {"nome": "O Aralto de Zalderath", "vida": 55, "ataque": 15, "fala": "O Aralto de Zalderath: 🧙 Zalderath ordenou que eu termine essa terefa!", "frase": f"{nome}: 🧑‍🎓 Esse dever de casa é vitalício. 🧑‍🏫"},
]

# Chefão Final
chefe_final = {"nome": "Zalderath, o Corrompido", "vida": 100, "ataque": 20, "fala": f"🐉 Eu esperei por você, {nome}... Heroizinho medíocre!! ☠️"}

# Sistema de batalha
def batalha(inimigo):
    global vida_jogador, experiencia, poções
    vida_inimigo = inimigo["vida"]
    print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print(f"\n⚔️  {inimigo['nome']} apareceu!\n")
    sleep(2)
    print(f"{inimigo['fala']}")
    sleep(1)
    print(f"{inimigo["frase"]}")
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
                dano = (forca + 8) * 2
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
                dano = forca + 8

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
                    dano = forca + 10
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
                    dano_inimigo = random.randint(1, 8) + inimigo["ataque"]
                    vida_jogador -= dano_inimigo
                    print(f"{inimigo['nome']} atacou e causou {dano_inimigo} de dano!")

        else:
            print("\n⚔️ Você continua lutando!")

    

# Jogando as fases
for i, fase in enumerate(fases):
    print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("\n⚔️  Prepare-se para a próxima batalha! ⚔️")
    sleep(2)
    batalha(fase)

    # Se o jogador morrer, o jogo para
    if vida_jogador <= 0:
        print("\n💀 Você foi derrotado! A escuridão triunfou... 💀")
        exit()

# Enfrentando o chefão final
batalha(chefe_final)

print(f"\n🎉{nome}, você venceu Zalderath e salvou Legend City!")