import download
from os import kill

log = ['Logs:']

def Start():
    print('Colete os números da covid com Python.')
    print('Essa operação irá consumir espaço até ser terminada, Quer Prosseguir?')
    pergunta = input('[y] [n]   ')
    if pergunta == 'y':
       download.CreateTemp()
       download.DeathsArchive()
        
    elif pergunta == 'n':
        print("A Operação sera cancelada! ")
        kill()

 
if __name__ == '__main__':
    Start()


