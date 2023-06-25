from setuptools import find_packages,setup
from typing import list


HYPEN_E_DOT="-e ."
def get_requirements(file_path:str):
    ''' it will get list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for i in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

return requirements

setup(
name="ML Project"
version="0.0.1"
author="Naveen Kumar"
author_email="snaveenkumar0312@gmail.com"
package=find_packages()
install_requires=get_requirements()
)