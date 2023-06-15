import boto3

def translate_text(text, source_language_code, target_language_code):
    client = boto3.client('translate')
    response = client.translate_text(
    Text=text,
    SourceLanguageCode=source_language_code,
    TargetLanguageCode=target_language_code,
    )
    original_text = text
    translated_text = response['TranslatedText']
    print(f'Original Text: {original_text}')
    print()
    print(f'Translated Text: {translated_text}')

def main():
    translate_text('We are going to the store later today.',
                    'en', 'es')

if __name__ == "__main__":
    main()