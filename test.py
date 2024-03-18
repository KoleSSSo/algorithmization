#ЛЕКЦИЯ
mystr = 'ляляля'
mylist = list(mystr)
#print(mylist)
mylist.append('л')
mylist.insert(7, 'я' )
#print(mylist)
#print(len(mylist))
#print(mylist.count('л'))
sorted = mylist.copy()
sorted.sort()
#print(sorted)
sumlist = mylist + sorted
#print(sumlist)
squares = [x**3 for x in range(6)] #генератор списков
#print(squares)
mytuple = ("Ivan", "Andrew", "Mary", "ALex")
#print(mytuple)
mydictionary = {'house':'chaos', 'flat':'flood', 'window':'windows'}
item = mydictionary.get("window")
#print(mydictionary["house"])
#print(item)
item = mydictionary.pop("flat")
#print(item)
#print(mydictionary)
#print(mydictionary.values())
myset = {'apple', 'banana', 'melon', 'lemon', 'apple', 'watermelon', 'orange', 'melon', 'grain', 'apple'}
set_A = {1, 2, 3}
set_B = {3, 4, 5}
C = set_A|set_B
#print(myset)
#print(C)
C = set_A&set_B
#print(C)


#4.1
def multiplicity_3 (a):
    print("При х = ", a, a%3==0)
print("4.1")
x1 = 6
x2 = 4
x3 = 0.6
multiplicity_3(x1)
multiplicity_3(x2)
multiplicity_3(x3)
print()

#4.2
print("4.2")
def division_100 ():
    try:
        a = int(input("Введите делитель: "))
        temp = 100 / a
    except ZeroDivisionError:
        k = 0
    except ValueError:
        isinstance(str, a)
    print("100 : x = ", 100 / a)

division_100()
print()

#4.3
print("4.3")
def magicDate ():
    try:
        a = list(map(int, input("Введите дату в формате хх.хх.хххх: ").split(".")))
        magic = a[0]*a[1]==(a[2]%100)
    except ValueError:
        isinstance(str, a)==False
    if magic:
        print("Дата счастливая, повезло!")
    else:
        print("Увы:(")

magicDate()
print()

#4.4
print("4.4")
def lucky_ticket ():
    temp = input("Введите номер билета: ")
    l = len(temp)
    firsthalf = 0
    secondhalf = 0
    counter = 0
    for i in temp:
        if(counter < (l//2)):
            firsthalf+=int(i)
        else:
            secondhalf+=int(i)
        counter+=1
    if(firsthalf==secondhalf):
        print("Счастливый билет!")
    else:
        print("Увы:(")
lucky_ticket()
print()