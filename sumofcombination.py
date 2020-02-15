import itertools
def p(num):
    if num > 1:        
        for i in range(2, num//2):   
           if (num % i) == 0: 
               return False 
               break
        else: 
           return True
  
    else: 
       return False 
if __name__ == "__main__":
    while(True):
        n=input()
        n=list(n)
        x=[]
        for i in n:
            x.append(int(i))
        #print(x)
        a=[]
        b = [x[i:j] for i, j in itertools.combinations(range(len(x)+1), 2)]
        d=[]
        co=0
        import numpy as np
        for i in b:
            e= np.char.mod('%d', i)
            c= ''.join(e)
            c= int(c)
            d.append(c)
            if p(c):
                co=co+c
        #print(d)
        print(co)
