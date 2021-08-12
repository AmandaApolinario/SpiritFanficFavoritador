from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#escolhe o chrome
PATH = "/home/amanda/Documents/python/SpiritBot/SpiritFanficFavoritador/chromedriver"
driver = webdriver.Chrome(PATH)

FILE = open("NomesEContas/dados.txt","r")
verificador = 0

for i in range(25):
    usuario = FILE.readline()
    #abre o site pra fazer cadastro
    driver.get("https://www.spiritfanfiction.com/cadastrar")
    
    user = driver.find_element_by_id("Usuario")
    user.send_keys(usuario)
    user.send_keys(Keys.RETURN)

    email = driver.find_element_by_id("Email")
    emailfinal = usuario + "@gmail.com"
    email.send_keys(emailfinal)
    email.send_keys(Keys.RETURN)

    #a senha eh padrao
    senha = driver.find_element_by_id("Senha")
    senha.send_keys("senha1234@")
    senha.send_keys(Keys.RETURN)

    #coloca um avatar
    driver.get("https://www.spiritfanfiction.com/editar/avatar")
    foto = random.randint(1,351)
    caminho = "/home/amanda/Pictures/kpop/" + str(foto) +".jpg"

    try:
        element = WebDriverWait(driver,15).until(
            EC.presence_of_element_located((By.ID,"cphConteudo_cphConteudo_fupUsuarioAvatar"))
        )
        element.send_keys(caminho)
    except:
        print("erro no upload da foto do usuario " + usuario)
    
    
    try:
        element = WebDriverWait(driver,15).until(
            EC.presence_of_element_located((By.ID, "cphConteudo_cphConteudo_btnEnviarAvatar"))
        )
        element.click()
    except:
        print("erro no envio da foto " + str(foto) + "user " + usuario)

    driver.get("https://www.spiritfanfiction.com/logoff")

    verificador+=1
    print(verificador)

driver.quit()