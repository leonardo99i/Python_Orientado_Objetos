def cria_conta(numero, titular, saldo, limite):
    """
    It creates a dictionary with the keys "numero", "titular", "saldo" and "limite" and returns it
    
    :param numero: account number
    :param titular: The name of the account holder
    :param saldo: the amount of money in the account
    :param limite: the maximum amount of money that can be withdrawn from the account
    :return: A dictionary with the keys "numero", "titular", "saldo", and "limite"
    """
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo {}".format(conta["saldo"]))

nova_conta = cria_conta(123, "Leonardo", 1222, 5000)

deposita(nova_conta, 300)

# Printing the value of the `saldo` key in the `nova_conta` dictionary.
extrato(nova_conta)