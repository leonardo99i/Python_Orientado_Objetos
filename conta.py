# It creates a class called Conta.
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        """
        This function is a constructor for the class Conta. It takes four arguments: numero, titular, saldo,
        and limite. It sets the attributes of the class to the arguments passed in.
        
        :param numero: account number
        :param titular: the name of the account holder
        :param saldo: the balance of the account
        :param limite: the maximum amount of money that can be withdrawn from the account
        """
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


conta = Conta(123, "Leo", 50.5, 1000.0)
conta_2 = Conta(321, "Nico", 100.0, 1000.0)
