from setuptools import setup, find_packages


packages = find_packages()

package_data = {'': ['*']}

install_requires = ['pyfiglet>=0.8.post1,<0.9', 'PyInquirer>=1.0.3,<2.0.0', 'toml>=0.10.1,<0.11.0']

entry_points = {'console_scripts': ['create-flask-api=create_flask_api.__main__:main']}

long_description = """# Create Flask API

"""


setup(
    name='create-flask-api',
    version='0.0.5',
    description='This is a create-react-app analog that creates a base Flask Aplication structure with boilerplates.',
    long_description='# Create Flask App\nThis is a create-react-app analog that creates a base Flask Aplication structure with boilerplates.\n# Usage\nAaaaaa',
    author='Pedro Henrique Germano Silva',
    author_email='pedrohenriquegs2001@gmail.com',
    maintainer=None,
    maintainer_email=None,
    url='',
    packages=packages,
    package_data=package_data,
    install_requires=install_requires,
    entry_points=entry_points,
    python_requires='>=3.7,<4.0',
)