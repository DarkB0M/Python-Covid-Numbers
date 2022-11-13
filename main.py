from download import CreateTemp,DeathsArchive
from os import kill

log = ['Logs:']

def Start():
    print('Colete os números da covid com Python.')
    print('Essa operação irá consumir espaço até ser terminada, Quer Prosseguir?')
    pergunta = input('[y] [n]   ')
    if pergunta == 'y':
        CreateTemp()
        DeathsArchive()
        
    elif pergunta == 'n':
        kill()

 
Start()


