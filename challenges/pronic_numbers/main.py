# print ("Hello pronic numbers")
# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))

# for i in range(num1,num2):
#     # print (i)
#     # print (i+1)
#     # print (i*(i+1))

#     product = i*(i+1)

#     print(f"- {i} x {i+1} ={product}")


num = int(input("type a number"))
is_pronic = False

for i in range(1,num):

    product = i *  (i+1)

    if product == num:  
        print("this is a pronic number") 
        is_pronic = True
        break

if is_pronic == False:
    print("this is not a pronic number")


