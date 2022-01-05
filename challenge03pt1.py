def get_columns(lista):
    length = len(lista[0]) #lenght determina a "largura" da lista
    conc = '' #variável vazia para armazenar a concatenação dos números da coluna
    lista1=[] #lista1 é a lista de números de cada coluna
    for i in range(length): #loop para percorrer os subitens de um item
        for item in lista: #loop para percorrer todos os itens de uma lista
            conc += item[i] #concatenando todos os números da coluna
        lista1.append(conc) #adicionando todos os itens da coluna na lista1
        conc='' #conc vazia para zerar a variavel após o loop, senão zerada a conc ficará como todos os valores acumulados, mas não se preocupe os valores antes calculados já foram salvos em forma de item da lista1
    return lista1 #retorna uma lista com os números de cada coluna, onde cada item da lista é a cada coluna
    
    

with open('input.txt','r') as file: #abrir o arquivo com o input
    lista=[] #lista vazia para depois populá-la com o loop
    for line in file: #loop para percorrer cada linha do input
        line = line.strip('\n') #tirar a quebra de linha de cada linha
        lista.append(line) #adicionar cada linha como um item na lista
    colunas = get_columns(lista) #chamada da função e váriavel para obter os números de cada coluna
    bits='' #variável vazia para armazenar a concatenação de cada bit mais repetido de cada coluna
    for coluna in colunas: #percorrer cada colunas da lista de colunas
        cont = coluna.count('0') #contar quantos zeros tem na coluna
        bit='' #variavel vazia para representar o bit
        if cont>len(lista)/2: #se o contador tiver mais zeros que a metade da "altura" da lista, haverá mais "zeros" que "um's" na coluna
            bit='0' #ou seja, o bit é igual a zero
            bits += bit #concatenar os bits para depois convertê-lo em decimal
        else:
            bit='1' #caso contratrio o bit será um
            bits += bit #concatenar os bits para depois convertê-lo em decimal
    gamma = (int(bits,2))  #conversão dos bits em numero decimal(nativo do python), onde o primeiro argumento são os bits e o segundo arg é a base do número, no caso 2 o que representa um número binário
    
    bitsy='' #variável vazia para armazenar a concatenação de cada bit menos repetido de cada coluna, ou seja, o oposto do feito anteriormente
    for coluna in colunas: #loop para percorrer todas as colunas
        cont = coluna.count('1') #contar quantos "um's" tem em cada coluna
        bit='' #variável vazia para armazenar o valor do bit
        if cont>len(lista)/2: #se o contador tiver menos "um's" que a metade da altura da coluna, haverá mais "zero's"
            bit='0' #ou seja, o bit é igual a zero
            bitsy += bit #concatenar os resultados obtidos
        else:
            bit='1' #caso contrário o bit será um
            bitsy += bit #concatenar os resultados obtidos
    epson = (int(bitsy,2)) #conversão do bitsy obtido para número decimal
    result = gamma * epson #resultado para a questão seria a multiplicação dos dois índices

print(result) #printa o result