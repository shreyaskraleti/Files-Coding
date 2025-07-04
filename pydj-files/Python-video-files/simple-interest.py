# calculate simple interest:
def si(p,t,r):
    return (p*t*r)/100
p = int(input("Enter Principal Amount:"))
t = int(input("Enter time in years:"))
r = int(input("Enter rate of interest per annum:"))
result = si(p,t,r)
print(result)