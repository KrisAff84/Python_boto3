import boto3

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    translated_text = response['TranslatedText']
    print(f'Translated Text: {translated_text}')
    
kwargs={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"es"
}

def main():
    translate_text(**kwargs)

if __name__ == "__main__":
    main()
