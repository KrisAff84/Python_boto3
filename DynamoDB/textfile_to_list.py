file = open('Python_boto3/DynamoDB/song_list.txt')

def textfile_to_list(txt_file, delimeter):
    file = open(txt_file)
    textlist = []
    counter = 0
    for line in file:
        l = line.strip('\n')
        textlist.append(l.split(delimeter))
        print(textlist[counter])
        counter += 1
    return textlist


def main():
    txt_file = 'Python_boto3/DynamoDB/song_list.txt'
    delimeter = ':'
    textlist = textfile_to_list(txt_file, delimeter)
    
        
if __name__ == '__main__':
    main()


# To get specific index of nexted list for all items in main list
    # for i in textlist:
    #     print(i[0])
    # print()
    # print("Kaela's Songs:")
    # for i in textlist:
    #     if i[2] == 'Kaela':
    #         print(i[0])
        