from prompt_toolkit.validation import Validator, ValidationError

import re


class URLValidator(Validator):
    
    def validate(self, document):
            
        expression = ("((http|https)://)(www.)?" +
         "[a-zA-Z0-9@:%._\\+~#?&//=]" +
         "{2,256}\\.[a-z]" +
         "{2,6}\\b([-a-zA-Z0-9@:%" +
         "._\\+~#?&//=]*)")
        
        compiled_regex = re.compile(expression)
        
        if (document.text == None) or not re.search(compiled_regex, document.text):
            raise ValidationError(
                message='Please enter a valid url',
                cursor_position=len(document.text))


git_questions = [
    {
        'type': 'list',
        'qmark': ' 🌲 ',
        'message': 'Do you want to start a git repo?',
        'name': 'Git',
        'choices': [
            {
                'name': 'Yes',
                'value': True
            },
            {
                'name': 'No',
                'value': False
            }
        ],
    },
    {
        'type': 'input',
        'qmark': '   ',
        'message': 'Type the git remote repo URL:',
        'name': 'Repo',
        'validate': URLValidator
    },
    {
        'type': 'list',
        'qmark': '   ',
        'message': 'Add gitignore?',
        'name': 'Gitignore',
        'choices': [
            {
                'name': 'Yes',
                'value': True
            },
            {
                'name': 'No',
                'value': False
            }
        ],
    },
]

