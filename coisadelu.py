from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#escolhe o chrome
#endereco para o chrome driver
PATH = "/home/amanda/Documents/python/SpiritBot/SpiritFanficFavoritador/chromedriver"
driver = webdriver.Chrome(PATH)

#nome do arquivo com as contas que vc quer usar
FILE = open("NomesEContas/user1.txt","r")

verificador = 0

for i in range(17):
    driver.get("https://www.spiritfanfiction.com/login")

    usuario = FILE.readline()

    user = driver.find_element_by_id("Usuario")
    user.send_keys(usuario)
    user.send_keys(Keys.RETURN)

    senha = driver.find_element_by_id("Senha")
    senha.send_keys("senha1234@")
    senha.send_keys(Keys.RETURN)

    #abre a fanfic
    driver.get("https://www.spiritfanfiction.com/historia/largura-das-portas-19677653 ")

    #aperta fav
    fav = driver.find_element_by_id("botaoFavoritos")
    fav.click()


    #visualiza
    driver.get("https://www.spiritfanfiction.com/historia/largura-das-portas-19677653/capitulo1")

    #segue
    driver.get("https://www.spiritfanfiction.com/perfil/kodathewhel/addwatch")
    segue = driver.find_element_by_id("cphConteudo_cphPerfil_btnEnviar")
    segue.click()

    #logoff
    driver.get("https://www.spiritfanfiction.com/logoff")

    verificador+=1
    print(verificador)

driver.quit()