#Captura o número de empresas para gerar a nota fiscal conforme necessário
cont = int(input('Quantos relatórios você deseja imprimir? '))

#Variáveis para mostrar os valores finais
totalImp = 0
totalMerc = 0
totalGeral = 0

#Laço de repetição baseado no input que o usuário passou
for item in range(cont):
    #Captura o nome do cliente
    cliente = input('\nNome do cliente ')

    #Captura a quantidade comprada
    q = int(input('Quantidade comprada '))

    #Define o valor unitário do produto
    vu = 4.50

    #Calcula o valor do ICMS
    icms = (q*vu*18/100)

    #Calcula o valor do IPI
    ipi = (q*vu*4/100)

    #Calcula o valor do PIS
    pis = (q*vu*1.86/100)

    #Calcula o valor do COFINS
    cofins = (q*vu*8.54/100)

    #Calcula a soma total dos impostos
    total = (icms + ipi + pis + cofins)

    #Atribui os impostos atuais a soma total
    totalImp = totalImp + total
    totalMerc = totalMerc + (q * vu)
    totalGeral = totalGeral + (q*vu + total)

    #Imprime na tela o nome do cliente e a quantidade de produtos comprados
    print('\nCliente: {} \nQuantidade comprada: {} ' .format(cliente, q))

    #Imprime o valor dos impostos conforme a quantidade comprada
    print('ICMS (18%): {:.2f}; IPI (4%): {:.2f}; PIS (1.86%): {:.2f}; COFINS (8.54%): {:.2f}'.format(icms, ipi, pis, cofins))

    #Imprime o gasto total da empresa
    print('\nTotal: {:.2f} ' .format(q*vu + total))

#Imprime o total de todas as empresas
print('\nTotal impostos: {:.2f}' .format(totalImp))
print('Total mercadorias: {:.2f}' .format(totalMerc))
print('Total geral: {:.2f}' .format(totalGeral))

