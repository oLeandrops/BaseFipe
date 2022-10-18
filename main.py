
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from funcoesDB import cadastrarCarro

browser = Chrome('DRIVERS/chromedriver.exe')
url = 'https://veiculos.fipe.org.br/'
browser.implicitly_wait(2)
browser.get(url)
sleep(5)
tabelaFipe = []
#Selecionar menus para extrair os dados
indice = browser.find_elements(By.CSS_SELECTOR,'li[class="ilustra"] div[class="title"]')  
#Selecionar primeiro Indice "Consulta de carros e utiliarios pequenos"
indice[0].click()
#clicar mostrar as marcas
#browser.find_element(By.CSS_SELECTOR,'select[data-placeholder="Digite ou selecione a marca do veiculo"]').click()
#browser.find_element(By.CSS_SELECTOR,'div[class="step-1"] div.input[urlconsulta="ConsultarModelos"]').click()
sleep(1)
#Clicar na primeira pesquisa que é de marca de carro
browser.find_element(By.CSS_SELECTOR,'a[class*="chosen-single chosen-default"]').click()
sleep(1)
listaMarcas =  browser.find_elements(By.CSS_SELECTOR,'div[class="chosen-drop"] ul li')
listaMarcasTexto = []
for item in listaMarcas:
     listaMarcasTexto.append(item.text)
for marca in listaMarcasTexto:
     if not marca == listaMarcasTexto[0]:
          browser.find_elements(By.CSS_SELECTOR,'div[class="chosen-container chosen-container-single"] a[class="chosen-single"][tabindex="-1"]')[1].click()
     browser.find_elements(By.CSS_SELECTOR,'div[class="chosen-drop"] div[class="chosen-search"] input[tabindex="2"]')[0].send_keys(marca)
     browser.find_elements(By.CSS_SELECTOR,'div[class="chosen-drop"] div[class="chosen-search"] input[tabindex="2"]')[0].send_keys(Keys.ENTER)
     #clicar no segundo campo de pesquisa de modelo
     sleep(1)
     browser.find_element(By.CSS_SELECTOR,'div[urlconsulta="ConsultarAnoModelo"]').click()
     #pegar a lista de carros da lista de marcas

     listaCarros = browser.find_elements(By.CSS_SELECTOR,'div[class="chosen-drop"] ul li')
     listaCarrosTexto = []
     for item in listaCarros:
          listaCarrosTexto.append(item.text)
     for carros in listaCarrosTexto:
          try:
               if not carros == listaCarrosTexto[0]:
                    teste = browser.find_element(By.CSS_SELECTOR,'div[urlconsulta="ConsultarAnoModelo"]')
                    teste.click()
               browser.find_elements(By.CSS_SELECTOR,'div[class="chosen-drop"] div[class="chosen-search"] input[tabindex="2"]')[1].send_keys(carros)
               browser.find_elements(By.CSS_SELECTOR,'div[class="chosen-drop"] div[class="chosen-search"] input[tabindex="2"]')[1].send_keys(Keys.ENTER)
          except:
               break
               #Selecionar modelo atraves do ano
          browser.find_element(By.CSS_SELECTOR,'div[urlconsulta="ConsultarModelosAtravesDoAno"]').click() 
          sleep(3)
          listaModelos = browser.find_elements(By.CSS_SELECTOR,'div[class="chosen-drop"] ul li')
          listaModelosTexto = []
          for item in listaModelos:
               listaModelosTexto.append(item.text)
          for modelo in listaModelosTexto:
               inserircarro(marca,carros,modelo)
               sleep(3)
               if not modelo == listaModelos[0]:
                    browser.find_element(By.CSS_SELECTOR,'div[urlconsulta="ConsultarModelosAtravesDoAno"]').click() 
               input_1 = browser.find_elements(By.CSS_SELECTOR,'div[class="chosen-drop"] div[class="chosen-search"] input[tabindex="2"]')[2]
               input_1.send_keys(modelo)
               browser.find_elements(By.CSS_SELECTOR,'div[class="chosen-drop"] div[class="chosen-search"] input[tabindex="2"]')[2].send_keys(Keys.ENTER)    
               #Selecionar Pesquisa
               browser.find_element(By.CSS_SELECTOR,'#buttonPesquisarcarro').click()
               #Realizar consulta do carro 
               dados = browser.find_elements(By.CSS_SELECTOR,'tbody tr') 
               #criar dicionarios para receber os dados consultados
               carro={'MesReferencia' : dados[0].find_elements(By.CSS_SELECTOR,'td')[1].text,
               'CodigoFipe' : dados[1].find_elements(By.CSS_SELECTOR,'td')[1].text,
               'Marca' : dados[2].find_elements(By.CSS_SELECTOR,'td')[1].text,
               'Modelo' : dados[3].find_elements(By.CSS_SELECTOR,'td')[1].text,
               'AnoModelo' : dados[4].find_elements(By.CSS_SELECTOR,'td')[1].text,
               'Autentificacao' : dados[5].find_elements(By.CSS_SELECTOR,'td')[1].text,
               'DataCosnulta' : dados[6].find_elements(By.CSS_SELECTOR,'td')[1].text ,
               'PrecoMedio' : dados[7].find_elements(By.CSS_SELECTOR,'td')[1].text ,
                    }
               tabelaFipe.append(carro)
               sleep(3)
               
          
               
              
          

          

