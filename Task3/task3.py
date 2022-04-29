
def subtract(str1, str2):

	res = ""
	n1 = len(str1)
	n2 = len(str2)


	str1 = str1[::-1]
	str2 = str2[::-1]
	carry = 0

	for i in range(0, n2):

		
		subst = int(str1[i]) - int(str2[i]) - carry

		if subst < 0:
			subst = subst + 10
			carry = 1
		
		else:
			carry = 0

		
		res += str(subst)

	for i in range(n2, n1):
		subst = int(str1[i]) - carry

		if subst < 0:
			subst = subst + 10
			carry = 1
		
		else:
			carry = 0

		res += str(subst)

	return res[::-1]

def NumberOfWays(a):

	if a == "1":
		return a
		
	else:
		
		a = subtract(a, "1")
		carry = 0

		
		a = list(a[::-1])
		
		
		for i in range(0, len(a)):
			tmp = (int(a[i]) * 2) + carry
			a[i] = str(tmp % 10)
			carry = tmp // 10
		
		
		a = ''.join(a)
		if carry > 0:
			a += str(carry)

		return a[::-1]

if __name__ == "__main__":

	a = "12345678901234567890"
	print(NumberOfWays(a))


