a=[1,2,3,4,5]
b=[]
for i in range(len(a)):
	b.append({a[i],a[(i+1)%len(a)]})
print(b)
