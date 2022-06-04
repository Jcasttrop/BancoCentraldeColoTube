"""
Vamos a tener dos clases de usuarios:
-Parent (
    -Holds details about an user
    -Has a function to show user details
)

-Child (
    -Stores details about the account balance
    -Store details about the amount
    -Allows for deposit 
)
"""

#Clase padre



class User():
    
    #Clase inicializadora

    def __init__(self, name, age, gender):

        #el self es para que uno pueda poner cualquier cosa antes del metodo, eso le asignara la variable

        self.name = name
        self.age = age
        self.gender = gender

    
    #Una nueva funcion que tendrá la clase

    def show_user_details(self):
        """
        Esta funcion le devuelve los user details usando los parametros inicializadores
        """

        print("Personal Details")
        print("")
        print("Name: ",self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

"""
#Creamos el User Julian
Julian = User("Julian", 18, "M")

#Usamos la funcion definida dentro del objeto
Julian.show_user_details()
"""

#Clases hijas

#Child Class
class Bank(User):

    def __init__(self, name, age, gender):
        #Debemos traer lo que traia la clase padre con el metodo superinit
        super().__init__(name, age, gender)

        #Cada usuario tendrá un balance por defecto de 0
        self.balance = 0


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

