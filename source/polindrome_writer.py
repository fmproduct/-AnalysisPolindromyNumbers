
def reverse(data):
	s = str(data)
	return int(s[::-1]);

def isPolindrome(d):
	return reverse(d) == d

i = 0
x = 10
y = 9000

for j in range(x,y):
	print('------------------------------------------ \r\n')
	print('original:	'+str(j)+"\r\n")

	while not isPolindrome(j):
		if i > 1000:
			break
		i = i + 1
		j = j + reverse(j)

	if i < 1000:
		print('iterations:	'+str(i)+"\r\n")
	else:
		print("iterations:	 1000+\r\n")
	print('output:		'+str(j)+"\r\n")
	i = 0
input('close');