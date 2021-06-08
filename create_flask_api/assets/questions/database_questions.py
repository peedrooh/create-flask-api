db_questions = [
    {
        'type': 'list',
        'qmark': ' 🗃️ ',
        'message': 'Select a database:',
        'name': 'Database',
        'choices': [
            {
                'name': "Postgresql",
                'value': "Postgresql"
            },
            {
                'name': "SQLite",
                'value': "SQLite"
            },
            {
                'name': "No database",
                'value': False
            }
        ],
    }
]

postgresql_questions = [
    {
        'type': 'input',
        'qmark': '   ',
        'message': 'Type the database name:',
        'name': 'psql_db',
    },
    {
        'type': 'input',
        'qmark': '   ',
        'message': 'Type your postgresql user:',
        'name': 'psql_user',
    },
    {
        'type': 'input',
        'qmark': '   ',
        'message': 'Type your postgresql password:',
        'name': 'psql_password',
    },
]

sqlite_questions = [
    {
        'type': 'input',
        'qmark': '   ',
        'message': 'Type a database name:',
        'name': 'sqlite_db',
    }
]