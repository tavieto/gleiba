# Acessando dados da planilha
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('greb.json', scope)
client = gspread.authorize(creds)
# Nome da planilha acessada
sheet = client.open("lista-teste").sheet1
# Dados a serem coletados
col = sheet.col_values(2)

# Abrindo navegador
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

navegador = webdriver.Chrome(ChromeDriverManager().install())
url = 'http://consultaaluno.educacao.ba.gov.br/'
navegador.get(url)

input = navegador.find_element_by_id('matricula')

for id in range(1, len(col)):
    navegador.implicitly_wait(4)
    input.send_keys(col[id])
    try:
        emailElement = navegador.find_element_by_tag_name('b')
        email = emailElement.text
    except:
        email = "Email não encontrado"
    sheet.update_acell('C' + str(id+1), email)
    input.clear()

navegador.quit()
