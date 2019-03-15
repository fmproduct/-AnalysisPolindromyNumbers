
def reverse(data):
	s = str(data)
	return int(s[::-1]);

def isPolindrome(d):
	return reverse(d) == d

i = 0
f = open("note.txt", "w+")
x = 10
y = 9000000000000000000

for j in range(x,y):
	f.write('------------------------------------------ \r\n')
	f.write('original:	'+str(j)+"\r\n")

	while not isPolindrome(j):
		if i > 1000:
			break
		i = i + 1
		j = j + reverse(j)

	if i < 1000:
		f.write('iterations:	'+str(i)+"\r\n")
	else:
		f.write("iterations:	 1000+\r\n")
	f.write('output:		'+str(j)+"\r\n")
	i = 0
f.close();