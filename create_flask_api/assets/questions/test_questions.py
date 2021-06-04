test_questions = [
    {
        'type': 'list',
        'qmark': ' 🔬 ',
        'message': 'Do you want to add a testing folder?',
        'name': 'Test',
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
        'type': 'checkbox',
        'qmark': '   ',
        'message': 'Select test library(ies):',
        'name': 'Test',
        'choices': [
            {
                'name': 'Pytest',
                'value': 'Pytest'
            },
            {
                'name': 'Unit Test',
                'value': 'Unit Test'
            }
        ],
    },
]