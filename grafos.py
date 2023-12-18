import networkx as nx
import pandas as pd


def escolha_Arquivo(escolha):
    switcher ={
        1:"./grafos/trab2grafo_1.txt",
        2:"./grafos/trab2grafo_2.txt",
        3:"./grafos/trab2grafo_3.txt",
        4:"./grafos/trab2grafo_4.txt",
        5:"./grafos/trab2grafo_5.txt",
    }

    url_path = switcher.get(escolha, "Grafo invalido")

    df = pd.read_csv(url_path , sep ='\t',names=["Grafo"])
    csv_in_numpy = df['Grafo'].to_numpy()
    Lista1 = TransformaNPEmLista(csv_in_numpy)

    # Criando Vertice(V) e Aresta(A)
    V,A=Criar_Vertice_Aresta(Lista1)


    G=nx.Graph()
    ### add Vertice no Grafo
    G.add_nodes_from(V)
    ### Add Aresta no Grafo
    G.add_weighted_edges_from(A)

    return G


def TransformaNPEmLista(arrayDi):
    l=[]
    #Numero_de_linhas=46824
    
    ListaNP =list(arrayDi)
    ultimo=ListaNP[-1]                      ## 11616 29809
    ultimoIndex=ListaNP.index(ultimo)
    #print("ultimo elemento",ultimo,"p",ultimoIndex)
    Numero_de_linhas =int(ultimoIndex)+1    ##  ultimo Index = 46824 +1
    
    for i in range(1,Numero_de_linhas):
        #print(arrayDi[i])
        string = str(arrayDi[i])
        #print(string)
        lista = string.split()
        l.append(lista)
    return l



def Criar_Vertice_Aresta(ll):
    lista_Aux=[]
    lista_Aux2=[]
    for i in range(len(ll)):
        
        ll[i][2]=int(ll[i][2])
        lista_Aux.append(ll[i][0])
        lista_Aux2.append(tuple(ll[i]))
    Vertice=set(lista_Aux)
    Aresta=lista_Aux2
    return Vertice,Aresta


def dijkstra_caminho(G,node1, node2):
    ### retorna aresta negativas
    e_negativo=([(u, v,d) for (u, v, d) in G.edges(data=True) if float(d["weight"]) < 0.0])    
    print()
    if e_negativo==[]:
        print("Sem pesos negativos")
        if(int(node2) <= len(G.nodes)):
            print("O menor caminho entre {} e {} é: {}" .format(node1, node2, nx.dijkstra_path(G,node1,node2,weight='weight')))
            print("O custo para ir do vértice {} ao vértice {} é de {}" .format(node1, node2, nx.dijkstra_path_length(G,node1,node2)))
        else:
            print("Este grafo não possui este tamanho")
    else:
        print("Não é possível usar este método, pois há arestas com pesos negativos")
    print()


