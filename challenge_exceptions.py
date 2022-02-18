# Here we create an especific class of exception for
# our problem in order to manage with two errors
class UnAcceptedValueError(Exception):   
    def __init__(self, data):    
        self.data = data
    def __str__(self):
        return repr(self.data)


def divisors(num):
    divisors = [i for i in range(1,num+1) if num % i == 0]
    return divisors
        

def run():
    
    while True:
        try:
            num = int(input("Ingresa un numero: "))
            if num < 0:
                raise UnAcceptedValueError("Ingresa un número positivo")
            print(divisors(num))
            print("Termino mi programa")
            break
        # here we manage the error caused by letters
        except ValueError:
            print("Debes ingresar un número")
        # here we manage the error caused by negative numbers
        except UnAcceptedValueError as UAVE:
            print(UAVE)

if __name__ == "__main__":
    run()