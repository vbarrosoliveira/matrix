
import numpy as np
#exercice
#Ecrire une fonction que calcule le produit d'un nimbre quelquonque des matrices


E = [[9, 0, 0],[0,0,1],[0,0,1]]
F = [[1, 0, 0],[0,1,0],[0,0,1]]
G = [[1, 0, 0],[0,1,0],[0,0,1]]
H = [[1, 0, 0],[0,1,0],[0,0,1]]



#début de la fonction
# on va créer deux  boucles
# la première calculera le produit des deux premières matrices dans *args
#la deuxieme boucle fera le reste des produits, récursivement

def produto_geral_matrizes(*args):

    #ici la fonction nos avertira que nous en avons besoin d'au moins deux  matrices:
    
    if len(args)<2:
        
        result="Numero insuficiente de matrizes! Entre pelo menos duas matrizes."
        return (result)
    #Sinon le else sera efectué    
    else:   
        E,F=args[0],args[1]  #pour simplifier on appellera les deux premières matrices E et F respectivement
        EF = []              #liste vide où nous allons créer le produit matriciel de E et F 

        #debut du premier loop

        #fixons une ligne de la matrice E  
        for i in range(len(E)):      #dans l'example i=0,1,2 

                # produit scalaire ligne E x colonne F
            
                for j in range(len(F[0])):#dans l'exemple j=0,1,2 

                    # debut duproduit scalaire ligne E x colonne F
                    coef=0
                
                    for k in range(len(F)):#k=0,1,2 dans l'ex
                        coef += E[i][k] * F[k][j]#coef cest le produit scalaire de ligne E pour colonne F
                        k=k+1
                    EF.append(coef)#on ajoute la valeur de coef a la liste vide EF

                    #toujours avec la première ligne de E fixee, nous parcourons les autres colonnes de F
                    j=j+1

                #maintenant on change la ligne de E et on refait tout le processus    
                i=i+1
        result=np.reshape(EF, (len(E), len(F[0])))#Liste EF organisée sous forme de matrice
        #fin du premiere loop

       
        #maintenant on va faire le produit de la matrice EF (que l'on appelle résultat) par G (=troisième élément de la liste des matrices)

        #debut du deuxieme loop
    
        for a in range(2,len(args)):
            primeira_matriz=result    #quand a=2 la première matrice est EF et la deuxième matrice est G (la troisième matrice de la liste)
            segunda_matriz=args[a]

             #à partir d'ici c'est la même idée d'avant

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
            result= np.reshape(produto_lista, (len(primeira_matriz), len(segunda_matriz[0]))) # a=2 c'est le produit EFG
            a=a+1 

            #fin du deuxieme  loop
        return(result)        
print(produto_geral_matrizes(E,F))        

    
          
    


   

    
#testando com 6 matrizes
E = [[1, 0, 0],[0,0,1],[0,0,1]]
F = [[1, 0, 0],[0,0,1],[0,0,1]]
G = [[1, 0, 0],[0,0,1],[0,0,1]]
H = [[1, 0, 0],[0,0,1],[0,0,1]]
I = [[1, 0, 0],[0,0,1],[0,0,1]]
J = [[0],[0],[2]]

#criamos uma lista com as 6 matrizes
listam_seis=[E,F,G,H,I,J]
print(produto_geral_matrizes(E,F,G,H,I,J))




