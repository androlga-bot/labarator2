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
   

def check_Occurence_Left (intrvl,value):
    if int(value)<int(intrvl):
        continue
        
        
def check_Bigger (val1,val2):
    if int(val1)<int(val2):
        return True
    else:
        return False

    
def check_Occrnc_Intrvl(edge_Left, value_Floor, value_Ceil, edge_Right):
    if  float(edge_Left)>float(value_Floor) or float(edge_Right)<float(value_Ceil):
            return True

        
def check_Occrnc_Word(list_Check,list_Confid):
    count=0
    if  list_Check!=['']:
            for i in range(len(list_Check)):
                if not (list_Check[i] in list_Confid.split(';')):
                    count+=1
            if count==len(list_Check):
                return True
            
list_Data_Bigger=[age, achivments]
list_Data_Intrvl=[pozitive, negative, owner, price]
list_Data_Word=[categories, genre, tag, developer, publisher, platform]
with open('steam.csv', encoding='utf-8') as f:
    r=csv.reader(f)
    
    for line in r:
        line[12].append(line[12])
        line[13].append(line[13])
        line[17].append(line[17])
        line[16]=line[16].split('-')
        list_Line_Intrvl=[line[12], line[13], line[16], lina[17]]
        list_Line_Word=[line[8],line[9],line[10],line[4],line[5],line[6]]
        if line[1]=='name':
            continue
        string=','.join(line)#bесполезно, ибо я работаю с массивом
        
        
        if line[3]!=english:
            #continue
            pass
        
        for i in range(2):
            if check_Bigger (list_Data[i],line[7+4*i]):
                continue
        
        
        for i in range(4):
            if check_Occrnc_Intrvl (list_Data_Intrvl[i][0], list_Line_Intrvl[i][0],
                                    list_Line_Intrvl[1], list_Data_Intrvl[i][1]):
                continue
                
         
        for i in range(6):
            if check_Occrnc_Word(list_Data_Word[i], list_Line_Word[i]):
                continue
        #if  int(achivments)>int(line[11]):
            #continue
            #pass
            
            
        #if  int(pozitive[0])>int(line[12]) or int(pozitive[1])<int(line[12]):
            #continue
            #pass
            
            
        #if  int(negative[0])>int(line[13]) or int(negative[1])<int(line[13]):
            #continue
        
        
        #if int(owner[0])>int(line[16].split('-')[0]) or int(owner[1])<int(line[16].split('-')[1]):#не то формат в таблице
            #continue
        
        
        #if  float(price[0])>float(line[17]) or float(price[1])<float(line[17]):
            #continue
        
        
        #if  categories!=['']:
            #for i in range(len(categories)):
#                if not (categories[i] in line[8].split(';')):
#                    k=1
  #                  
  #                  
  #      if k==1:
   #         k=0
   #         continue
        
   #     
  #      if genre!=['']:
   #         for i in range(len(genre)):
   #             if  not (genre[i] in line[9].split(';')):
  #                  k=1
                    
                    
   #     if k==1:
    #        k=0
   #         continue

            
    #    if tag!=['']:
    #        for i in range(len(tag)):
    #            if  not (tag[i] in line[10].split(';')):
    #                k=1
    #                
    #                
    # #   if k==1:
    #        k=0
    #        continue

            
    #    if developer==['']:
    #        k=1
            
            
    #    if developer!=['']:
    #        for i in range(len(developer)):
    #            if developer[i] in line[4].split(';'):
    #                k=1
    #                break
                    
                    
    #    if k==0:
    #        continue
    #    else:
    #        k=0
            
            
    #    if publisher==['']:
    #        k=1
            
            
    #    if publisher!=['']:
    #        for i in range(len(publisher)):
    #            if publisher[i] in line[5].split(';'):
     #               k=1
                    
                    
     #   if k==0:
    #        continue
    #    else:
    #        k=0
            
            
     #   if platform==['']:
    #        k=1
            
            
    #   if platform!=['']:
   #         for i in range(len(platform)):
    #            if platform[i] in line[6].split(';'):
   #                 k=1
   #                 break
                    
                    
  #      if k==0:
  #          continue
  #      else:
   #         k=0
            
            
        print(line[1])
