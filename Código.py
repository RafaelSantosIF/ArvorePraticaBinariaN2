class No:
    def __init__(self, valor):
        self.valor = valor 
        self.esquerdo = None 
        self.direito = None 
    
    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerdo and self.esquerdo.valor, self.valor, self.direito and self.direito.valor) 

class ArvoreB:
    def __init__(self):
        self.raiz = None
    
    def inserirEmNiveis(self, valor):
        if self.raiz is None:
           self.raiz = No(valor)
        else:
            self.inserirEmNivelRecursivo(valor, self.raiz)
    
    def inserirEmNivelRecursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerdo is None:
                no.esquerdo = No(valor)
            else:
                self.inserirEmNivelRecursivo(valor, no.esquerdo)
        else:
            if no.direito is None:
                no.direito = No(valor)
            else:
                self.inserirEmNivelRecursivo(valor, no.direito) 
    
    def emNiveis(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            print(self.raiz.valor, end = " ") 
        self.emNivelRecursivo(self.raiz) 
    
    def emNivelRecursivo(self, no):
        if no.esquerdo is not None:
            print(no.esquerdo.valor, end = " ")
        if no.direito is not None:
            print(no.direito.valor, end = " ")
        if no.esquerdo is not None:
            self.emNivelRecursivo(no.esquerdo)
        if no.direito is not None:
            self.emNivelRecursivo(no.direito)
    
    def mostrarRaiz(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            print(self.raiz.valor) 
    
    def altura(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            print(self.alturaRecursivo(self.raiz))
    
    def alturaRecursivo(self, no):
        if no is None:
            return 0
            
        altEsquerda = self.alturaRecursivo(no.esquerdo)
        altDireita = self.alturaRecursivo(no.direito)
        
        if altEsquerda > altDireita:
            return altEsquerda + 1
        else:
            return altDireita + 1
    
    def nosInternos(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.nosInternosRecursivo(self.raiz)
            
    def nosInternosRecursivo(self, no):
        if no is None:
            return False
        if no.esquerdo is not None or no.direito is not None:
            print(no.valor, end = " ")
        self.nosInternosRecursivo(no.esquerdo)
        self.nosInternosRecursivo(no.direito)
    
    def mostrarFolhas(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else: 
            self.mostrarFolhasRecursivo(self.raiz)
    
    def mostrarFolhasRecursivo(self, no):
        if no is None:
            return False
        if no.esquerdo is None and no.direito is None:
            print(no.valor, end = " ")
        self.mostrarFolhasRecursivo(no.esquerdo)
        self.mostrarFolhasRecursivo(no.direito)
    
    def verificarValor(self, valor):
        if self.raiz is None:
            print("A árvore está vazia")
        else: 
            return self.verificarValorRecursivo(self.raiz, valor)
            
    def verificarValorRecursivo(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        elif valor > no.valor:
            return self.verificarValorRecursivo(no.direito, valor)
        else:
            return self.verificarValorRecursivo(no.esquerdo, valor)

    
arvore = ArvoreB()
arvore.inserirEmNiveis(4)
arvore.inserirEmNiveis(2)
arvore.inserirEmNiveis(6)
arvore.inserirEmNiveis(1)
arvore.inserirEmNiveis(3)
arvore.inserirEmNiveis(5)
arvore.inserirEmNiveis(7)

print("Árvore inserida em níveis: ", arvore.emNiveis())
print("\nRaiz: ", arvore.mostrarRaiz())
print("\nAltura da árvore: ", arvore.altura())
print("\nNós internos: ", arvore.nosInternos())
print("\nFolhas: ", arvore.mostrarFolhas())

num = int(input("\nDigite o número que deseja verificar se está presente na árvore: "))
if arvore.verificarValor(num):
    print(f"\nO número {num} está presente na árvore!")
else:
    print(f"\nO número {num} não está presente na árvore!")
