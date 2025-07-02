#Задание 1. Список (List)

primes = [10, 15, 20, 25, 30, 35, 40]
n = 3
print(f"{n}-й элемент списка-", primes[n])

x = 100
primes[n] = x
primes = primes + [x]
print(primes)

#или можно добавить с помощью метода extend
#primes.extend([x])
#print(primes)

#Задание 2. Кортеж (Tuple)

my_tuple = ('треугольник', 'квадрат', 'круг', 'овал')
n = 2
print(f"{n}й элемент кортежа", my_tuple[n])

x = 'параллелепипед'
my_new_tuple = my_tuple + (x,)  #Для создания кортежа с единственным элементом после значения элемента ставят замыкающую запятую
print(my_new_tuple)

#Задание 3: Множество (Set)

numbers = {2, 4, 6, 8, 10, 12}
animals = set(['cat','cat', 'dog', 'fox', 'elephant', 12, 10])
my_set = numbers.intersection(animals) #Найдите и выведите общие элементы в них
print(my_set)

numbers = {2, 4, 6, 8, 10, 12}
animals = set(['cat','cat', 'dog', 'fox', 'elephant', 12, 10]) #Объедините множества и выведите результат
my_newset = numbers.union(animals)
print(my_newset)

numbers = {2, 4, 6, 8, 10, 12}
animals = set(['cat','cat', 'dog', 'fox', 'elephant', 12, 10])# Удалите число X из второго множества
animals.remove(12)
print(animals)

#Задание 4: Словарь (Dict)

months = {1 : 'Январь', 2 : 'Февраль', 3 :'Март', 4 : 'Апрель'}
print(months [1])

months = {1: 'Январь', 2: 'Февраль', 3:'Март', 4: 'Апрель'}
months [5] = 'Май' #Добавьте новую пару "X": "Y".
del months [1] #Удалите ключ "X".
print(months)

#Задание 5. Метод для списка

def filter(numeric_list):
    list = [] #Создаем пустой лист

    for element in numeric_list: #Перебираем введенные числа
        if element > 0:
            list.append(element) #Добавляем в пустой список только положительные числа

    return list

# userValue = input('Введите любое количество чисел через пробел: ') #пользователь вводит строку
# listString = userValue.split() #рвзбиение строки на части по пробелу. Получается лист строк
# numeric_list = [int(x) for x in listString]
# print(filter(numeric_list))

print(filter([10, 56, 89,-100, -1502]))

#Задание 6: Метод для словаря

def update_age(student, age):
    new_age = student['возраст'] + age #создаем новую переменную, где находим по ключу и прибавляем 3
    return new_age #возвращаем новую переменную, хотя можно было и заретернуть student['возраст'] + age

student = {'имя' : 'Виктория', 'возраст' : 19}
print(update_age(student, 3))



