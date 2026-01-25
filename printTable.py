tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
counts=[]
def printTable(table):
	colwidths=[0]*len(table)
	for i in range(len(table)):
		for item in table[i]:
			if len(item)>colwidths[i]:
				colwidths[i]=len(item)
	for x in range(len(table[0])):
		for y in range(len(table)):
			print(table[y][x].ljust(colwidths[y]),end=' ')
		print()
--------------------------------------------------------
printTable(tableData)