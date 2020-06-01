from selenium.webdriver import Firefox
import time

key = 'AIzaSyADFcrpdHlBqnPuvE70opOobrwSfGSE5qA'

navegador = Firefox()
url1 = 'http://consultaaluno.educacao.ba.gov.br/'

navegador.get(url1)

input = navegador.find_element_by_id('matricula')
input.send_keys("9040434")

time.sleep(1)

emailElement = navegador.find_element_by_tag_name('b')
email = emailElement.text
print(email)

#navegador.quit()
