def divisors(num):
    divisors = [i for i in range(1,num+1) if num % i == 0]
    return divisors

def run():
    val = False
    while val == False:
        try:
            num = int(input("Ingresa un numero: "))
            print(divisors(num))
            print("Termino mi programa")
            val = True
        except ValueError:
            print("Debes ingresar un número")

if __name__ == "__main__":
    run()