import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from manipular_json import manipular_json
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from cria_excel import criaExcel

ID = "id"
XPATH = "xpath"

url = "https://esaj.tjce.jus.br/cpopg/open.do"
nome_arquivo_json = 'processos.json'
numero_arquivo_excel = 'numero-processos.xlsx'

option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(url)

def get_dados_processo(numero_processo_api):
    # Consulta processo
    driver.implicitly_wait(3)
    driver.find_element(By.ID, "numeroDigitoAnoUnificado").clear()
    driver.find_element(By.ID, "foroNumeroUnificado").clear()
    driver.find_element(By.ID, "numeroDigitoAnoUnificado").send_keys(numero_processo_api)
    
    driver.implicitly_wait(2)

    driver.find_element(By.ID, "botaoConsultarProcessos").click()
    
    driver.implicitly_wait(2)

    # Pega as informações do processo
    try:
        id_processo = driver.find_element(By.ID, "numeroProcesso")
        numero_processo = id_processo.text
    except NoSuchElementException:
        numero_processo = "Não encontrado"

    try:
        parte_autora_xpath = "//table[@id='tablePartesPrincipais']/tbody/tr[1]/td[2]"
        parte_autora = driver.find_element(By.XPATH, parte_autora_xpath).text
        parte_autora_adv = parte_autora.rsplit(":", 1)
    
        if len(parte_autora_adv) > 1:
            advogado = parte_autora_adv[1].strip()
        else:
            advogado = "Não encontrado"

    except NoSuchElementException:
        parte_autora = "Não encontrado"
        advogado = "Não encontrado"

    try:
        parte_requerida_xpath = "//table[@id='tablePartesPrincipais']/tbody/tr[2]/td[2]"
        parte_requerida = driver.find_element(By.XPATH, parte_requerida_xpath).text
    except NoSuchElementException:
        parte_requerida = "Não encontrado"
    
    dados = {
        'numeroProcesso': numero_processo,
        'parteAutora': parte_autora,
        'parteRequerida': parte_requerida,
        'advogado': advogado
    }

    if numero_processo != "Não encontrado":
        manipular_json(nome_arquivo_json, dados)
    
    try:
        seta_voltar = driver.find_element(By.ID, "setaVoltar")
        seta_voltar.click()
        driver.implicitly_wait(3)
    except (NoSuchElementException, ElementClickInterceptedException) as error:
        seta_voltar = "Não encontrado"
        print(error)

    # checa se tem popup solicitando senha 
    try:
        cancel_botao = driver.find_element(By.ID, "botaoFecharPopupSenha")
        cancel_botao.click()
        driver.implicitly_wait(3)
    except (NoSuchElementException, ElementClickInterceptedException) as error:
        cancel_botao = "Não encontrado"

df_numero = pd.read_excel(numero_arquivo_excel, dtype="string")

for celula in df_numero[0]:
    print(celula)
    get_dados_processo(celula)

criaExcel()

# Finaliza o bot
driver.quit()