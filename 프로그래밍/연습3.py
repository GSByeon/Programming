#문제 4-1
for i in range(0,5):
    print("*",end='')

#문제 4-2
for i in range(0,4):
    for j in range(0,5):
        print("*",end='')
    print("")

#문제 4-3
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end='')
    print("")
#문제 4-4
for i in range(0,5):
    for j in range(0,5-i):
        print("*",end='')
    print("")
#문제 4-5
for i in range(0,5):
    for j in range(0,5-i):
        print(" ",end='')
    for j in range(0,i+1):
        print("*",end='')
    print("")
#문제 4-6
for i in range(0,5):
    for j in range(0,i+1):
        print(" ",end='')
    for j in range(0,5-i):
        print("*",end='')
    print("")
#문제 4-7
for i in range(0,5):
    for j in range(0,5-i):
        print(" ",end='')
    for j in range(0,2*i+1):
        print("*",end='')
    for j in range(0,5-i):
        print(" ",end='')
    print("")
#문제 4-8
for i in range(0,5):
    for j in range(0,i+1):
        print(" ",end='')
    for j in range(0,2*5-2*i-1):
        print("*",end='')
    for j in range(0,i+1):
        print(" ",end='')
    print("")
#문제 4-9
apart=[[101,102,103,104],[201,202,203,204],[301,302,303,304],[401,402,403,404]]
arrears=[101,203,301,404]
for floor in apart:
    for house in floor:
        if house in arrears:
            continue
        else:
            print("Newspaper delivery: ",house)

    
