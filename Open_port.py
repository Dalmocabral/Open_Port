#coding: utf-8
#!usr/din/python

import socket

ip = str(input("Entre com IP ou endereço do site que deseja scannear: "))
ports = []
x = int(input("Digite a quantidade de portas que deseja scannear: "))

i = 0

while i < x:
	ports.append(int(input("Digite a porta: ")))
	i += 1

for port in ports:
	cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cliente.settimeout(0.2)
	conexao = cliente.connect_ex((ip, port))
	print conexao