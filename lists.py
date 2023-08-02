friends = []
print('Enter five names: ')
for looper in [1, 2, 3, 4, 5]:
    friend = input()
    friends.append(friend)

temp = ''
for friend in friends:
    temp = temp + ", " + friend

print('The names are ' + temp)

#a = "tony"
#b = " "
#c = "paul"
#print (a + b + c)