# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
# da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# latas de 18 litros, que custam R$ 80,00
# galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga 
# e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math

metros = 100
tinta_necessaria =  metros/6

# Info tinta
lata_litro = 18
galao_litro = 3.6
lata_preco = 80
galao_preco = 25

# Lata
qtd_lata = math.ceil(tinta_necessaria/lata_litro,)
preco_lata_total = qtd_lata*lata_preco
print(f"Apenas lata {preco_lata_total} reais")

# Galão
qtd_galao = math.ceil(tinta_necessaria/galao_litro)
preco_galao_total = qtd_galao*galao_preco
print(f"Apenas galão {preco_galao_total} reais")

# Misturado
tinta_necessaria = tinta_necessaria*1.1
# print(tinta_necessaria)

if tinta_necessaria > lata_litro:
    qtd_latas_mix = round(tinta_necessaria/lata_litro)
    # print(f"Latas pra misturar {qtd_latas_mix}")

    qtd_resto_tinta = tinta_necessaria%lata_litro
    qtd_galao_mix = math.ceil(qtd_resto_tinta/galao_litro)
    # print(f"Galões pra misturar {qtd_galao_mix}")

    preco_galao_total_mix = qtd_galao_mix*galao_preco
    preco_latas_total_mix = qtd_latas_mix*lata_preco

    preco_mix = preco_galao_total_mix + preco_latas_total_mix
    print(f"misturado {preco_mix} reais")

# Comparação
if tinta_necessaria > lata_litro:
    if preco_lata_total < preco_galao_total and preco_lata_total < preco_mix:
        print(f"O mais barato é compra as latas -> {qtd_lata} de latas por {preco_lata_total} reais")
    elif preco_galao_total < preco_lata_total and preco_galao_total < preco_mix:
        print(f"O mais barato é compra os galões -> {qtd_galao} de galões por {preco_galao_total} reais")
    else:
        print(f"O mais barato é compra os galão com latas misturados -> {qtd_galao_mix} de galões e {qtd_latas_mix} de latas por {preco_mix} reais")
else:
    if preco_lata_total < preco_galao_total:
        print(f"O mais barato é compra as latas -> {qtd_lata} de latas por {preco_lata_total} reais")
    else:
        print(f"O mais barato é compra os galões -> {qtd_galao} de galões por {preco_galao_total} reais")