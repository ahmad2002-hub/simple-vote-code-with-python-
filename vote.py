dic={}
dic1={}
for i in range (1,3,1):
    print("give us the id of vote ")
    key=input("id of vote pls : ")
    print("giv me the age pls ")
    k=int(input("give us the age pls : "))
    while k<25:
        k=int(input("the age must be at least 25 : "))
    dic[key]=k
    print("give us the final order ")
    s=input("the order pls : ")
    while s!="ok" and s!="nonok" and s!="abs":
        s=input("the only accept answars  is (ok ,nonok,abs) ")
    
    dic1[key]=s
print(dic1,dic)
    
    
    
    
