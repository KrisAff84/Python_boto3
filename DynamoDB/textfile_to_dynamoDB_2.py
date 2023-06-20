import boto3


def textfile_to_list(txt_file, delimiter):
    file = open(txt_file)
    textlist = []
    for line in file:
        l = line.strip('\n')
        textlist.append(l.split(delimiter))
    return textlist

    
def add_items_to_table(table, txt_file, delimiter):
    textlist = textfile_to_list(txt_file, delimiter)
    ddb = boto3.client('dynamodb')
    totalsize = 0
    for entry in textlist:
        singer = entry[2]
        song = entry[0]
        key = entry[1]
        if len(entry) > 3:
            review = 'Review'
        elif len(entry) <= 3:
            review = ' '
        totalsize += 1
        response = ddb.put_item(
            TableName=table,
            Item={
                'Singer': {
                    'S': singer,
                },
                'Song': {
                    'S': song,
                },
                'Key': {
                    'S': key,
                },
                'Review': {
                    'S': review,
                },
            },
        )
    return response


def main():
    txt_file = 'Python_boto3/DynamoDB/song_list.txt'
    delimiter = ':'
    table = 'Songs'
    add_items_to_table(table, txt_file, delimiter)
    
    
if __name__ == '__main__':
    main()
    