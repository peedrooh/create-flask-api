from os.path import join


def ma_fix(project):
    return [
        {
            'file_path': join(project.app_path, 'configurations', '__init__.py'),
            'lines_to_fix': [
                """
    serializer.init_app(app)""", 
                ', serializer'
            ],
            'fixed_lines': [
                '',
                ''
            ]
        },
        {
            'file_path': join(project.app_path, 'views', 'user_view.py'),
            'lines_to_fix': [
                'from app.serializers.user_serializer import UserSchema', 
                'UserSchema().dump(user)'
            ],
            'fixed_lines': [
                'from app.serializers.user_serializer import UserSerializer', 
                'UserSerializer(user)'
            ] 
        }
    ]