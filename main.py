import re





def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        raise ZeroDivisionError("Dzielisz przez 0")
    return a/b

def calculating(equation):
    equation=equation.replace(" ","")
    equation_space = equation.replace("", " ")
    equation_list=equation_space.split()
    #tokens_o = re.findall(r'\d+\.?\d*|[+\-*/]', equation)
    print (equation_list)


while True:
    print("Witamy w kalkulatorze. Można wykonać działanie dodawania (+), odejmowania (-), mnożenia (*) lub dzielenia (/) wybranych liczb. Można wybrać tylko jedno działanie naraz")
    print ("Aby wyjść należy wpisać 'wyłącz'")
    print("Aby poznać wynik zadanego działania, proszę podać całość naraz poniżej (np. 2+2)")

    user_eq = input("Podaj swoje działanie: ")

    if user_eq.lower() == 'wyłącz':
        print("Wyłączanie...")
        break

    try:
        result = calculating(user_eq)
        print(f"Wynik: {result}")
    except Exception as e:
        print(f"Error: {e}")