# https: // wiki.python.org.br / EstruturaSequencial

# 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um
# link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando
# este link (em minutos)

print()
tamanho_arquivo_MB = float(input("Digite o tamanho do arquivo para donwload em MB: "))
velocidade_mbps = float(input("Digite a velocidade da internet em Mbps: "))

tamanho_arquivo_mbps = tamanho_arquivo_MB * 8
tempo_segundos = tamanho_arquivo_mbps / velocidade_mbps
tempo_minutos = int(tempo_segundos / 60)
resto_s = tempo_segundos - 60
while resto_s >= 60:
    resto_s = resto_s - 60

print("Duração: {} segundos\nDuração: {} minutos e {} segundos" .format(tempo_segundos, tempo_minutos, int(resto_s)))