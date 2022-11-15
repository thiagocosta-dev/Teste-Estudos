from random import sample

def ordenar(ini, fim, tamanho):
    lista = sample(range(ini, fim), tamanho)
    lista_ordenada = sorted(lista, reverse = True)
    print ("Lista : " +  str(lista))
    print ("Lista ordenada: " +  str(lista_ordenada))



ordenar(0, 50, 10)
ordenar(0, 500, 12)