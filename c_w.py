# f=open('data.txt','w',encoding='utf-8')
# f.write("data1"+'\n')
# f.write("data2"+'\n')
# f.write("data3"+'\n')
# f.close()

# with open('data.txt','a',encoding='utf-8') as f:
#     f.write("append 2"+'\n')
data=[]
with open('data.txt','r',encoding='utf-8') as f:
    data=[item.strip() for item in f.readlines()]
    
    for item in f.readlines():
        data.append(item.strip()) 
    dataN = f.readlines()
    data=[]
for item in dataN:
    data.append(item.strip())
    
# print(data)
# for i in data:
#     person = i.split(',')
#     print(f'ученик:{person[0]} возраст {person[1]} рост - {person[2]} вес - {person[3]}' )