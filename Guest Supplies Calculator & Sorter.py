allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'steak sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests,item):
	numBrought=0
	for k , v in guests.items():
		numBrought=numBrought+v.get(item,0)
	return numBrought
items_to_check = ['apples', 'cups', 'steak sandwiches', 'apple pies', 'pretzels']
results_liste=[]
for i in items_to_check:
	count=totalBrought(allGuests,i)
	results_liste.append([count,i])
results_liste.sort(reverse=True)
print('Number of things being brought:')
for count , item in results_liste:
	print('- '+item+ ':'+str(count))