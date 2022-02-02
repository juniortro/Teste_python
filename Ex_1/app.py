import json
import sys
response = 0

print(sys.version)

while response != '3':
    print('1- Read configuration \n2- Write configuration \n3- Exit')
    response = input()

    def modifyFile(operation):
        if operation == '1':
            try:
                f = open('config.json')
                with open('config.json', 'r') as json_file:
                    data = json.load(json_file)
                    print(data)
                f.close()
            except:
                print('O arquivo não contem informações!')

        elif operation == '2':
            serverName = input('Informe o nome do servidor: ')
            serverIp = input('Informe o IP do servidor: ')
            serverPassword = input('Informe a senha do servidor: ')

            jsonData = {
                'server_name': serverName,
                'server_ip': serverIp,
                'server_password': serverPassword
            }

            print('Dados salvos com sucesso!\n',jsonData)

            with open('config.json', 'w') as json_file:
                data = json.dump(jsonData, json_file, indent=4)

    modifyFile(response)
