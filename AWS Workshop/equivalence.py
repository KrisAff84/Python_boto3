import json

# This uses a json string as input
json_string = """
{
    "Input":[
        {
        "Text":"Wilder is going to school tomorrow",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr"
        }
    ]
}
"""

# We use loads as we are loading from a string.
json_input = json.loads(json_string)

# Defines two variables to store the language code from the input.
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# The if statement checks to see if the language code is the same as the source code
if SourceLanguageCode == TargetLanguageCode:
    print('The SourceLanguageCode is the same as the TargetLanguageCode - stopping')
else:
    print('The Source Language and Target Language codes are different - proceeding')
