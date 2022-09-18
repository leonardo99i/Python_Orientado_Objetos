# It creates a class called Conta.
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Objeto Criado")
        # Creating the attributes of the class.
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        """
        The __init__() function is called automatically every time the class is being used to create a new
        object 
        Self é a referencia, que sabe onde encontrar o objeto
        """

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))


conta = Conta(123, "Leo", 55.5, 5000.0)
conta2 = Conta(321, "Nico", 43.9, 1000.0)

conta2.extrato()