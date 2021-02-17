l1 = linked_list()
l1.append(2)
l1.append(4)
l1.append(3)
l1.display()


l2 = linked_list()
l2.append(5)
l2.append(6)
l2.append(4)
l2.display()


#sum = []
carry = 0
value = 0
current1 = l1.head
current2 = l2.head
l3 = linked_list()

while current1.next != None and current2.next != None:
    current1 = current1.next
    current2 = current2.next
    n1 = current1.data
    n2 = current2.data
    print('n1,n2',n1,n2)
    print('carry',carry)
    value = (n1+n2)%10
    add = value + carry
    carry = (n1+n2)//10

    print('add',add)
    l3.append(add)
#print(int(''.join([str(x) for x in sum][::-1])))
