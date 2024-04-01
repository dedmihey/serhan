immutable_var = (19, 56, 'm', 'y')
print(immutable_var)
#immutable_var[1] = 24 #Попытка изменить элемент кортежа заканчивается неудачей
#print(immutable_var) #Кортеж является неизменяемым объектом
mutable_list = [19, 56, 'm', 'y']
mutable_list[1] = 24
print(mutable_list)

