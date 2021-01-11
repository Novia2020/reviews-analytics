data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data. append (line)
		count += 1 
		if count % 10000 == 0:#%是用來求餘數-如果count和1000餘數為0
			print(len(data))
print('檔案讀取結束,總共有', len(data), '筆檔案')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))
	
new = []#一個新的清單叫new
for d in data:#data是1百萬筆的清單檔,d是每一筆的留言
    if len(d) <100:#假如長度小於100的留言
    	new.append(d)#則加入這個new清單裏
print('一共有', len(new), '筆留言長度小於100個字元')#最後印出這個小於100的留言清單有多少筆(len(new))
print(new[2])
