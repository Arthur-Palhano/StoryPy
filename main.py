import random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
firefox = webdriver.Firefox(options=options)


def getName(classe):
    firefox.get(f"https://www.nomesdefantasia.com/{classe}/short/")
    namesOptions = firefox.find_elements_by_tag_name("li")
    name = random.choice(namesOptions).text
    return name


def getPlace():
    places = ["Ruínas", "Planíces", "Masmorra", "Floresta",
              "Templo", "Pântano", "Deserto", "Montanhas",
              "Cataratas", "Reino", "Vale", "Profundezas",
              "Oceano"]
    place = random.choice(places) + " de " + getName("mixed")
    return place


def getQuest():
    quests = ["Um grupo de conjuradores sob a liderança de um arquimago",
              "Criaturas deformadas com uma enorme sede de sangue que irão caçar suas presas a partir de um pedaço de roupa da vítima ou um item pessoal",
              "Um grupo de artistas marciais altamente treinados", "Infiltradores enviados pela maior Guilda de Assassinos",
              "Um grupo de soldados que recebeu dádiva das trevas que os torna mais fortes e rápidos que um homem normal", "Uma horda de espíritos de escravos que foram erguidos do local de onde foram assassinados",
              "Um grupo de zelotes que luta sob uma profecia que é verdadeira", "Um grupo de mercenários que juntos são quase imbatíveis"]
    quest = random.choice(quests)
    return quest.lower()


def getRole():
    roles = ["Cavaleiro", "Mago", "Assassino", "Ladino",
             "Arqueiro", "Músico", "Ninja", "Necromante",
             "Dançarino", "Tritão", "Druida", "Astrônomo", "Médico"]
    role = random.choice(roles).lower()
    return role


pers = [getName("human"), getRole(), getQuest(), getPlace(), ]

print(f"Era uma vez um {pers[1]} que se chamava {pers[0]}, ele vivia em {pers[3]}, um dia, esse {pers[1]} foi convocado pelo rei de {pers[3]} e foi incubido de derrotar {pers[2]}, teria {pers[0]} sucesso em sua missão?")
firefox.close()
