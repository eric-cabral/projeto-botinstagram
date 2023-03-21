from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

# AUTOMÁÇÃO DE MENSAGENS NO INSTAGRAM

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Edge(service=Service(r'C:\Users\user\Desktop\msedgedriver\msedgedriver.exe'))

    # Logar no Instagram e entrar no perfil desejado
    def login(self):
        try:
            driver = self.driver
            driver.get('https://www.linkedin.com/')
            time.sleep(2)
            #login_button = driver.find_element(By.CLASS_NAME, '_aa4b _add6 _ac4d')
            #login_button.click()
            user_element = driver.find_element(By.XPATH, '//input[@name="username"]')
            user_element.clear()
            user_element.send_keys(self.username)
            password_element = driver.find_element(By.XPATH, '//input[@name="password"]')
            password_element.clear()
            password_element.send_keys(self.password)
            password_element.send_keys(Keys.RETURN)
            time.sleep(3)
            self.acessar_perfil('--INSTRAGEM USERNAME--')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    # Acessar a área de inbox e enviar mensagem desejada
    def acessar_perfil(self, arroba):
        driver = self.driver
        driver.get('https://www.instagram.com/'+ arroba +'/')
        time.sleep(2)
        enviar_msg = driver.find_element(By.CLASS_NAME, 'xsz8vos').click()
        time.sleep(2)
        msg = driver.find_element(By.TAG_NAME, 'textarea')
        msg_escolhida = 'Boa noite!!!'
        msg.send_keys(msg_escolhida)
        msg.send_keys(Keys.RETURN)


iniciar = InstagramBot('--USERNAME--', '--PASSWORD--')
iniciar.login()
