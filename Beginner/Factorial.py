num=int(input('Enter the number'))
factorial = 1
if (num<0):
  print('No factorial for negative values')
elif(num==0):
  print('1')
else:
  for i in range (1,num+1):
    factorial= factorial*i
  print ('factorial is',factorial)
