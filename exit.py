count=0
while True:
    number=input(" Please enter your desired number : ")
    if number=="exit":
        break
    else:
        number=int(number)
        count+=number
print(" Your total is equal to : ",count)
