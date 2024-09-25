# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z5vdTSfRAdkcD8sI8UmcpqA6WkB25Zif
"""

import numpy as np #Importando as bibliotecas necessárias
from sklearn.cluster import KMeans

#Matriz com as filmes assistidos
filmes_assistidos = np.array([
 [1,0,0,1],
 [1,1,0,0],
 [0,1,1,0],
 [0,0,1,1],
 [1,0,1,0],
 [0,1,0,1],
 [1,0,1,0],
 [0,1,0,1],
 [1,1,0,0],
])
#Definindo o número de Clusters(grupos)
num_cluster = 2

#Inicializar o modelo
kmeans = KMeans(n_clusters=num_cluster, random_state=0, n_init=10)

#Treinando o modelo
kmeans.fit(filmes_assistidos)

#Classificando os usuários
alcateia_indices = kmeans.predict(filmes_assistidos)

#Exibir os dados
print("Usuário pertence ao seguinte grupo:")
for i, cluster in enumerate(alcateia_indices):
  print(f"Usuário {i+1} pertence ao grupo {cluster+1}")

  print("\filmes_assistidos")
for i in range(len(filmes_assistidos)):
    assistidos = np.where(filmes_assistidos[i] == 1)[0] + 1
    print(f"Usuário {i+1} asssitiu aos filmes: {assistidos}")

#Função que recomenda filmes
def recomendar_filmes(filmes, filmes_assistidos, grupos_indices):
  filmes = np.array(filmes)

  #Encontrar o grupo do usuário com base em seu vetor de filmes assistidos
  usuario_id = len(filmes_assistidos)
  grupo_usuario = kmeans.predict(([filmes]))[0]

  #Encontrar todos os usuários no mesmo grupo
  usuarios_no_mesmo_grupo = [i for i in range(len(alcateia_indices))
  if grupos_indices[i] == grupo_usuario]

  #filmes assistidos pelos usuários no mesmo grupo
  filmes_recomendados = set()
  for usuario in usuarios_no_mesmo_grupo:
    filmes_assistidos_usuario = np.where(filmes_assistidos[usuario] == 1)[0]
    filmes_recomendados.update(filmes_assistidos_usuario)

#Remover filmes que o usuario ja assistiu
  filmes_recomendados = filmes_recomendados - set(np.where(filmes == 1)[0])

#Ajustar os índices dos filmes recomendados (de volta para 1-based)
  filmes_recomendados = [filme + 1 for filme in filmes_recomendados]

  return sorted(filmes_recomendados)

#Exemplo de uso da função recomendar_filmes
filmes_assistidos_usuario = [1, 0, 1, 0] #vetor de filmes
#assistidos (por exemplo, assistiu aos filmes 1 e 3)
filmes_recomendados = recomendar_filmes(filmes_assistidos_usuario, filmes_assistidos, alcateia_indices)

print(f"\nfilmes recomendados: {filmes_recomendados}")

def multiplicacao(num1, num2) :
    mult = num1 * num2
    return mult

print(multiplicacao(6,10))
print(multiplicacao(4,10))