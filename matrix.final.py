

# Produit de matrices
# uma funcao que faca o produto de um numero qq de matrizes


#E = [[9, 0, 0],[0,0,1],[0,0,1]]
#F = [[1, 0, 0],[0,1,0],[0,0,1]]
#G = [[1, 0],[0,1],[0,0]]
#H = [[1],[0]]
#I=[[1,1,2,2]]

###########################################

# inicio da funcao

# criaremos dois grandes loops

# o primeiro calculara o produto das duas primeiras matrizes da lista

# o segundo fara o restante dos produtos ,de forma recursiva

###############################

def produto_geral_matrizes(*args):

    # se entrarmos apena uma matriz ele vai avisar que precisamos de pelo menos duas:
    
    if len(args)<2:
        
        result="Numero insuficiente de matrizes! Entre pelo menos duas matrizes."

        return (result)

    # se entrarmos duas ou mais matrizes :   
       
    E,F=args[0],args[1]    # pra facilitar chamaremos as duas primeiras matrizes de E e F respectivamente

    EF = []                 # lista vazia onde criaremos o produto matricial das duas primeiras matrizes da lista 

    # inicio do primeiro grande loop

    # fixamos uma linha de E

    for i in range(len(E)):                      # i=0,1,2 no ex
        
        # fixamos uma coluna de F
            
        for j in range(len(F[0])):               # j=0,1,2 no ex

            # fazemos o produto escalar linha E x coluna F

            coef=0
                
            for k in range(len(F)):              # k=0,1,2 no ex

                coef += E[i][k] * F[k][j]        # coef eh o produto escalar da linha de E pela coluna de F

                k=k+1

            EF.append(coef)                       # colocamos o valor na lista vazia 

            # ainda com a primeira linha de E fixada percorremos as outras colunas de F

            j=j+1

        # agora trocamos a linha de E e refazemos todo o processo 
           
        i=i+1

    ########################################################################


    # EF  eh uma lista so, com 9 elementos.agora vamos organiza-la no formato lista de listas

    # de acordo com as regras de produto matricial EF deve ter dimensao 3 (=num de linhas de E)por 3 (num de col de F)

    # portanto no exemplo ,EF eh uma lista com 3 listas

    # usando o exemplo para explicar a ideia do proximo loop:
     
    # quando row=0 o loop de dentro pegara os 3 primeiros elementos (elementos nas posicoes 0,1 e 2)
    #da lista EF e criara uma lista (lista_base)


    # observe que ,no final,o loop de dentro limpa a lista_base e recomeca o precesso.
    # por isso criamos linha_EF para receber este tres elementos de forma defiitiva
    # e nao serem apagados no final do loop

    # finalmente anexamos esta lista com tres elementos a lista final,chamada result

    # quando row=1 o loop de dentro pegara os PROXIMOS 3  elementos (elementos nas posicoes 3,4 e 5)
    # da lista EF e criara novamente a lista_base, trocara os zeros de linha_EF por estes tres elementos
    # e os anexara a result.neste momento a lista result tem duas listas.

    # e assim por diante

    ##########################################################################

    # inicio

    result=[] #no final result sera uma lista de listas      #esta coluna explica o primeiro loop no exemplo:

    for row in range(len(E)):                                #no ex:fixe row=0

        lista_base=[] #lista vazia

        linha_EF=[0]*len(F[0]) #lista de zeros

        for col in range(len(F[0])):                         #no ex:para col=0,1,2,        
                                                              
            lista_base.append(EF[col + row * len(F[0])])     #no ex:pegue os elementos de posicao 0,1,2 de EF e construa lista_base

            linha_EF[col]=EF[col + row * len(F[0])]          #no ex:substitua os zeros de linha_EF por estes elementos 

        result.append(linha_EF)                              #no ex:anexe a lista_EF a result

        lista_base.clear()                                   #limpe a lista_base para recomecar

    #final  

    #######################################################
        
    #final do primeiro grande loop

    #agora faremos o produto da matriz EF (que chamamos result) por G (=terceiro elemento da lista de matrizes)

    ###############################################

    #inicio do segundo grande loop
    
    for a in range(2,len(args)):                                            

        primeira_matriz=result     # quando a=2 a primeira matriz eh EF 

        segunda_matriz=args[a]     # quando a=2 a segunda matriz eh G(a terceira matriz da lista)


        # a partir daqui eh a mesma ideia do primeiro loop pois eh o produto de duas matrizes

        # inicio do produto de matrizes

        produto_lista=[]

        

        for c in range(len(primeira_matriz)):

            
            for d in range(len(segunda_matriz[0])):

                coeficiente=0
                
                for e in range(len(segunda_matriz)):

                    coeficiente+=primeira_matriz[c][e] * segunda_matriz[e][d]

                    e=e+1

                produto_lista.append(coeficiente)

                d=d+1

            c=c+1

        # fim do produto de matrizes

        # no exemplo,quando a=2, produto_lista (=EFG) sera uma lista com 6 elementos

        ############################################################

        # agora definiremos duas dimensoes importantes:alpha e beta de maneira recursiva (ainda estamos dentro do loop em a)

        # no ex:

        # quando  multiplicamos EF por G, alpha=numero de linhas da matriz EF e beta=num de colunas de G

        #  quando multiplicamos EFG por H, alpha=numero de linhas da matriz EFG e beta=num de colunas de H

        #e assim por diante

        # alpha e beta serao importantes mais abaixo na hora de organizar a lista de listas no formato matricial 
        # padrao ,com linhas e colunas
            
        alpha,beta=len(primeira_matriz),len(segunda_matriz[0])

        ####################################################################

        # novamente organizamos produto_lista em formato lista de listas, que chamaremos de result

        # mesma ideia de antes

        # inicio

        result=[]

        for row in range(len(primeira_matriz)):

            lista_base=[] #lista vazia

            linha_terceira_matriz=[0]*len(segunda_matriz[0]) #lista de zeros

            for col in range(len(segunda_matriz[0])):

                lista_base.append(produto_lista[col + row * len(segunda_matriz[0])])

                linha_terceira_matriz[col]=produto_lista[col + row * len(segunda_matriz[0])]

            result.append(linha_terceira_matriz) # 

            lista_base.clear()

        # final 

        a=a+1      #no proximo loop em a teremos a=3,primeira matriz=EFG e segunda matriz=H

        

    #final do segundo grande loop

    ################################################
    
    # neste momento, no ex, result eh uma lista de listas que representa o produto EFGHI

    # o proximo loop organiza result no formato matricial padrao (com linhas e colunas)

    # explicaremos usando o exemplo onde o produto final eh EFGHI de dimensao 3 por 4 (3 linhas,4 colunas)

    # aqui serao importantes alpha e beta. alpha sera 3 e beta sera 4

    # por isso alpha e beta foram calculados de maneira recursiva (para sabermos a dimensao da matriz final)

    # na primeira linha  eu transformo result numa lista so

    # quando row=0 o loop de dentro pegara os 4 primeiros elementos de result e cria a lista linha_result

    # imprime esta lista

    # limpa esta lista

    # e pega os PROXIMOS 4 elementos de result para recomecar o processo

    # e assim vai imprimindo a lista, de 4 em 4 elementos ate termos 3 linhas


    ################################################

    result=sum(result,[])       # transformo result numa lista so   
    

    print('Resultado final em formato matricial')

    print()

    print('M=')

    linha_result=[]               # crio uma lista vazia
    
    for row in range(alpha):      # quando row=0 o loop de dentro pegara os 4 primeiros elementos de result e cria a lista linha_result

        for col in range(beta):

            linha_result.append(result[col + row * beta ])

        print(linha_result)

        linha_result.clear()

    print()    

    print("(numero de linhas de M, numero de colunas de M)=")

    result= alpha ,beta 

    return result      

    #agora vamos testar   

    
          
    


   

    




