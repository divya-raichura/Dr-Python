list1 = ['vikas', 'divya', 'raichura']
for i in list1:
    i.upper()
    print(list1)
list1[0].upper()
list1[1] = 'chomu'
print(list1)
#  observation: if we replace the element in a list, yes it modifies
#  ie we can remove or add or replace element in list
#  but in that element if we tried to make change it won't cause
#  it is string type and strings are immutable in python
