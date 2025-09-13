#Funções para conversão de temperatura

def celsius_farenheit(celsius):
    """Função para converter celsius em farenheit"""

    #Aqui eu coloco a fórmula de conversão de celsius para ferenheit
    faren = 9 / 5 * celsius + 32
    return faren

def farenheit_celsius(farenheit):
    """Função para converter farenheit em celsius"""

    #Aqui eu coloco a fórmula de conversão de farenheit para celsius
    cels = (farenheit - 32) * 5 / 9
    return cels

def principal(opc_cels_faren, digt_var, temp_var):
    """Função principal do programa que determina qual será a conversão"""

    #Aqui eu crio um bloco try-except para a função principal
    try:

        #Aqui eu pego o valor digitado e converto para float
        valor = float(digt_var.get())

        #Aqui eu verifico se a opção de convertão é True ou False
        if opc_cels_faren.get():

            #Aqui eu chamo a função de conversão celsius-farenheit
            final = celsius_farenheit(valor)

        else:

            #Aqui eu chamo a função de conversão farenheit-celsius
            final = farenheit_celsius(valor)

        #Aqui eu coloco o resultado formatado no Label de resultado
        temp_var.set(f'{final:.2f}')

    #Aqui eu termino o bloco try-except com a validação de dados.
    except ValueError:
        temp_var.set("Digite um número")