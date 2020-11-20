import os

from setuptools import find_packages, setup

def local_file(name):
	return os.path.relpath(os.path.join(os.path.dirname(__file__), name))

with open("requirements.txt") as f:
	required = f.read().splitlines()

setup(
   name="pomodoro_bot",
   packages=find_packages(exclude=["tests"]),
   install_requires=required,
   version="0.0.1",
   author="Alice Yang",
   python_requires=">=3.7",
   extras_require={
	"dev": [
	     "bandit=1.6.2", 
	     "black==19.10b0", 
	     "flake8==3.8.3",
	     "flake8-bandit==2.12",
	     "flake8-bugbear==20.1.4",
	     "flake8-builtins==1.5.3",
	     "flake8-comprehensions==3.2.3",
	     "isort==5.2.0",
	     "pre-commit==2.6.0"
	] 
	}
)
