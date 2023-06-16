file = open('Python_boto3/DynamoDB/song_list.txt')
songlist = {}
for line in file:
    counter = 0
    l = line.strip('\n')
    song = l.split('-')
    songlist[song[0]] = song[1], song[2]
for key, value in songlist.items():
    print(key, ':', value)

