# https://wiki.python.org.br/ExerciciosArquivos

# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
# contendo um relatório dos endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:
import time

# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256
# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
#
# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256


def valida_string(valores):
    parte_1 = ''
    parte_2 = ''
    parte_3 = ''
    parte_4 = ''
    count_ponto = 0

    if len(valores) > 15:
        status = '0'
        return status
    else:
        if (valores.startswith('1') or valores.startswith('2') or valores.startswith('3') or valores.startswith('4')
                or valores.startswith('5') or valores.startswith('6') or valores.startswith('7')
                or valores.startswith('8') or valores.startswith('9')):

            for count_valores in range(len(valores)):
                valor_posicao = valores[count_valores]

                if valor_posicao == '.':
                    count_ponto += 1
                    continue

                if count_ponto == 0:
                    parte_1 = parte_1 + valor_posicao
                elif count_ponto == 1:
                    parte_2 = parte_2 + valor_posicao
                elif count_ponto == 2:
                    parte_3 = parte_3 + valor_posicao
                elif count_ponto == 3:
                    parte_4 = parte_4 + valor_posicao
                else:
                    status = '0'
                    return status

            if parte_1.isdigit() and parte_2.isdigit() and parte_3.isdigit() and parte_4.isdigit():
                parte_1 = int(parte_1)
                parte_2 = int(parte_2)
                parte_3 = int(parte_3)
                parte_4 = int(parte_4)

                if (0 < parte_1 <= 255) and (0 <= parte_2 <= 255) and (0 <= parte_3 <= 255) and \
                        (0 <= parte_4 <= 255):
                    status = '1'
                    return status
                else:
                    status = '0'
                    return status
            else:
                status = '0'
                return status

            status = '1'
            return status
        else:
            status = '0'
            return status


def execute():
    inicio = time.time()

    arquivo = open("src/exercise_archive/ip.txt", "r")
    ip_valido = open("src/exercise_archive/ip_valido.txt", "w")
    ip_invalido = open("src/exercise_archive/ip_invalido.txt", "w")
    n_linha = 0

    for linha in arquivo:
        valores = linha.split()

        n_linha = n_linha + 1

        try:
            if valida_string(valores[0]) == '0':
                print('Endereço IP é invalido: {}'.format(valores[0]))
                ip_invalido.writelines(valores[0] + '\n')
                continue
            elif valida_string(valores[0]) == '1':
                print('Endereço IP válido: {}'.format(valores[0]))
                ip_valido.writelines(valores[0] + '\n')
                continue
            else:
                print('Esta string não conseguiu ser validada {}'.format(valores[0]))
        except IndexError:
            print('Endereço IP é invalido: {}'.format(valores))
            ip_invalido.writelines(str(valores) + '\n')

    arquivo.close()
    ip_valido.close()
    ip_invalido.close()

    fim = time.time()
    tempo_gasto = fim - inicio

    print("Função demorou {} segundos para validar {} IPs ".format(tempo_gasto, n_linha))

    return tempo_gasto


if __name__ == '__main__':
    execute()
