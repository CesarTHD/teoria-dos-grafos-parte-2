from  grafos import *


G = escolha_Arquivo(5)

#print(G.nodes.data())
#print(G.edges.data())

dijkstra_caminho(G,'1','10')
dijkstra_caminho(G,'1','100')
dijkstra_caminho(G,'1','1000')
dijkstra_caminho(G,'1','10000')