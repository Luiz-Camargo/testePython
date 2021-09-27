import random

#GERADOR DE SENHAS

minusculo = ("abcdefghjklmnopqrstuvwxyz")
maiusculo = ("ABCDEFGHJKLMNOPQRSTUVWXYZ")
numeros = ("0123456789")
simbolos = ("@#$%&*")


soma = minusculo + maiusculo + numeros + simbolos

tamanho = 5
senha = random.sample(soma,tamanho)
print("".join(senha))