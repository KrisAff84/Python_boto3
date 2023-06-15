# Standard Imports
import argparse
import json

# 3rd Party Imports
import boto3 

# Arguments
parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True)

args = parser.parse_args()

# Functions
def open_input():
    """This function returns a dictionary containing the contents of the Input section in the input file""" 
    with open(args.filename) as file_object:
        contents = json.load(file_object)
    return contents['Input']

# Boto3 function to use Amazon Translate to translate the text and only return the Translated Text
def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText']) 

# Add a Loop to iterate over the json file.
def translate_loop():
    input_text = open_input()
    for item in input_text: # Here we iterate over all dictionaries in the Input list
        translate_text(**item)

# Main Function - use to call other functions
def main():
    translate_loop()

if __name__ == "__main__":
    main()

