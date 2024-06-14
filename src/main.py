#importando as funções
from meuPacote.atletas import getAge
from meuPacote.atletas import getCountry
from meuPacote.atletas import getMedal
from meuPacote.email import enviar_email


#importando bibliotecas
import os 
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv 
load_dotenv()
BASE_DIR = str(Path(os.path.dirname(__file__)).parent)

#arquivo com nome dos atletas
def main():
    file = BASE_DIR + '/data/nomesAtletas.xlsx'
    df = pd.read_excel(file)
    print (df)

#fazer uma lista com os nomes
df ='/data/nomesAtletas.xlsx'
listaNomes = df['nome'].values.tolist()

#data frame
atletas ={
    'nome':[],
    'idade':[],
    'pais':[],
    'medalha':[]
}
ages = []
for nome in listaNomes:
    age = getAge(nome)
    ages += [age]
    ages.append(ages)
    print(age)

countrys = []
for nome in listaNomes:
    country = getCountry(nome)
    countrys += [country]
    countrys.append(countrys)
    print(countrys)

medals =[]
for nome in listaNomes:
    medal = getMedal(nome)
    medals += [medal]
    medals.append(medals)
    print(medals)


df_dicionario = pd.DataFrame(atletas)
df['ages'] = ages
df['countrys'] = countrys
df['medals'] = medals
print(df_dicionario)

df_dicionario.to_excel (BASE_DIR +  '/data/listaFinal.xslx')


#atletas 30 anos ouro
atletas_ouro_30 = df_dicionario[(df_dicionario['ages']>30)& (df_dicionario[medal]=='Gold')]

#atletas eua
num_atletas_eua = df_dicionario[df_dicionario['coutrys']=='United States'].shape[0]

#atleta mais velho
oldest_atleta = df_dicionario[df_dicionario['ages']==df_dicionario['ages'].max()]
oldest_atleta = oldest_atleta['name'].tolist()

#países participantes
num_paises = df_dicionario['coutrys'].nunique()



#enviar e-mail yahoo automático
usuario = os.environ.get("YAHOO_USER") 
senha = os.environ.get("YAHOO_PASSWORD")
destinatario = 'pedrocadaluz@outlook.com'
assunto = 'AP2'
mensagem = f'''
i)atletas com mais de 30 anos que conquistaram a medalha de ouro foram {atletas_ouro_30}.
ii)os USA ganharam {num_atletas_eua} medalhas.
iii) O atleta mais velho  que ganhou uma medalha foi o {oldest_atleta} de {age} anos.
iv) Nessa amostra contém {num_paises} países que ganharam medalhas.
'''

