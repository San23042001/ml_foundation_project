from typing import List
from setuptools import find_packages,setup


HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    in the requirements.txt there is -e . which will trigger setup.py
    '''
    requirements =  []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements      

setup(
    name='mlproject',
    version='0.0.1',
    author='Sanjay',
    author_email='shettysanjay719@gmail.com',
    packages=find_packages(), # will find in how many folder __inti__.py is there
    install_requires = get_requirements('requirements.txt')
)