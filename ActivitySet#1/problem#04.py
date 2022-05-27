# Conditional Execution


hrs = float(input())
r=float(input())
if hrs<40:
    print("",hrs*r)
else:
   
    print(*"",40*r+((hrs-40)*r*1.5))
    