def ssl3(list1):
  kel=sorted(list1)
  subl=[]
  if list1==[]:
    print("list is empty")
  elif len(list1)==1:
    print("1")
  else:
    for i in range(len(kel)):
      if kel[i]!=list1[i]:
        subl.append(i)
  s=len(list1[subl[0]:subl[-1]+1])
  print(s)

ssl3([0,1,4,3,8,9])
