from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define o caminho do driver do Chrome
chrome_driver_path = "/usr/local/bin/chromedriver."

# Abre o navegador Chrome
driver = webdriver.Chrome(chrome_driver_path)

# Navega até o site da tabela de alimentos
driver.get("http://www.tabeladealimentos.com.br/")

# Aguarda até que o campo de pesquisa esteja presente na página
campo_pesquisa = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-input"]')))

# Digita o alimento desejado no campo de pesquisa
campo_pesquisa.send_keys("alimento desejado")

# Pressiona a tecla Enter para realizar a pesquisa
campo_pesquisa.send_keys(Keys.ENTER)

# Aguarda até que a lista de resultados esteja presente na página
resultados = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-list"]/li[1]')))

# Clica no primeiro resultado da lista de resultados
resultados.click()

# Aguarda até que as informações do alimento estejam presentes na página
informacoes_alimento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[1]')))

# Obtém as informações do alimento e as salva em um arquivo txt
with open("informacoes_alimento.txt", "w") as f:
    f.write(informacoes_alimento.text)

# Fecha o navegador Chrome
driver.quit()
