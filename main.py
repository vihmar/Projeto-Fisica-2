#Constantes
hEV = 4.136e-15
hJ = 6.626E-34
c = 2998e+05
cElementar = 1.602e-19
cR = 1.0974e7
massaEletron = 9.11e-31
e0 = 8.85e-12
energiaInicial = -13.6

#*****Zona de Funções*****
def calculaEnergiaComp(comp):
    energia = (hEV*c)/comp #Calcula o Valor da energia com o comprimento
    return energia #Retorna a conta executada na função

def calculaEnergiaFreq(freq):
    energia = hEV * freq #Calcula o Valor da energia com a Frequência
    return energia #Retorna a conta executada na função

def calculaRaio(n):
    raio = (pow(n,2)) * 5.29e-11 #Calcula o Valor do Raio com a n
    raio *= 1e9
    return raio #Retorna a conta executada na função

def calculaVel(n):
  # 1/e0 * (cargaElementar^2 / (2*n*hEV))
    vel = (1/e0) * ((pow(cElementar,2)) / (2*n*hJ))
  #vel = (1/e0) * (pow(cElementar,2) / (2*n*hEV)) #Calcula o Valor do Raio com base no n
    return vel #Retorna a conta executada na função

def calculaEnergiaCinetica(n):
    energiaCinetica = (13.6) / pow(n,2) #Calcula o Valor da energia Cinetica com base no valor de n
    return energiaCinetica #Retorna a conta executada na função

def calculaEnergiaPotencial(n):
    energiaPotencial = (-27.2) / pow(n,2) #Calcula o Valor da energia Potencial com base no valor de n
    return energiaPotencial #Retorna a conta executada na função

def calculaEnergiaTotal(n):
    energiaTotal = (calculaEnergiaPotencial(n) + calculaEnergiaCinetica(n)) #Calcula o Valor da energia Total com base no valor de n
    return energiaTotal #Retorna a conta executada na função

def calculaCompOnda(n):
    velocidade = calculaVel(n)
    compOnda = hJ / (massaEletron * velocidade)
    compOnda *= 1e+9
    return compOnda # Retorna a conta executada na função

def calculaFoton(nInicial,nFinal):
    energiaNInicial = (-13.6) / pow(nInicial,2)
    energiaNFinal = (-13.6) / pow(nFinal,2)
    energiaFoton = abs(energiaNFinal - energiaNInicial)
    compFoton = (hEV * c) / energiaFoton
    freqFoton = energiaFoton / hEV
    compFoton *= 1e+9
    return compFoton, freqFoton

# calcular tipo de onda utilizando frequência
def calc_tipo_onda(freq):
    tipo_onda = ""
    if(freq < 1e+09):
        tipo_onda = "radio"
    elif(freq >= 1e+09 and freq <= 3e+11):
        tipo_onda = "microondas"
    elif(freq > 3e+11 and freq <= 4.29e+14):
        tipo_onda = "infravermelho"
    elif(freq > 4.29e+14 and freq <= 7.5e+14):
        tipo_onda = "luz visivel"
    elif(freq > 7.5e+14 and freq <= 1e+16):
        tipo_onda = "ultravioleta"
    elif(freq > 1e+16 and freq <= 1e+19):
        tipo_onda = "raio-x"
    elif(freq > 1e+19):
        tipo_onda = "raio gama"
    return tipo_onda

def calculaBalmer(compFoton):
    corLuz = ""
    if(compFoton >= 410.2 and compFoton < 434.1):
        corLuz = "violeta"
    elif(compFoton >= 434.1 and compFoton < 486.1):
        corLuz = "azul"
    elif(compFoton >= 486.1 and compFoton < 656.3):
        corLuz = "verde"
    elif(compFoton >= 656.3):
        corLuz = "vermelha"
    return corLuz

def calculaNF(compFoton):
    absorve = False
    energiaFoton = (hEV * c) / compFoton
    energiaFinal = energiaInicial + energiaFoton
    n = (energiaInicial/energiaFinal)**0.5
    x = round(n)
    diferenca = x - n
    diferenca = abs(diferenca)
    print(x)
    if(diferenca <= 0.01):
      absorve = True

    #absorve = isinstance(x, int)
    return x,absorve

