file = open('Python_boto3/DynamoDB/song_list.txt')
textlist = {}
for line in file:
    counter = 0
    l = line.strip('\n')
    item = l.split('-')
    textlist[item[0]] = item[1], item[2]
for key, value in textlist.items():
    print(key, ':', value)

