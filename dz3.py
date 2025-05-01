a="фара"
b="арфа"
if len(a)==len(b):
    for i in range(len(a)):
        if a[i] not in b:
            print("это не анаграмма")
            break
    else:
        print("это анаграмма")    
else: 
    print("это не анаграмма")