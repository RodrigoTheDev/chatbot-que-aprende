#ChatBot que aprende
#Criado por @RodrigoTheDev [link para o github: https://github.com/RodrigoTheDev]
#Se você gostou desse código e quer utilizá-lo em algum projeto, por favor, deixe os créditos.
import json

#importando o dicionário do arquivo .json
# [ATENÇÃO: SE É A SUA PRIMEIRA VEZ RODANDO O PROGRAMA, E VOCÊ NÃO TEM O ARQUIVO 'ChatBotFiles.json, DEIXE A LINHA ABAIXO COMO UM COMENTÁRIO]
vocabulario = json.load(open('ChatBotFiles.json'))

reset = 1

while True:
    talk = input('digite>> ')
    #Caso o programa já conheça o que você está digitando, ele dará a resposta
    if talk in vocabulario.keys():
        print('BotBob:',vocabulario[talk])
    else:
        #Caso contrário, ele irá pedir para você ensinar a resposta
        ans = input('///adicione a resposta: ')
        vocabulario[talk] = ans
        print('====comando aprendido!====')
    j = json.dumps(vocabulario)

    with open('ChatBotFiles.json', 'w') as f:
        f.write(j)
        f.close()