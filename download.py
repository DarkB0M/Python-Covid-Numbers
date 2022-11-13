import gzip
from os import mkdir
from urllib import request

from pandas import read_csv

import main

# Cria a pasta temp para colocarmos os arquivos CSV da COVID

def CreateTemp():
    mkdir('temp')
    main.log.append('Create Temp Archive /n')

def DeathsArchive():
    request('https://data.brasil.io/dataset/covid19/obito_cartorio.csv.gz','temp/obito.csv.gz')
    # Arrumar
    with gzip.open('obito.csv.gz', 'rb') as f:
        file_content = f.read()
        arquivo = open('temp/death.csv', 'w+',)

        arquivo.write(str(read_csv('temp/death.csv')))
