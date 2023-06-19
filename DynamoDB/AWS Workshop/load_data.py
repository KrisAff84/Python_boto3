import boto3
import json
import decimal


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal)
    total_movies = 0
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']
        
        total_movies += 1
        print("Adding movie:", year, title)

        table.put_item(
           Item={
               'year': year,
               'title': title,
               'info': info,
            }
        )
    print("Total Movies Added:", total_movies)
