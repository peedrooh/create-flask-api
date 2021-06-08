import secrets

auth_questions = [
    {
        'type': 'list',
        'qmark': ' 🔑 ',
        'message': 'Select authentication library:',
        'name': 'Authentication',
        'choices': [
            {
                'name': "JWT-Extended",
                'value': 'JWT-Extended'
            },
            {
                'name': "No authentication lib",
                'value': False
            }
        ],
    },
    {
        'type': 'list',
        'qmark': '   ',
        'message': 'Do you want to add a auto gernerated SECRET_KEY?',
        'name': 'SECRET_KEY',
        'choices': [
            {
                'name': 'Yes',
                'value': secrets.token_hex(16)
            },
            {
                'name': 'No',
                'value': False
            }
        ],
    },
]