import random

def AccountNumberGenerator() -> int:
    """
    Esta funcion genera un numero de cuenta unico a cada usuario

    Esto lo hace comprobando que cada numero de cuenta sea distinto para cada usuario 
    """

    possibleNumbers = ["1","2","3","4","5","6","7","8","9","0"]

    listForAccount = []

    for i in range(9):
        union = random.choice(possibleNumbers)
        listForAccount.append(union)

    numberAccount = "".join(listForAccount)
    

    return numberAccount


def generatepassword() -> int:
    """
    Esta funcion genera un a contraseña de 15 caracteres al usuario.

    La funcion no necesita de ningun argumento 
    """

    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[',
            '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = MAYUS + MINUS + NUMS + CHARS

    password = []

    for i in range(15):
        elegidos = random.choice(caracteres)
        password.append(elegidos)

    contra = "".join(password)   #convertimos la lista en un str
    
    return contra
class User():
    pass

    def __init__(self,name,password,account_number):
        self.name = name
        self.password = password
        self.account_number = account_number

        self.isRegistered = False

        self.intentos = 3

        self.isConected = False

    def registrarUsuario(self):
        """
        Este atributo permite al usuario registarse

        Devuelve: name, password y numero de cuenta
        """

        print("Hey! Bienvenido al Banco de ColoTube, vamos a registarte")
        self.name = input("Por favor ingrese su nombre: ")

        #Genera la contraseña al usuario
        self.password = generatepassword()
        print(f"Por favor recuerda esta contraseña segura: {self.password}")

        #Le pregunta al usuario que si quiere cambiar la contraseña
        print("La contraseña que te dimos cumple con altos estandares de seguridad")

        eleccionCambioContraseña = input("¿Deseas personalizar tu contraseña? " )
        eleccionCambioContraseñaCONSOLA = eleccionCambioContraseña.lower()

        if eleccionCambioContraseñaCONSOLA == "si":
            newPassword = input("Tu nueva contraseña debe tener al menos 9 caracteres\nIngresa tu nuva contraseña: ")
            # Evalua la condicion
            if len(newPassword) >= 9:
                newPassword = self.password
            else:
                pass


        self.account_number = AccountNumberGenerator()

        self.isRegistered = True


        print(f"Tu registro: Te llamas {self.name}, con cuenta número {self.account_number} y contraseña {self.password}")

        self.account_number = AccountNumberGenerator()

        self.isRegistered = True

        return self.name,self.password,self.account_number,self.isRegistered


    def login(self):
        """
        Este atributo permite al usuario iniciar sesion siempre y cuando exista una cuenta registrada
        """
        print(f"Hey! {self.name} Bienvenido al Banco de ColoTube\nPara comprobar que eres tu, por favor danos tu contraseña ")

        validacionContraseña = input()

        if validacionContraseña == self.password:
            print(f"{self.name} bienvenido al sistema bancario")
            self.isConected = True
        else:
            self.intento =- 1
            #Aqui le daremos al usuario la capacidad de cambiar la contraseña en el ultimo inetento
            if self.intentos > 1:
                print("Contraseña incorrecta, intentelo de nuevo")
                print(f"Tienes {self.intentos} intentos restantes")
                self.login()

            elif self.intentos <1:
                print("¿Olvidaste tu contraseña?")

                ContraseñaOlvidada = input()

                ContraseñaOlvidadaCONSOLE = ContraseñaOlvidada.lower()

                if ContraseñaOlvidadaCONSOLE == "si":
                    newPassword = input("Tu nueva contraseña debe tener al menos 9 caracteres\nIngresa tu nuva contraseña: ")
                    # Evalua la condicion
                    if len(newPassword) >= 9:
                        newPassword = self.password
                    else:
                        pass
                else:
                    self.login()


