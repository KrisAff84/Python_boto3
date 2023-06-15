import boto3
import argparse 

# Define the parser variable to equal argparse..ArgumentParser()
parser = argparse.ArgumentParser(description='Translate text from one language to another')

# Add each of the arguments using parser.add_argument() method
parser.add_argument(
    '--text', 
    dest='Text',
    type=str,
    help='The text you want to translate. The text string can be a maximum of 5,000 bytes long.',
    required=True
    )

parser.add_argument(
    '--slc', 
    dest='SourceLanguageCode',
    type=str,
    help='The language code for the language of the source text. The language must be a language supported by Amazon Translate.',
    required=True
    )
    
parser.add_argument(
    '--tlc',
    dest='TargetLanguageCode',
    type=str,
    help='The language code requested for the language of the target text. The language must be a language supported by Amazon Translate.',
    required=True
    )
    
# This will inspect the command line, convert each argument to the appropriate type and then invoke the appropriate action.
args = parser.parse_args()

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    translated_text = response['TranslatedText']
    print(f'Translated Text: {translated_text}')
    
def main():
   # vars() is an inbuilt function which returns a dictionary object
   translate_text(**vars(args))
   
if __name__ == "__main__":
    main()
