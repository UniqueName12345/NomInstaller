import githandler
import os

noml = githandler.GitRepo('https://github.com/GenericProgrammer1234/Noml/')

try:
    path = input('Enter path to install noml to: ')
    print(f"Path entered: {path}")
    noml.clone()
    os.chdir(path)
except Exception as e:
    print(f"An error occurred: {e}")

def add_to_pythonpath(path):
    try:
        pythonpath = os.environ.get('PYTHONPATH', '')
        if pythonpath:
            pythonpath += os.pathsep
        pythonpath += path
        os.environ['PYTHONPATH'] = pythonpath
        print(f"PYTHONPATH set to: {os.environ['PYTHONPATH']}")
    except Exception as e:
        print(f"An error occurred: {e}")

def alias_noml(script_path):
    os.environ['PATH'] += os.pathsep + script_path
    print(f"PATH set to: {os.environ['PATH']}")

add_to_pythonpath(path)
alias_noml(path)