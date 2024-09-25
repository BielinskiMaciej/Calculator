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
    #equation_list = equation.split()
    #tokens_o = re.findall(r'\d+\.?\d*|[+\-*/]', equation)
    #print (equation_list)
    #merging together spliited numbers with more than one digit
    i = 0
    #print ("Before merging")
    #print(equation_list)
    while i < len(equation_list) - 1:
        if equation_list[i].isdigit() and equation_list[i + 1].isdigit():
            equation_list[i] = equation_list[i] + equation_list[i + 1]
            del equation_list[i + 1]
            i-=1
        i += 1
    #print("After merging")
    #print(equation_list)
    #print (len(equation_list))

    #searching for multiplication and division
    i = 0
    while i < len(equation_list):
        if equation_list[i]=="*":
            mul_result = mul(float(equation_list[i-1]),float(equation_list[i+1]))
            equation_list[i-1]=mul_result
            del equation_list[i:i+2]
        elif equation_list[i]=="/":
            div_result = div(float(equation_list[i-1]),float(equation_list[i+1]))
            equation_list[i-1]=div_result
            del equation_list[i:i+2]
        i+=1
    #print(equation_list)
    #looking for addition and subtraction
    i = 0
    while i < len(equation_list):
        if equation_list[i] == "+":
            add_result = add(float(equation_list[i - 1]), float(equation_list[i + 1]))
            equation_list[i - 1] = add_result
            del equation_list[i:i + 2]
        elif equation_list[i] == "-":
            sub_result = sub(float(equation_list[i - 1]), float(equation_list[i + 1]))
            equation_list[i - 1] = sub_result
            del equation_list[i:i + 2]
        i += 1
    #print(equation_list)
    return equation_list[0]

while True:
    # print("Witamy w kalkulatorze. Można wykonać działanie dodawania (+), odejmowania (-), mnożenia (*) lub
    # dzielenia (/) wybranych liczb. Można wybrać tylko jedno działanie naraz")
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