def consecutivecount(a):
    count=0
    j=0
    i=0
    while(j<len(a)):
        i=i+count
        count=0
        if(i==len(a)):
            break
        for j in range(i,len(a)):
            if(a[i]==a[j]):
                count=count+1
            if(a[i]!=a[j]):
                break
        print("(",count,",",a[i],")")
def main():
    if __name__=="__main__":
        try:
            a=input("Enter your number :")
            a=list(a)
            consecutivecount(a)
        except None as input_error:
            print("input is of wrong format")
            main()
while(1):
    main()
