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
owners=''
average=''
median=''
pozitive=''
negative=''
english=''
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
if price=='':
    price=['0','2000']
print('Количество достижений (минимальный порог)')
achivments=input()
if achivments=='':
    achivments='0'
print('Можете выбрать количество владельцев игры (минимум, максимум)')
owners=input().split(', ')
if owners=='':
    owners=['0','8000000000']
print('Количество позитивных отзывов (минимум, максимум)')
pozitive=input().split(', ')
if pozitive=='':
    pozitive=['0','7000000000']
print('Количество негативных отзывов (минимум, максимум)')
negative=input().split(', ')
if negative =='':
    negative=['0','8000000000']
print('Aнглийский язык поддерживать (да/нет)')
engli=input()
if engli =='да':
    english=1
else:
    english=0
with open('steam.csv') as f:
    r=csv.reader(f)
    
    for line in r:
        string=','.join(line)
        if string[3]!=english:
            continue
        if int(age)<int(string[7]):
            continue
        if  int(achivments)<int(string[11]):
            continue
        if  int(pozitive[0])>int(string[12]) or int(pozitive[1])<int(string[12]):
            continue
        if  int(negative[0])>int(string[13]) or int(negative[1])<int(string[13]):
            continue
        if int(owner[0])>int(string[16]) or int(owner[1])<int(string[16]):
            continue
        if int(price[0])>int(string[17]) or int(owner[1])<int(string[17]):
            continue
        if  categories!='':
            for i in range(len(categories)):
                if not (categories[i] in string[8].split(';')):
                    k=1
        if k==1:
            k=0
            continue
        
        if genre!=''
            for i in range(len(genre)):
                if  not (genre[i] in string[9].split(';')):
                    k=1
        if k==1:
            k=0
            continue

        if tag!='':
            for i in range(len(tag)):
                if  not (tag[i] in string[10].split(';')):
                    k=1
        if k==1:
            k=0
            continue
        if developer!='':
            for i in range(len(developer)):
                if developer[i] in string[4].split(';'):
                k=1
                break
        if k==0:
            continue
        else:
            k=0

        if publisher!='':
            for i in range(len(publisher)):
                if publisher[i] in string[5].split(';'):
                k=1
                break
        if k==0:
            continue
        else:
            k=0

        if platform!='':
            for i in range(len(platform)):
                if platform[i] in string[6].split(';'):
                k=1
                break
        if k==0:
            continue
        else:
            k=0
        print(string[1])
