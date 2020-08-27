#Merge sort
def msort(mylist, left, right):
	if right - left > 1:
		middle = (left + right)//2
		msort(mylist, left, middle)
		msort(mylist, middle, right)
		mlist(mylist, left, middle, right)

def mlist(mylist, left, middle, right):
	leftlist = mylist[left:middle]
	rightlist = mylist[middle:right]
	k = left
	i = 0
	j = 0
	while(left + i < middle and middle + j < right):
		if(leftlist[i] <= rightlist[j]):
			mylist[k]  = leftlist[i]
			i = i + 1
		else:
			mylist[k] = rightlist[j]
			j = j + 1
		k = k + 1
		if left + i < middle:
			while k < right:
				mylist[k] = leftlist[i]
				i = i + 1
				k = k + 1
		else:
			while k < right:
				mylist[k] = rightlist[j]
				j = j + 1
				k = k + 1

mylist = input('enter the unsorted list').split()
mylist = [int(x) for x in mylist]
msort(mylist,0,len(mylist)-1)
print(mylist)

