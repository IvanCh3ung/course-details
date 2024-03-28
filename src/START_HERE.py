import subprocess

def run_all():
    # Create a virtual environment
    subprocess.run(['python', '-m', 'venv', 'venv'])

    # Activate the virtual environment
    subprocess.run(['venv\\Scripts\\activate'], shell=True)

    # Install dependencies from requirements.txt
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

    # Run main.py
    subprocess.run(['python', 'src/do_it_all.py'])

if __name__ == "__main__":
    run_all()