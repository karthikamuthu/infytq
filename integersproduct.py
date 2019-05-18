def find_product(num1,num2,num3):
    product=0
    if(num1!=7 and num2!=7 and num3!=7):
        product=(num1*num2*num3)
    elif(num1==7):
        product=num2*num3
    elif(num2==7):
        product=num3
    else:
        invalid
