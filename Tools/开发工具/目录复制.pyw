import os
import subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def copy_current_directory():
    current_directory = os.getcwd()
    subprocess.run(['clip'], input=current_directory.strip().encode('utf-16'), check=True)

if __name__ == "__main__":
    copy_current_directory()
