import socket
import os
import colorama
import logging

from colorama import Fore, Back, Style

colorama.init(autoreset=True)

logging.basicConfig(filename="logs.log", level=logging.INFO, format="%(asctime)s | %(message)s")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 8080))

os.system('cls' if os.name == 'nt' else 'clear')

print('Digite (sair) para terminar o chat')

terminado = False

while not terminado:

    inputUser = input('User: ')

    logging.info(f'CLIENTE: {inputUser}') 

    cliente.send(inputUser.encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')

    if msg == 'sair':
        print(Fore.RED + 'Servidor fechado')
        terminado = True

    else: 
        print(Fore.GREEN + 'Servidor: ' + msg)

    
cliente.close()
