from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from datetime import datetime
import time

def raspar_nomes(numero_jogos_por_pagina):
    nome_jogos = []
    for i in range(1, numero_jogos_por_pagina + 1):
        nome_xpath = f"/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[3]/a"
        nome_elemento = driver.find_element(By.XPATH, nome_xpath)
        nome_jogos.append(nome_elemento.text.replace(",", "."))
    return nome_jogos

def raspar_precos(numero_jogos_por_pagina):
    preco_jogos = []
    for i in range(1, numero_jogos_por_pagina + 1):
        nome_xpath = f"/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[5]"
        nome_elemento = driver.find_element(By.XPATH, nome_xpath)
        preco_jogos.append(nome_elemento.text.replace(",", "."))
    return preco_jogos

def raspar_avaliacao(numero_jogos_por_pagina):
    avaliacao_jogos = []
    for i in range(1, numero_jogos_por_pagina + 1):
        nome_xpath = f"/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[6]"
        nome_elemento = driver.find_element(By.XPATH, nome_xpath)
        avaliacao_jogos.append(nome_elemento.text.replace(",", "."))
    return avaliacao_jogos

def raspar_porcentagem_de_desconto(numero_jogos_por_pagina):
    porcentagem_de_desconto = []
    for i in range(1, numero_jogos_por_pagina + 1):
        nome_xpath = f"/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[4]"
        nome_elemento = driver.find_element(By.XPATH, nome_xpath)
        porcentagem_de_desconto.append(nome_elemento.text.replace(",", "."))
    return porcentagem_de_desconto

def raspar_data_lancamento(numero_jogos_por_pagina):
    data_lancamento_jogos = []
    for i in range(1, numero_jogos_por_pagina + 1):
        nome_xpath = f"/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[7]"
        nome_elemento = driver.find_element(By.XPATH, nome_xpath)
        data_lancamento_jogos.append(nome_elemento.text.replace(",", "."))
    return data_lancamento_jogos

def raspar_fim_do_desconto(numero_jogos_por_pagina):
    fim_do_desconto_jogos = []
    for i in range(1, numero_jogos_por_pagina + 1):
        nome_xpath = f"/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[8]"
        nome_elemento = driver.find_element(By.XPATH, nome_xpath)
        fim_do_desconto_jogos.append(nome_elemento.text.replace(",", "."))
    return fim_do_desconto_jogos

def salvar_csv(nome_jogos, preco_jogos, avaliacao_jogos, porcentagem_de_desconto_jogos, data_lancamento_jogos):
    data_atual = datetime.now()
    data_formatada = data_atual.strftime("%Y/%m/%d")
    caminho = f'dados/{data_formatada}'

    if not os.path.exists(caminho):
        os.makedirs(caminho)

    with open(f"{caminho}/informacoes.csv", "w", encoding="utf-8") as arq:
        arq.write("NOME,PRECO,AVALIACAO,PORCENTAGEM_DE_DESCONTO,DATA_LANCAMENTO\n")
        for nome, preco, avaliacao, porcentagem_de_desconto, data_lancamento in zip(nome_jogos, preco_jogos, avaliacao_jogos, porcentagem_de_desconto_jogos, data_lancamento_jogos):
            arq.write(f"{nome},{preco},{avaliacao},{porcentagem_de_desconto},{data_lancamento}\n")


def ajustar_numero_jogos_por_pagina():
    driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[1]/div[1]/select").click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[1]/div[1]/select/option[8]").click()
    time.sleep(2)


driver = webdriver.Chrome()
driver.get("https://steamdb.info/sales/")
time.sleep(5)

numero_jogos = int(driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[1]/div[1]/div/div/div/div[1]/h2/span").text.replace(",", ""))

nome_jogos= []
preco_jogos= []
avaliacao_jogos= []
porcentagem_de_desconto_jogos= []
data_lancamento_jogos= []

ajustar_numero_jogos_por_pagina()
nome_jogos = raspar_nomes(numero_jogos)
preco_jogos = raspar_precos(numero_jogos)
avaliacao_jogos = raspar_avaliacao(numero_jogos)
porcentagem_de_desconto_jogos = raspar_porcentagem_de_desconto(numero_jogos)
data_lancamento_jogos = raspar_data_lancamento(numero_jogos)
salvar_csv(nome_jogos, preco_jogos, avaliacao_jogos, porcentagem_de_desconto_jogos, data_lancamento_jogos)

driver.quit()
