import random


# datos iniciales 
surnames = ['10', 'juan', '@12', 'null', 'antonioPerezDelCarmen', 'abcdefghtioiasoisdjads', 'Manolo', 'Perez', 'Soledad']
escuses = ['OMG?', 'Whats going on?', 'How much is it?', 'undefined']
dates = ['Jeferson', 'Matilda', 'R@fael', '1van', 'Pep3', 'Loquesea', 'Fel1berto', 'Pepit@', 'D@M']

# 1 - crear una funcion que genere una escusa aleatoria con esos datos 
def excuse_generator(who, what, when):
	ran_who = who[random.randint(0, len(who)-1)]
	ran_what = what[random.randint(0, len(what)-1)]
	ran_when = when[random.randint(0, len(when)-1)]
	print(ran_who+ ' ' + ran_what + ' ' + ran_when)
excuse_generator(surnames, escuses, dates)

# 2 - creeis otra funcion que cuente el numero de repeticiones de letras en cada array

count_dic = {}
def letter_counter(arr):
    for word in arr:
        for char in word:
            if char == count_dic:
                count_dic[char] =+ 1
            else: 
                count_dic[char] = 1
    return count_dic
print(letter_counter(surnames))

# 3 - suprimir repeticiones en un array y devolver el array sin la repeticion

def no_rep(arr):
    return list(set(arr))
    
print(no_rep(surnames))

# 4 - function que invierta todos los valores de el array

def inverted(arr):
    new_arr = []
    for i in range(0, len(arr)):
        for j in arr[i][::-1]:
            new_arr.append(j[::-1])
    return new_arr

print(inverted(surnames))