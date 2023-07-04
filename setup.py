from setuptools import find_packages,setup
from typing import List

NAME="housing predicter",
VERSION="0.0.1",
AUTHOR="Naveen Kumar",
DESCRIPTION="Complete ML project",
PACKAGES=["housing"],
file_path="requirements.txt"


def get_requirements_list()->List[str]:
    """
     It will get list of requirements.
    """
    with open(file_path) as file_obj:
        return file_obj.readlines().remove("-e .")

setup(
name=NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
author_email="snaveenkumar0312@gmail.com",
packages=PACKAGES,
install_requires=get_requirements_list(),
)

if __name__=="__main__":
    print(get_requirements_list())