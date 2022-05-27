# Functions

def computepay(hrs, r):
   if hrs<40:
    print("",hrs*r)
   else:
    return(40*r+((hrs-40)*r*1.5))
    
hrs = float(input())
r= float(input())
 
p = computepay(hrs, r)
print("Pay", p)

    

