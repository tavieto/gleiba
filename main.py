from selenium.webdriver import Firefox
import time

navegador = Firefox()
url = 'http://consultaaluno.educacao.ba.gov.br/'

navegador.get(url)

input = navegador.find_element_by_id('matricula')
input.send_keys("9040434")

time.sleep(0.2)

emailElement = navegador.find_element_by_tag_name('b')
email = emailElement.text
print(email)

# navegador.quit()
