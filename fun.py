#total=0  code1
#for number in range(1,10+1):
   # print(number)
   # total=total+number
#print(total)
#def add_numbers(): code2
   # total=0
   # for numbers in range(1,11):
        #print(numbers)
        #total=numbers+total
    #return total
#answer=add_numbers()
#print(answer)

#def add_numbers():#start,end  code3
   # start=333
        
   # for numbers in range (333,778):
       # start=numbers+start
    #return(start)
#answer=add_numbers()
#print(answer)
def add_numbers(start,end):
    beg=0
    for numbers in range (start,end+1):
        beg=beg+numbers
    return beg
test1=add_numbers(333,777)
print(test1)
test2=add_numbers(1,100)
print(test2)
test3=add_numbers(1,2)
print(test3)



    
        
