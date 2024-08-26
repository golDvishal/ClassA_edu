import time as t
def you(str):
  for i in str:
    t.sleep(0.5)
    print(i,end="")
  return "code end "

data=input("enter your data: ")
print(you(data))
