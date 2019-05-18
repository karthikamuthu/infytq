def display(num):
    message=" "
    if(num%3==0 and num%5==0):
        message='Zoom'
    elif(num%5==0):
        message='Zip'
    elif(num%3==0):
        message='Zap'
    else:
        message="invalid"
    return message
message=display(11)   
print(message)
