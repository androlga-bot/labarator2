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
        
        
def check_Bigger (val_Floor, val_Ceil):
    if val_Floor<=val_Ceil:
        return True
    else:
        return False

    
def check_Occrnc_Intrvl(edge_Left, value_Floor, value_Ceil, edge_Right):
    if  edge_Left>int(value_Floor) or edge_Right<int(value_Ceil):
            return True

        
def check_Occrnc_Word(list_Check,list_Confid):
    count=0
    if  list_Check!=['']:
            for i in range(len(list_Check)):
                if not (list_Check[i] in list_Confid.split(';')):
                    count+=1
            if count==len(list_Check):
                return True

            
list_Data_Bigger=[int(age), int(achivments)]
list_Data_Intrvl=[[int(pozitive[0]), int(pozitive[1])], [int(negative[0]),int(negative[1])],
                  [int(owner[0]),int(owner[1])], [float(price[0]),float(price[1])]]
list_Data_Word=[categories, genre, tag, developer, publisher, platform]


with open('steam.csv', encoding='utf-8') as f:
    r=csv.reader(f)
    
    for line in r:
        if line[12]=='positive_ratings':
            continue
        
        line12=[int(line[12])]
        line13=[int(line[13])]
        line17=[float(line[17])]
        line12.append(int(line[12]))
        line13.append(int(line[13]))
        line17.append(float(line[17]))
        line[16]=line[16].split('-')
        list_Line_Intrvl=[line[12], line[13], line[16], line[17]]
        list_Line_Word=[line[8], line[9], line[10], line[4], line[5], line[6]]
        if line[1]=='name':
            continue
        
        if line[3]!=str(english):
            continue
        
        for i in range(2):
            if check_Bigger ((list_Data_Bigger[i]),(line[7+4*i])):
                continue
        
        for i in range(4):
            if check_Occrnc_Intrvl ((list_Data_Intrvl[i][0]), (list_Line_Intrvl[i][0]),
                                    (list_Line_Intrvl[1]), (list_Data_Intrvl[i][1])):
                continue
         
        for i in range(6):
            if check_Occrnc_Word(list_Data_Word[i], list_Line_Word[i]):
                continue
        print(line[1])
        
