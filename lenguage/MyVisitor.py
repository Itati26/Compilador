from GrammarVisitor import GrammarVisitor
from GrmmmarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    # Definimos la memoria o el entorno
    def __init__(self):
        self.memory={}

    #Definimos la asignación 
    def visitAssing(self,ctx):
        # Se obtiene el id o nombre de la variable 
        name=ctx.ID().getText()
        # Se obtiene un valor (numerico o expresion)
        value=self.visit(ctx.expr())
        # Se almacena en memoria apartir de memoria a partir del nombr y el valor
        self.memory[name]=value

    #Definimos print
    def visitPrint(self,ctx):
        # Definimos la expresion que se desea mostrar
        value=self.visit(ctx.expr())
        # Imprime el valor
        print(value)

    # Definimos las expresiones
    def visitExpr(self, ctx):
        # Bus ca si existen ID
        if ctx.ID():
            # Obtine del contexto el nombre de la variable
            name=ctx.ID().getText()
            # Si el nombre de la variable no esta, lanza un error
            if name not in self.memory:
                raise NameError(f"Varible '{name}' no definida")
            # Si existe el nombre retorna la variable
            return self.memory[name]
        # Busca el operador
        elif ctx.op:
            # Visita y obtiene lado izquierdo 
            left=self.visit(ctx.expr(0))
            # Visita y obtiene lado derecho
            right=self.visit(ctx.expr(1))
            # Evalua la operación a realizar
            if ctx.op.text == "+":
                return left + right
            if ctx.op.text == "-":
                return left - right
            if ctx.op.text == "*":
                return left * right
            if ctx.op.text == "/":
                # Verifica la division de cero 
                if right == 0:
                    raise ValueError("División por cero")
                return left / right
            
    

        
    