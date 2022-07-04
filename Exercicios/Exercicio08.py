


def mult(num1,num2):
  if num1 == 0 or num2 ==0:
    return 0
  elif num2==1:
    return num2
  else:
    return num1+ mult(num1,num2-1)

result = mult(5,4)
print(result)