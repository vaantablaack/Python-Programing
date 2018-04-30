n1 = int(input('Enter the starting range:'))
n2 = int(input('Enter the ending:'))
for i in range (n1, n2+1):
  for num in range (2,i):
   if (i%num)==0:
     break
   else:
    print(i)
