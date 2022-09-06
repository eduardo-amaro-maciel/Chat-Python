import socket
import os
import colorama
import logging

from colorama import Fore, Back, Style

colorama.init(autoreset=True)

logging.basicConfig(filename="logs.log", level=logging.INFO, format="%(asctime)s | %(message)s")

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8080))

servidor.listen()
cliente, end = servidor.accept()

os.system('cls' if os.name == 'nt' else 'clear')

print('Digite (sair) para terminar o chat')

terminado = False

while not terminado: 

    msg = cliente.recv(1024).decode('utf-8')

    if msg == 'sair':
        print(Fore.RED + 'Cliente saiu da conversa')
        terminado = True
    
    else: 
        print(Fore.CYAN + 'User: ' + msg)

    
    inputServer = input('User: ')

    logging.info(f'SERVIDOR: {inputServer}') 

    cliente.send(inputServer.encode('utf-8'))

cliente.close()
servidor.close()
