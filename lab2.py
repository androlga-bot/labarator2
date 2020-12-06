import csv

k = 0
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
english = 1

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
price=input().split(', ')
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
negative=input().split(', ')
if negative == ['']:
    negative = ['0','8000000000']
    
print('Aнглийский язык поддерживать (да/нет)')
engli = input()
if engli == 'да':
    english = 1
else:
    english=0
        
        
def check_bigger (val_floor, val_ceil):
    if val_floor <= val_ceil:
        return True
    else:
        return False

    
def check_occrnc_intrvl(edge_left, value_floor, value_ceil, edge_right):
    if  edge_left > int(value_floor) or edge_right < int(value_ceil):
            return True

        
def check_occrnc_word(list_check,list_confid):
    count=0
    if  list_check != ['']:
            for i in range(len(list_check)):
                if not (list_check[i] in list_confid.split(';')):
                    count += 1
            if count == len(list_check):
                return True

            
list_data_bigger = [int(age), int(achivments)]
list_data_intrvl = [[int(pozitive[0]), int(pozitive[1])], [int(negative[0]), int(negative[1])],
                  [int(owner[0]), int(owner[1])], [float(price[0]), float(price[1])]]
list_data_word = [categories, genre, tag, developer, publisher, platform]


with open('steam.csv', encoding='utf-8') as f:
    r = csv.reader(f)
    
    for line in r:
        if line[12]=='positive_ratings':
            continue
        
        line12 = [int(line[12])]
        line13 = [int(line[13])]
        line17 = [float(line[17])]
        line12.append(int(line[12]))
        line13.append(int(line[13]))
        line17.append(float(line[17]))
        line[16]=line[16].split('-')
        list_line_intrvl=[line[12], line[13], line[16], line[17]]
        list_line_word=[line[8], line[9], line[10], line[4], line[5], line[6]]
        if line[1] == 'name':
            continue
        
        if line[3] != str(english):
            continue
        
        for i in range(2):
            if check_bigger ((list_data_bigger[i]),(line[7+4*i])):
                continue
        
        for i in range(4):
            if check_occrnc_intrvl ((list_data_intrvl[i][0]), (list_line_intrvl[i][0]),
                                    (list_line_intrvl[1]), (list_data_intrvl[i][1])):
                continue
         
        for i in range(6):
            if check_occrnc_word(list_data_word[i], list_line_word[i]):
                continue
        print(line[1])
        