#*****Término da Zona de Funções*****
while True:
    print("\n========================================================\nEscolha uma das opções:")
    print("1 - Calcular energia do fóton com o comprimento de onda")
    print("2 - Calcular energia do fóton com a frequência")
    print("3 - Calcular raio da órbita, velocidade, energia e comprimento de onda com o número quântico")    
    print("4 - Calcular a absorção e emissão de fótons com o número quântico inical e final")
    print("5 - Calcular o espectro de emissão do átomo de hidrogênio")
    print("6 - Retorna se o átomo vai absorver ou não o fóton incidente")
    print("0 - Sair\n========================================================")
    entrada = int(input(":"))# Printa na tela o Menu
    if(entrada == 1):
    #Comprimento
        comp = float(input("\nDigite o comprimento de onda: "))
        result = calculaEnergiaComp(comp)#Salva na variavel result o retorno da função calculaEnergiaComp(comp)
        energiaJoule = result * (1.6e-19)
        print("\nValor da energia em elétron-volt: %.2f eV" % result)#Printa o valor da energia caculado com o comprimento Formatado 
        print("Valor da energia em joule: " , f'{energiaJoule:.2e}', end=" J\n")
    
    elif(entrada == 2):
    #Frequência
        freq = -1
        while(freq < 0.0):
            freq = float(input("\nDigite a frequência: "))
            if(freq < 0.0):
                print("\nErro, a freqência não pode ser negativa")
            
        resultado = calculaEnergiaFreq(freq) #Salva na variavel resultado o retorno da função calculaEnergiaFreq(freq)
        energiaJoule = resultado * (1.6e-19)
        print("\nValor da energia em elétron-volt: %.2f eV" % resultado) #Printa o valor da energia caculado com a frequência Formatado 
        print("Valor da energia em joule: " , f'{energiaJoule:.2e}', end=" J\n")

    elif(entrada == 3):
    #Nível Quantico
        n = 0
        while(n < 1):
            n = int(input("\nDigite o n: "))#Espera uma entrada para o valor de N
            if(n < 1):
                print("\nErro, o n não pode ser menor que 1")#Mensagem de erro ao digitar o número 

        resultado = calculaRaio(n) #Salva na variavel resultado o retorno da função calculaRaio(n)
        print("\nValor do Raio: %.2f nm" % resultado)#Printa o valor da Raio Formatado em notação cientifica

        resultadoVel = calculaVel(n) #Salva na variavel resultadoVel o retorno da função calculaVel(n)
        print("Valor da Velocidade:", f'{resultadoVel:.2e}', end=" m/s\n")#Printa o valor da Velocidade Formatado em notação cientifica

        resultadoCinetica = calculaEnergiaCinetica(n) #Salva na variavel resultadoCinetica o retorno da função calculaEnergiaCinetica(n)
        print("Valor da Energia Cinética: %.2f eV" % resultadoCinetica)#Printa o valor da Energia Cinética Formatado em notação cientifica

        resultadoPotencial = calculaEnergiaPotencial(n) #Salva na variavel resultadoPotencial o retorno da função calculaEnergiaPotencial(n)
        print("Valor da Energia Potencial: %.2f eV" % resultadoPotencial)#Printa o valor da Energia Potencial Formatado em notação cientifica

        resultadoTotal = calculaEnergiaTotal(n) #Salva na variavel resultadoTotal o retorno da função calculaEnergiaTotal(n)
        print("Valor da Energia total: %.2f eV" % resultadoTotal) #Printa o valor da energia total Formatado em notação cientifica

        resultadoCompOnda = calculaCompOnda(n) #Salva na variavel resultadoCompOnda o retorno da função calculaCompOnda(n)
        print("Valor do Comprimento de Onda: %.2f nm" % resultadoCompOnda) #Printa o valor do Comprimento de Onda Formatado em notação cientifica
    
    elif(entrada == 4):
        nInicial = 0
        nFinal = 0
        while(nInicial < 1):
            nInicial = int(input("\nDigite o n inicial: "))
            if(nInicial < 1):
                print("\nErro, o n inicial não pode ser menor que 1")
        while(nFinal < 1):
            nFinal = int(input("\nDigite o n final: "))
            if(nFinal < 1):  
                print("\nErro, o n final não pode ser menor que 1")

        if(nInicial == nFinal):
            print("\nErro, os valores de n inicial e n final não podem ser iguais.")
        # elétron sobe de um nível inferior para um nível superior    
        elif(nInicial < nFinal):
            compFoton, freqFoton = calculaFoton(nInicial,nFinal)
            tipo_onda = calc_tipo_onda(freqFoton)
            print("\nUm fóton do tipo %s foi absorvido" % tipo_onda)
            print("Valor do comprimento de onda do fóton: %.2f nm" % compFoton)
            print("Valor da frequência do fóton", f'{freqFoton:.2e}', end=" Hz\n" )
        # elétron decai de um nível superior para um nível inferior    
        elif(nFinal < nInicial):
            compFoton, freqFoton = calculaFoton(nInicial,nFinal)
            tipo_onda = calc_tipo_onda(freqFoton)
            print("\nUm fóton do tipo %s foi emitido" % tipo_onda)
            print("Valor do comprimento de onda do fóton: %.2f nm" % compFoton)
            print("Valor da frequência do fóton", f'{freqFoton:.2e}', end=" Hz\n" )

    elif(entrada == 5):
        serie = 0
        while True:
            print("\nEscolha o número quântico final de uma das séries abaixo")
            print("1 - Série de Lyman\n2 - Série de Balmer\n3 - Série de Paschen")
            print("4 - Série de Brackett\n5 - Série de Pfund")
            serie = int(input(":"))
            if(serie != 1 and serie != 2 and serie != 3 and serie != 4 and serie != 5):
                print("\nErro, escolha uma das opções válidas")
            else:
                break
                
        nInicial = 0
        # n inicial deve ser pelo menos 2, pois nesse caso ele pode decair para n = 1
        while(nInicial < 2 or nInicial <= serie):
            nInicial = int(input("\nDigite o n inicial: "))
            if(nInicial < 2):
                print("\nErro, o n inicial deve ser no mínimo 2")    
            # a série escolhida não pode ser maior ou igual que o n inicial
            elif(nInicial <= serie):
                print("\nErro, o n inicial não pode ser menor ou igual a série escolhida")
            
        # caso seja a série de Lyman, Paschen, Brackett ou Pfund   
        if(serie == 1 or serie == 3 or serie == 4 or serie == 5):
            compFoton, freqFoton = calculaFoton(nInicial,serie)
            tipo_onda = calc_tipo_onda(freqFoton)
            print("\nUm fóton do tipo %s foi emitido" % tipo_onda)
            print("Valor do comprimento de onda do fóton: %.2f nm" % compFoton)
            print("Valor da frequência do fóton:", f'{freqFoton:.2e}', end=" Hz\n" )
        # caso seja a série de Balmer
        else:
            compFoton, freqFoton = calculaFoton(nInicial,serie)
            if(compFoton >= 410.2):
                corLuz = calculaBalmer(compFoton)
                print("\nUm fóton do tipo luz visível da cor %s foi emitido" % corLuz)
            # caso o comprimento seja menor que 410.2, não é luz visível
            else:
                tipo_onda = calc_tipo_onda(freqFoton)
                print("\nUm fóton do tipo %s foi emitido" % tipo_onda)
                
            print("Valor do comprimento de onda do fóton: %.2f nm" % compFoton)
            print("Valor da frequência do fóton:", f'{freqFoton:.2e}', end=" Hz\n" )

    elif(entrada == 6):
        compFoton = float(input("Entre com o comprimento em metros: "))
        n,absorve = calculaNF(compFoton)
        if(absorve == False):
            print("\nO fóton não foi absorvido pelo átomo")
        else:
            print("\nO fóton foi absorvido pelo átomo")
            print("Número quântico final do átomo: %.0f" % n)

    elif(entrada == 0):
        print("\nPrograma encerrado...")
        break
        
    else:
        print("\nErro, insira uma das opções válidas")
