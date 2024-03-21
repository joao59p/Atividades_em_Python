"""CRIANDO UM SISTEMA BANCARIO"""
#OPERAÇÕES DEPOSITO,SAQUE E EXTRATO
#APENAS 1 UNICO USUARIO
#LIMITE DE 3 SAQUES DIARIOS  COM LIMITE MAX DE 1500 REAIS E POR SAQUE O LIMITE E 500 REAIS
#EXIBIR MENSAGEM CASO FALTA SALDO NA CONTA
# SAQUES DEVEM SER ARMAZENADOS EM UMA VARIAVEL E EXIBIDO POSTERIOMENTE
#EXTRATO ESSA OPERAÇÃO DEVE LISTA TODOS OS SAQUES E DEPOSITOS REALIZADOS NA CONTA
#EXTRATO DEVE IMPRIMIR TAMBÉM O SALDO AO FINAL DA TELA FORMATO R$ XXXX.XX

#importações
from time import sleep

#VARIÁVEIS

menu = f"""\r
{'#' * 10} Bem-vindo ao seu Banco {'#' * 10}
        o que você deseja fazer Hoje ?     
    
Depositar [D] 
Extrato   [E]
Sacar     [S]
Sair      [Q]

{'#' * 44}
"""
extrato = ""

saldo = 0
quantidade_de_saque = 0 

#CONSTANTES 
LIMITE = 500.00
LIMITE_SAQUES = 3

#INICIANDO O SISTEMA 
while True:

    opcao = input(menu).upper()

    match opcao:

        #AÇÃO DE DEPOSITO
        case "D":

                valor_para_deposito = float(input("\n\rInforma o valor a ser depositado:\n=> R$ "))
                
                if (valor_para_deposito >= 0):

                    saldo += valor_para_deposito 
                    extrato += f"\nDeposito: R$ {valor_para_deposito:.2f}"
                    
                    print(f"Valor depositado com sucesso.")
                    sleep(2)

                else:
                    print(f"Operação falhou. Favor informar um valor válido")
                    sleep(2)

        #AÇÃO DE EXTRATO
        case "E":
            
            #IMPRIMINDO DEPOSITOS E SAQUES
            print(f"{'#' * 18} EXTRATO {'#' * 18}")     
            print( "Não existem transações no périodo" if not extrato else extrato)
            
            #IMPRIMINDO SALDO
            print(f"SALDO:R$ {saldo:.2f}\n{'#' * 44}" )
            sleep(6)
        
        #AÇÃO DE SAQUE
        case "S":

                valor_para_saque = float(input("\n\rFavor informa o valor a ser sacado\n=> R$ "))
                
                #VERIFICAÇÕES
                verificar_limite =  valor_para_saque > LIMITE

                verificar_limite_saque = quantidade_de_saque == LIMITE_SAQUES

                verificar_saldo =  saldo < valor_para_saque

                #COMPARANDO   
                if(verificar_limite):
                        print(f"Erro na operação. Seu valor de saque solicitado e maior que seu limite.")
                    
                elif(verificar_limite_saque):
                        print(f"Erro na operação. Seu limite de saque diário foi atingindo.")

                elif(verificar_saldo):
                        print(f"Erro na operação. Seu saldo na conta não é insuficiente.")

                elif(valor_para_saque > 0):
                        saldo -= valor_para_saque 
                        quantidade_de_saque += 1 
                        extrato += f"\nSaque: R$ {valor_para_saque:.2f}"

                        print(f"Valor sacado com sucesso.")

                else:
                         print("valor informado é inválido, favor tentar novamente.")

                sleep(3)

        #AÇÃO DE SAIR DO SISTEMA
        case "Q":

            print("\nObrigado por usar nosso sistema, volte sempre.")
            sleep(2)
            break

        #AÇÃO DE ERRO CASO O CLIENTE TENTE OUTRA OPÇÃO 
        case _:

            print("Por favor, informe uma opção válida do menu !!!.")
            sleep(2)
