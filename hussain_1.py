given_iput = [1,2,2,3,3,4]
sum_ = given_iput[0]
for i in range(1,len(given_iput)):
	if given_iput[i] <= given_iput[i-1]:
		given_iput[i] += 1
		sum_ = sum_ + given_iput[i-1]
	else:
		sum_ = sum_ + given_iput[i]
		given_iput[i-1] = 


print(sum_)
