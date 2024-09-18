
print ("Witamy w kalkulatorze. Można wykonać działanie dodawania (+), odejmowania (-), mnożenia (*) lub dzielenia (/) wybranych liczb. Można wybrać tylko jedno działanie naraz")
print ("Aby poznać wynik zadanego działania, proszę podać całość naraz poniżej (np. 2+2")
user_eq=input("Podaj swoje działanie: ")

number_plus=user_eq.count("+")
number_minus=user_eq.count("-")
number_div=user_eq.count("/")
number_mul=user_eq.count("*")

def add(numbers):
    result = 0
    for i in numbers:
        result = result+int(i)
    return result

def sub(numbers):
    result = int(numbers[0])
    count = 0
    for i in numbers:
        count += 1
        if count == 1:
            result = int(i)
        else:
            result = result - int(i)
    return result

def mul(numbers):
    result = 1
    for i in numbers:
        result = result*int(i)
    return result

def div(numbers):
    result = 0
    count=0
    for i in numbers:
        count+=1
        if count==1:
            result=int(i)
        else:
            result = result/int(i)
    return result

if "+" in user_eq:
    user_var = user_eq.split("+")
    print (add(user_var))
elif "-" in user_eq:
    user_var = user_eq.split("-")
    print(sub(user_var))
elif "*" in user_eq:
    user_var = user_eq.split("*")
    print(mul(user_var))
elif "/" in user_eq:
    user_var = user_eq.split("/")
    print(div(user_var))
else:
    print ("Nieznany symbol działania")