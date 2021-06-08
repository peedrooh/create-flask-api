import argparse
import pathlib

from pyfiglet import Figlet

from .project import ProjectSpecs
from .build import build


#  ---*--- Argparse Command Config ---*--- #
parser = argparse.ArgumentParser(description="Create Flask API")
parser.add_argument("project_name", type=str, help="Here you should insert the project name.")
parser.add_argument("-p", "--poetry", action="store_true", help="Create project with poetry.")


#  ---*--- Pyfiglet Command Config ---*--- #
figlet = Figlet(font='slant')


def initial_messages():
    print(figlet.renderText('Create Flask API'))
    print("This is a Flask API template generator command line interface.")
    print("To stop the execution just press 'ctr + C' at any time.\n\n\n")
    

def main():
    # try: 
    initial_messages()
    
    args = parser.parse_args()
    args.project_name = args.project_name.lower()
    project_path = str(pathlib.Path().absolute())
    
    project = ProjectSpecs(project_path, args)
    build(project)
    print("✨  Finished ✨\n")
        
    # except Exception as err:
    #     print("Something went wrong.")