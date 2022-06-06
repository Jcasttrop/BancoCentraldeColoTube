#Funciones de uso

def _AccountNumberGenerator():
        """
        Esta funcion genera un numero de cuenta unico a cada usuario
        Esto lo hace comprobando que cada numero de cuenta sea distinto para cada usuario 
        """

        import random

        possibleNumbers = ["1","2","3","4","5","6","7","8","9","0"]

        listForAccount = []

        for i in range(9):
            union = random.choice(possibleNumbers)
            listForAccount.append(union)

        numberAccount = "".join(listForAccount)

        return numberAccount


class User():
    
    #Clase inicializadora

    def __init__(self, name, age, gender):

        #el self es para que uno pueda poner cualquier cosa antes del metodo, eso le asignara la variable

        self.name = name
        self.age = age
        self.gender = gender

        self._Anumber = _AccountNumberGenerator()

    def show_user_details(self):
        """
        Esta funcion le devuelve los user details usando los parametros inicializadores
        """

        print("Personal Details")
        print("")
        print("Name: ",self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Account nunmber:", self._Anumber)

class Bank(User):

    def __init__(self, name, age, gender):
        #Debemos traer lo que traia la clase padre con el metodo superinit
        super().__init__(name, age, gender)

        #Cada usuario tendrá un balance por defecto de 0
        self.balance = 0


    def Show_Account_Number(self):

        print("Yor account number is: ", self._Anumber)

    def deposit(self, amount):
        """
        Esta funcion le permite al usuario depositar dinero a su cuenta
        """

        self.amount = amount
        self.balance = self.balance + amount

        print("Account Balance Has Been Updated, your new balance is: ", self.balance)


    def withdraw(self, amount):
        """
        Esta funcion le permite retirar dinero de su cuenta
        """

        self.amount = amount

        #Comprobamos que hay suficientes fondos
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available: ", self.balance)

        else:
            #Actualizamos el balance
            self.balance = self.balance - self.amount
            print("Account balance has been updated: ", self.balance)



    def view_balance(self):
        """
        Esta funcion le enseña al usuario su balance
        """
        print("Your Balance is: ", self.balance)


Julian = Bank("Julian", 18, "M")
Julian.show_user_details()
Julian.Show_Account_Number()