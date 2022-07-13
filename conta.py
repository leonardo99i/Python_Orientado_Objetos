# It creates a class called Conta.
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Objeto Criado")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

        """
        The __init__() function is called automatically every time the class is being used to create a new
        object 
        Self é a referencia, que sabe onde encontrar o objeto
        """


conta = Conta(123, "Leo", 50.5, 1000.0)
conta_2 = Conta(321, "Nico", 100.0, 1000.0)
