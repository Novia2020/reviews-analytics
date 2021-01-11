data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data. append (line)
		count += 1 
		if count % 1000 == 0:#%是用來求餘數-如果count和1000餘數為0
			print(len(data))
print('檔案讀取結束,總共有', len(data), '筆檔案')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))
	
