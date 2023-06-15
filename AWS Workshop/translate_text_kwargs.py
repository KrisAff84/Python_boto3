import boto3

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    translated_text = response['TranslatedText']
    print(f'Translated Text: {translated_text}')


def main():
    translate_text(Text='I am going to the store', 
    SourceLanguageCode='en', TargetLanguageCode='fr')

if __name__ == "__main__":
    main()
