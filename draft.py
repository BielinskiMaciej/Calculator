#here there is some scratchpad with notes and where I try some options
from operator import truediv

test="2+1,54+2,32"
hand_list=["2","+","1",",","5","4","+","1"]

test_space = test.replace(" ", "")
test_space2 = test_space.replace("", " ")
test_list = test_space2.split()

comma=False
'''while i < len(test_list)-1:
    if test_list[i].isdigit():
        tr=True
    else:
        comma=False
    if test_list[i].isdigit() and test_list[i+1]==",":
        number=test_list[i]+test_list[i+1]
        test_list[i]=number
        comma=True
        del test_list[i+1]
    if  test_list[i+1].isdigit() and comma==True:
        number = test_list[i] + test_list[i + 1]
        test_list[i] = number
        del test_list[i + 1]
        print (number)
    i+=1'''
'''number=""
prev_x=""
com=False
j=0
j_beg=0
for x in test_list:
    print ("X: ",x)
    if x==",":
        #print (x)
        #print (prev_x)
        number=prev_x+x
        com=True
        j_beg=j
    if com==True and x.isdigit():
        number=number+x
    if (x=="+" or x=="-" or x=="*" or x=="/") and com==True:
        com=False
        test_list[j_beg-1]=number
        test_list[j_beg:j].insert("R")
        number=""
        j=0
        j_beg=0


    print(number)

    prev_x = x
    j+=1
'''
count_comma=test_list.count(",")
i=0
j=0
if count_comma!=0:
    while i<count_comma:
        where_comma=test_list.index(",")
        test_list[where_comma-1]=test_list[where_comma-1]+test_list[where_comma]+test_list[where_comma+1]
        print("Before del: ", test_list)
        del test_list[where_comma]
        del test_list[where_comma]
        print ("After del: ",test_list)
        while j < len(test_list)-where_comma:
            if test_list[j].isdigit():
                test_list[where_comma]=test_list[where_comma]+test_list[j]
            else:
                break
            j+=1
        i+=1




print (test)
print(test_list)
#print (hand_list)