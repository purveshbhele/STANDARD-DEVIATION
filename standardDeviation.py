import csv 
import math
with open("data.csv",newline='')as f:
        reader=csv.reader(f)
        file_data=list(reader)

data=file_data[0]

def mean(data):
        n=len(data)
        total=0
        for x in data:
            total=total+int(x)
        mean=total/n
        return mean


square=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    square.append(a)


sum=0
for i in square:
    sum=sum+i


result=sum/len(data)-1

std_deviation=math.sqrt(result)

print("Standard Deviation is "+str(std_deviation))