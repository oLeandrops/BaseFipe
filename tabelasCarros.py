from bdb import Breakpoint
from symbol import break_stmt
from time import sleep
from urllib.parse import urlparse
from turtle import back
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from funcoesDB import cadastrarCarro,consultalink,atualizarlink
#url = 'https://tabelacarros.com/marcas/carros#'
browser = Chrome('DRIVERS/chromedriver.exe')
for volta in range(1,100000):
    url, id = consultalink()
    browser.get(url)
    browser.implicitly_wait(2)
    count = len(browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]'))
    pagina_incial = urlparse(browser.current_url).path
    if count >1:
        for c in range(0,count):
            print(c)
            browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')[c].click()
            if len(browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')) >=1:
                browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')[0].click()
            if len(browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')) >=1:
                browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')[0].click()
            if len(browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')) >=1:
                browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')[0].click()
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
            if len(infocarro.find_elements(By.CSS_SELECTOR,'tr'))>8:
                categoria = infocarro.find_elements(By.CSS_SELECTOR,'tr')[8].text  
                cadastrarCarro(fabricante,modelo,anoModelo,versao,codigoFipe,preco,ultimaVariacao,mesReferencia,categoria)
            else:
                cadastrarCarro(fabricante,modelo,anoModelo,versao,codigoFipe,preco,ultimaVariacao,mesReferencia,None)    
            atualizarlink(id)
            browser.back()
            pagina_atual = urlparse(browser.current_url).path
            if 'MARRUA' in pagina_atual and 'carros' in pagina_atual:
                if 'modelo' not in pagina_atual:
                    print('ook')
            elif 'anos_modelos' in pagina_incial and 'carros' in pagina_atual and len(browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')) >1:
                num = len(browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]'))
                for c in range(0,num):
                    browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')[c].click()
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
                    if len(infocarro.find_elements(By.CSS_SELECTOR,'tr'))>8:
                        categoria = infocarro.find_elements(By.CSS_SELECTOR,'tr')[8].text  
                        cadastrarCarro(fabricante,modelo,anoModelo,versao,codigoFipe,preco,ultimaVariacao,mesReferencia,categoria)
                    else:
                        cadastrarCarro(fabricante,modelo,anoModelo,versao,codigoFipe,preco,ultimaVariacao,mesReferencia,None)    
                    atualizarlink(id)
                    browser.back()
                browser.back()
            
            elif 'anos_modelos' in pagina_incial and 'motos' in pagina_atual and len(browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')) >1:
                print('é moto e tem varias versoes')
                num = len(browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]'))
                for c in range(0,num):
                    browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')[c].click()
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
                    if len(infocarro.find_elements(By.CSS_SELECTOR,'tr'))>8:
                        categoria = infocarro.find_elements(By.CSS_SELECTOR,'tr')[8].text  
                        cadastrarCarro(fabricante,modelo,anoModelo,versao,codigoFipe,preco,ultimaVariacao,mesReferencia,categoria)
                    else:
                        cadastrarCarro(fabricante,modelo,anoModelo,versao,codigoFipe,preco,ultimaVariacao,mesReferencia,None)    
                    atualizarlink(id)
                    browser.back()
                browser.back()
                    
            elif 'motos' in pagina_atual and len(browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')) ==1:
                print('é moto mas só tem uma versao')
                browser.back()
                    
            elif 'anos_modelos' in pagina_incial and 'caminhoes' in pagina_atual and len(browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')) >1:
                print('é caminhao com varias versoes')
                num = len(browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]'))
                for c in range(0,num):
                    browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')[c].click()
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
                    if len(infocarro.find_elements(By.CSS_SELECTOR,'tr'))>8:
                        categoria = infocarro.find_elements(By.CSS_SELECTOR,'tr')[8].text  
                        cadastrarCarro(fabricante,modelo,anoModelo,versao,codigoFipe,preco,ultimaVariacao,mesReferencia,categoria)
                    else:
                        cadastrarCarro(fabricante,modelo,anoModelo,versao,codigoFipe,preco,ultimaVariacao,mesReferencia,None)    
                    atualizarlink(id)
                    browser.back()
                browser.back()
                
            elif 'anos_modelos' in pagina_incial and 'caminhoes' in pagina_atual and len(browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')) ==1:
                print('é caminhao mas só tem uma versao')
                browser.back()
                
        else:
            if 'modelo' not in browser.current_url:
                    browser.back()
        if browser.current_url == 'data:,':
            browser.forward()
        if 'modelo' not in browser.current_url:
            browser.forward()
    elif count <=1:
        browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')[0].click()
        if len(browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]'))>=1:
            browser.find_elements(By.CSS_SELECTOR,'tr[data-url*="https"]')[0].click()
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
        if  len(infocarro.find_elements(By.CSS_SELECTOR,'tr'))>8:
                categoria = infocarro.find_elements(By.CSS_SELECTOR,'tr')[8].text  
                cadastrarCarro(fabricante,modelo,anoModelo,versao,codigoFipe,preco,ultimaVariacao,mesReferencia,categoria)
        else:
            cadastrarCarro(fabricante,modelo,anoModelo,versao,codigoFipe,preco,ultimaVariacao,mesReferencia,None)    
        atualizarlink(id)
        

    

