# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:16:57 2021

@author: Saadia Bayou
"""


A=[[1,2,0],[3,4,7],[5,6,9]]
v=[1,0,2]

B=[[1,2,0],[3,4,7]]

M1=[[1,2,0],[3,4,7]]
M2=[[3,6,0],[8,0,2]]

C=[[1,2,3],[4,5,6],[7,8,9]]


print("\n- Déterminer la dimension d'une matrice : ")

def dimMat(M):
    """ Donne la dimension d'une matrice"""
    nl=len(M) # Nombre de lignes
    print("\nNombre de lignes :",nl)
    for i in range(len(M)):
        nc=len(M[i]) # nombre de colonnes
    print("Nombres de colonnes : ", nc)
    if nc==nl :
        print("Matrice carrée") 
    return "M(nl,nc)="+"M("+str(nl)+"x"+str(nc)+")"

print("Dimension matrice : ",dimMat(A))
print("Dimension matrice : ",dimMat(B))


print("\n- Afficher une matrice nxn : ")

def AffMat(M):
    return M
print("\nLa matrice M égale , M=", AffMat(A))


print("\n- Lire une matrice nxn :")

def LireMat(M):
    """Affiche le contenu d'une matrice """
    print("\nContenu de la matrice :")
    for i in range(len(M)):
        print("\nVecteur ligne:",i)
        print("M[",i,"]=",M[i],"\n")
        for j in range(len(M[i])):
            print("coefficient:", i,",",j)
            print("M[",i,"][",j,"]=",M[i][j])
# Pas de return, fonction qui affiche le contenue d'une matrice
            
LireMat(A)
#aff_mat(B)
   
print("\n- Ajouter deux matrices :")

def sommeMat(A,B):
    """ Aditionne deux matrices ,somme coefficient par coefficient """
    v=[] # vecteur ligne
    M=[] # Matrice
    
    for i in range(len(A)): # On parcourt les lignes
        for j in range(len(A[i])): # On parcourt les colonnes 
            c= A[i][j]+B[i][j] # On somme les coefficients      
            v.append(c) # On stocke les coefficient dans un vecteur
        M.append(v) # On strocke les vecteurs dans une matrice
        v=[] # On vide le vecteur avant de passer à la ligne suivante 
    return  M # On affiche la matrice

print("\nLe resultat somme des matrices, M=",sommeMat(M1,M2))


print("\n- Multiplier un vecteur par une matrice :")
def multVectMat(M,v):
    """ Multiplie un vecteur et une matrice"""
    s=0  
    u=[]
    for i in range(len(M)):
        for j in range(len(M[i])):
            s+=M[i][j]*v[j]
        u.append(s)
        s=0
    print("u=",u)
    
multVectMat(C,v)
           

print("\n -Multiplier une matrice par une matrice:") 

def MultMat(A,B):
    v=[]
    M=[]
    for i in range(len(A)):
        for j in range(len(A[i])):
            c=A[i][j]*B[i][j] # Coefficients matrice 
            v.append(c)
        M.append(v)
        v=[]
    return M

print("\nLe résultat multiplication de deux matrices : M=",MultMat(M1,M2))
