"""
this code prints hallow paralello gram 
enter number of stars :5
    *****
   *   *
  *   *
 *   *
*****
"""
st=int(input("enter number of stars :"))
sp=st-1
skip=st-2

print(sp * " "+ st * "*")
sp-=1
while(sp>0):
    print(sp * " "+"*"+skip * " "+ "*")
    sp-=1
print(st * "*")
    