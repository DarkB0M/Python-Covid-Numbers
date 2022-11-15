import gzip
from os import mkdir,rmdir
import json
from pandas import read_csv,DataFrame
from time import sleep
import main
import wget



# Cria a pasta temp para colocarmos os arquivos CSV da COVID

def CreateTemp():
    mkdir('temp')
    main.log.append('Create Temp Archive /n')

# Elimina a pasta temp quando terminamos os processos 
def EliminateTemp():
    rmdir('temp/')
    main.log.append('Eliminate Temp Archive')

# Cuida do arquivo DeathCSV e descompacta
def DeathArquive():
    with open('url.json',encoding="utf-8") as f:
        dados = json.loads(f)
    
    fetch = wget.download(dados["CasoCSV"],"temp/caso.csv.gz")
    with gzip.open("temp/caso.csv.gz") as unzip:
        archive = open("temp/caso.csv").write(unzip)

    readCSV = str(read_csv(archive))
    print("em 10 segundos aparecera os dados")
    if readCSV == "":
        print("No Content in File")
    else:
        sleep(10)
        print(DataFrame(readCSV))
    
