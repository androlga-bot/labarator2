import csv
k=0
genre=''
categories=''
tag=''
developer=''
publisher=''
platform=''
age=''
price=''
achivments=''
owner=''
average=''
median=''
pozitive=''
negative=''
english=1

print('Какой жанр игры вас интересует?')
genre=input().split(', ')

print('Какая категория?')
categories=input().split(', ')

print('Выберите  тэги')
tag=input().split(', ')

print('Каких разработчиков любите?')
developer=input().split(', ')

print('Какие издатели?')
publisher=input().split(', ')

print('Ваша/Ваши платформа(ы)')
platform=input().split(', ')

print('Ваш возраст')
age=input()

if age=='':
    age='18'
    
print('Какая цена (минимум, максимум)?')
price=input().split(', ')
if price==['']:
    price=['0','2000']
    
print('Количество достижений (минимальный порог)')
achivments=input()
if achivments=='':
    achivments='0'
    
print('Можете выбрать количество владельцев игры (минимум, максимум)')
owner=input().split(', ')
if owner==['']:
    owner=['0','8000000000']
    
print('Количество позитивных отзывов (минимум, максимум)')
pozitive=input().split(', ')
if pozitive==['']:
    pozitive=['0','7000000000']
    
print('Количество негативных отзывов (минимум, максимум)')
negative=input().split(', ')
if negative ==['']:
    negative=['0','8000000000']
    
print('Aнглийский язык поддерживать (да/нет)')
engli=input()
if engli =='да':
    english=1
else:
    english=0
    
with open('steam.csv', encoding='utf-8') as f:
    r=csv.reader(f)
    
    for line in r:
        if line[1]=='name':
            continue
        string=','.join(line)#bесполезно, ибо я работаю с массивом
        if line[3]!=english:
            #continue
            pass
        if int(age)<int(line[7]):
            continue
            #pass
        if  int(achivments)>int(line[11]):
            continue
            #pass
        if  int(pozitive[0])>int(line[12]) or int(pozitive[1])<int(line[12]):
            continue
            #pass
        if  int(negative[0])>int(line[13]) or int(negative[1])<int(line[13]):
            continue
        
        if int(owner[0])>int(line[16].split('-')[0]) or int(owner[1])<int(line[16].split('-')[1]):#не то формат в таблице
            continue
        
        if  float(price[0])>float(line[17]) or float(price[1])<float(line[17]):
            continue
        
        if  categories!=['']:
            for i in range(len(categories)):
                if not (categories[i] in line[8].split(';')):
                    k=1
        if k==1:
            k=0
            continue
        
        if genre!=['']:
            for i in range(len(genre)):
                if  not (genre[i] in line[9].split(';')):
                    k=1
        if k==1:
            k=0
            continue

        if tag!=['']:
            for i in range(len(tag)):
                if  not (tag[i] in line[10].split(';')):
                    k=1
        if k==1:
            k=0
            continue

        if developer==['']:
            k=1
        if developer!=['']:
            for i in range(len(developer)):
                if developer[i] in line[4].split(';'):
                    k=1
                    break
        if k==0:
            continue
        else:
            k=0
        if publisher==['']:
            k=1
        if publisher!=['']:
            for i in range(len(publisher)):
                if publisher[i] in line[5].split(';'):
                    k=1
        if k==0:
            continue
        else:
            k=0
        if platform==['']:
            k=1
        if platform!=['']:
            for i in range(len(platform)):
                if platform[i] in line[6].split(';'):
                    k=1
                    break
        if k==0:
            continue
        else:
            k=0
        print(line[1])
