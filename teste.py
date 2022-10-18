from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from funcoesDB import cadastrarCarro
from funcoesDB import cadastrarlink
url = 'https://tabelacarros.com/marcas/carros#'
browser = Chrome('DRIVERS/chromedriver.exe')
browser.get(url)
browser.implicitly_wait(10)
sleep(5)
listaDeMarcas = browser.find_elements(By.CSS_SELECTOR,'div[class="box_marcas_todas"] a')
for marca in listaDeMarcas:
    cadastrarlink('Acura',None,marca.text,marca.get_attribute('href'))
    marca.click()

    
    listaDeCarros = browser.find_elements(By.CSS_SELECTOR,'div[class="box_todos_modelos"] a')
    for carros in listaDeCarros:
        link = carros.get_attribute('href')
        cadastrarlink('CAMINHOES',None,carros.text,link)

#quando um carro tem muitos modelos
    modelos = browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')
    for modelo in modelos:
        link = modelo.get_attribute('data-url')
        cadastrarlink(None,None,modelo.text,link)








    
        carros.send_keys(Keys.ENTER)
        listaDeModelos = browser.find_elements(By.CSS_SELECTOR,'table[class="tabela1 links"] tr[data-url*="http"]a')
        breakpoint()
        for modelos in listaDeModelos:
            modelos.click()
            browser.find_element(By.CSS_SELECTOR,'tr[class="link"]').click()
            sleep(1)
            infocarro = browser.find_element(By.CSS_SELECTOR,'table[class="info"]')
            fabricante = infocarro.find_elements(By.CSS_SELECTOR,'tr')[0].text 
            modelo = infocarro.find_elements(By.CSS_SELECTOR,'tr')[1].text
            anoModelo = infocarro.find_elements(By.CSS_SELECTOR,'tr')[2].text
            versao = infocarro.find_elements(By.CSS_SELECTOR,'tr')[3].text
            codigoFipe = infocarro.find_elements(By.CSS_SELECTOR,'tr')[4].text    
            preco = infocarro.find_elements(By.CSS_SELECTOR,'tr')[5].text 
            ultimaVariacao = infocarro.find_elements(By.CSS_SELECTOR,'tr')[6].text
            mesReferencia = infocarro.find_elements(By.CSS_SELECTOR,'tr')[7].text 
            categoria = infocarro.find_elements(By.CSS_SELECTOR,'tr')[8].text  
            cadastrarCarro(fabricante,modelo,anoModelo,versao,codigoFipe,preco,ultimaVariacao,mesReferencia,categoria)
            browser.back()
            browser.back()
            listaDeModelos = browser.find_elements(By.CSS_SELECTOR,'table[class="tabela1 links"] tr[data-url*="http"]')
            