#Estrutura de dados:Fila e Pilha usando heranca

class Lista:
  def __init__(self):
    self.lista = []

  def __str__(self):
    return str(self.lista)

  def tamanho(self):
    return len(self.lista)

  def vazia(self):
    return self.tamanho() == 0

  def inserir(self, elemento):
    self.lista.append(elemento)

class Fila(Lista):
  def __init__(self):
    Lista.__init__(self)

  def remover(self):
    if not self.vazia():
      return self.lista.pop(0) 
    else:
      return "A Fila estah vazia"

class Pilha(Lista):
  def __init__(self):
    Lista.__init__(self)

  def remover(self):
    if not self.vazia():
      return self.lista.pop()
    else:
      return "A Pilha estah vazia"
