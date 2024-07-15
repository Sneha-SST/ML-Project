from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    This function will return the list of resquirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
print("Before setup")
setup(
    name='mlproject',
    version='0.0.1',
    author='Sneha',
    author_email='sst.snehashaji@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
print("After setup")