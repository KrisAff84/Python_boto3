import boto3

def translate_text(text):
    response = client.translate_text(
    Text=text,
    SourceLanguageCode='en',
    TargetLanguageCode='fr',
    )
    print(response)

def main():
    translate_text()

if __name__ == "__main__":
    
    client = boto3.client('translate')
    translate_text("I am learning to code in AWS")