#############################################


#exercicio:organizar a lista de valores entre 0 e 100 em ordem crescente ou decrescente 

#parametros da funcao:lista e ordem

#ordem=1 significa decrescente

#ordem!=1 significa crescente

#########################################################




#inicio da funcao

def sort(lista,ordem=1):

    a=0

    lista_local=lista.copy()        # copiamos a lista dentro da funcao para poder modifica-la

    lista_final=[]                  #  criamos uma lista vazia


    if ordem ==1:                  #  ordem decrescente

        #inicio do loop em a

        while a<len(lista_local):  #  fixamos o  primeiro termo da lista_local.
            
            #inicio do loop em b.este loop calcula o maximo da lista_local assim como sua posicao

            b=0

            posicao_max=0

            max=0

            while b < len(lista_local):

                if lista_local[b]>max:

                    max=lista_local[b]

                    posicao_max=b

                b=b+1

            #fim do loop em b

            lista_final.append(max)      # colocamos este maximo em lista_final

            lista_local[posicao_max]=0   # trocamos o valor maximo por 0 em lista_local   
            
            a=a+1                        # e voltamos a calcular o proximo maximo da lista_local

        #fim do loop em a  

        #quando o contador 'a' percorrer toda a lista,ela estara organizada em ordem decrescente.

    else:#ordem crescente

        while a<len(lista_local):#fixamos o  primeiro termo da lista_local.

            #inicio do loop em b.este loop calcula o minimo da lista_local assim como sua posicao
            
            b=0

            posicao_min=0

            min=100

            while b<len(lista_local):

                if lista_local[b]<min:

                    min=lista_local[b]

                    posicao_min=b

                b=b+1

            #fim do loop em b

            lista_final.append(min)         #  colocamos este minimo em lista_final

            lista_local[posicao_min]=100    #  trocamos o valor minimo por 100 em lista_local   
            
            a=a+1                           #  e voltamos a calcular o proximo minimo da lista_local
          
        #quando o contador 'a' percorrer toda a lista,ela estara organizada em ordem crescente.

    return lista_final 

  #imprimir a lista organizada de acordo com e escolha do parametro ordem 

#fim da funcao
 
