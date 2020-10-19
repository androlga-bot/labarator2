import csv

genre=[]
categories=[]
tag=[]
developer=''
publisher=''
platform=[]
age=19
pricei=[0,2000]
achivments=0
owners=[0,8000000000]
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
age=int(input())
print('Какая цена (минимум, максимум)?')
price=list(map(int,input().split(', ')))
print('Количество достижений (минимальный порог)')
achivments=int(input())
print('Можете выбрать количество владельцев игры (минимум, максимум)')
owners=list(map(int,input().split(', ')))
print('Среднее значение времени в игре')
average=input()
print('Медианное значение времени в игре')
median=input()
print('Количество позитивных отзывов (минимум, максимум)')
pozitive=input()
print('Количество негативных отзывов (минимум, максимум)')
negative=input()
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
        print(line)
        print (line)
        break
        
        
    




