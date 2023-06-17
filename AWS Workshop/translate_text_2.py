import boto3

def translate_text(text):
    response = client.translate_text(
    Text=text,
    SourceLanguageCode='en',
    TargetLanguageCode='fr',
    )
    original_text = text
    translated_text = response['TranslatedText']
    print(f'Original Text: {original_text}')
    print()
    print(f'Translated Text: {translated_text}')

def main():
    translate_text()

if __name__ == "__main__":
    
    client = boto3.client('translate')
    translate_text('We are going to the store later today.')