x = [(sum(list(int(i) for i in (input('Input num ').split(' '))))) for _ in range(5)]
# for i in range(4):
#     x.append(sum(list(int(i) for i in (input('Input num ').split(' ')))))
print(x.index(max(x))+1,max(x))
