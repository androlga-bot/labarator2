import csv

count = 0
genre = ''
categories = ''
tag = ''
developer = ''
publisher = ''
platform = ''
age = ''
price = ''
achivments = ''
owner = ''
average = ''
median = ''
pozitive = ''
negative = ''
english = ''

print('Какой жанр игры вас интересует?')
genre = input().split(', ')

print('Какая категория?')
categories = input().split(', ')

print('Выберите  тэги')
tag = input().split(', ')

print('Каких разработчиков любите?')
developer = input().split(', ')

print('Какие издатели?')
publisher = input().split(', ')

print('Ваша/Ваши платформа(ы)')
platform = input().split(', ')

print('Ваш возраст')
age = input()
if age == '':
    age = '18'
    
print('Какая цена (минимум, максимум)?')
price = input().split(', ')
if price == ['']:
    price = ['0', '2000']
    
print('Количество достижений (минимальный порог)')
achivments = input()
if achivments == '':
    achivments = '0'
    
print('Можете выбрать количество владельцев игры (минимум, максимум)')
owner = input().split(', ')
if owner == ['']:
    owner = ['0', '8000000000']
    
print('Количество позитивных отзывов (минимум, максимум)')
pozitive = input().split(', ')
if pozitive == ['']:
    pozitive = ['0', '7000000000']
    
print('Количество негативных отзывов (минимум, максимум)')
negative = input().split(', ')
if negative == ['']:
    negative = ['0','8000000000']
    
print('Aнглийский язык поддерживать (да/нет)')
engli = input()
if engli == 'да':
    english = 1
elif engli == 'нет':
    english = 0
        
        
def check_smaller (val_floor, val_ceil):
    return val_floor <= val_ceil
        
    
def check_occrnc_intrvl(edge_left, value_floor, value_ceil, edge_right):
    return  (edge_left <= int(value_floor) and edge_right > int(value_ceil))

        
def check_occrnc_word(list_check,list_confid):
    list_confid=list_confid.split(';')
    return any(element in list_confid for element in list_check) or  list_check==['']
                
            

list_data_intrvl = [
    [int(pozitive[0]), int(pozitive[1])],
    [int(negative[0]), int(negative[1])],
    [int(owner[0]), int(owner[1])],
    [float(price[0]), float(price[1])]
]
list_data_word = [categories, genre, tag, developer, publisher, platform]



with open('steam.csv', encoding='utf-8') as f:
    r = csv.reader(f)
    
    for line in r:
        if line[12] =='positive_ratings':
            continue
        
        list_data_bigger = [int(age), int(line[11]) ]
        line[16]=line[16].split('-')
        list_line_smaller = [int(line[7]), int(achivments)]
        list_line_intrvl = [
            [int(line[12]), int(line[12])],
            [int(line[13]), int(line[13])],
            [int(line[16][0]), int(line[16][1])],
            [float(line[17]), float(line[17])]]
        list_line_word = [
            line[8],
            line[9],
            line[10],
            line[4],
            line[5],
            line[6]
            ]
            
        
        if line[3] != str(english) and english!='':
            continue
        
        if not all(
            check_smaller (
                list_line_smaller [count],
                list_data_bigger[count]
            )
            for count in range(2) 
        ): 
            continue
        
        if not all(
            check_occrnc_intrvl (
                list_data_intrvl [count] [0],
                list_line_intrvl [count] [0],
                list_line_intrvl [count] [1],
                list_data_intrvl [count] [1]
                )
            for count in range(4)
        ):
            continue
            
         
        if  not all(
            check_occrnc_word(
                list_data_word [count],
                list_line_word[count]
            ) 
            for count in range(6)
        ):
            continue
        
        print(line[1])
