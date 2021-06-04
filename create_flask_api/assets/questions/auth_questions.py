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
]