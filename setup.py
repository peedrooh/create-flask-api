import pathlib
from setuptools import setup, find_packages


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

packages = find_packages()

package_data = {'': ['*']}

install_requires = ['pyfiglet>=0.8.post1,<0.9', 'PyInquirer>=1.0.3,<2.0.0', 'toml>=0.10.1,<0.11.0']

entry_points = {'console_scripts': ['create-flask-api=create_flask_api.__main__:main']}

setup(
    name='create-flask-api',
    version='0.0.6',
    description='This is a create-react-app analog that creates a base Flask Aplication structure with boilerplates.',
    long_description_content_type="text/markdown",
    long_description=README,
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