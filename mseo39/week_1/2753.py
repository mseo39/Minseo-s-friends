y= int(input())
print(1 if(((y%4==0)&(y%100!=0))|((y%4==0)&(y%400==0))) else 0)