# frc=input("введите силу:")
# shd=input("введите защиту:")
# record=frc+','+shd
# data=open(file="data.txt",mode='a')
# data.write(record+"\n")
# data.close()

data=open(file="data.txt",mode='r')
dataN=data.readlines()
data=[]
for item in dataN:
    data.append(item.strip())
for item in data:
    p=item.split(",")
    print(f'сила={p[0]}, защита={p[1]}')
