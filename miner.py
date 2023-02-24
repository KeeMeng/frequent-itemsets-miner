from itertools import combinations

max_size = 0
transcations = []
threshold = int(input("Input threshold: "))

line = input()
if ";" in line:
	all_items = line.split(";")
	line = input()
	while line != "":
		items = [all_items[i] for i in range(len(all_items)) if line[i] == "1"]
		transcations.append(sorted(items))
		if len(items) > max_size:
			max_size = len(items)
		line = input()
	
else:
	all_items = []
	while line != "":
		items = line.split(", ")
		transcations.append(sorted(items))
		[all_items.append(item) for item in items if item not in all_items]
		if len(items) > max_size:
			max_size = len(items)
		line = input()
		
	all_items.sort()

for size in range(1, max_size + 1):
	itemsets = combinations(all_items, size)
	for itemset in itemsets:
		support = 0
		for record in transcations:
			if all(item in record for item in itemset):
				support += 1
				
		if support >= threshold:
			print(f"{{{', '.join(itemset)}}}: {support}")
