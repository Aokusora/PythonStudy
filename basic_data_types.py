print('1024 * 768 =',1024*768)

a=-5



def function_a(x):
	return x+1;

function_a(a>=-5)

if function_a(a >= 0):
	print(a)
else:
	print(-a)

print('I\'m OK!')

print(r'\\abc\\')

L = ['1','2','9']
print(L[1])
for x in L:
	print(x)

height = 1.75
weight = 80.5
bmi = weight/height/height
if bmi < 18.5:
	print('过轻')
elif bmi < 25:
	print('正常')
elif bmi < 28:
	print('过重')
elif bmi < 32:
	print('肥胖')
else:
	print('严重肥胖')

sum = 0
# L = [1, ..., 10, 1]
for x in [1,2,3,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

sum=0
for x in range(101):
	sum = sum + x
print(sum)

sum = 0
n = 99
while (n>0):
	sum = sum+n
	n = n-2
print(sum)

L = ['Bart','Lisa','Adam']
for name in L:
	print('hello,',name)

n = 1
while n <= 10:
	if n > 6:
		break
	print(n)
	n = n+1
print('END')

n = 0
while n < 10:
	n = n+1
	if n % 2 == 1:
		continue
	print (n)
print('End')

