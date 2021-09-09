from typing import List
from setuptools import setup, find_packages


def get_dependencies() -> List[str]:
    with open("requirements.txt") as file:
        dep = map(lambda x: x.strip(), file.readlines())
        return dep


setup(
    name="avito_backend_test",
    version="0.0.1",
    packages=find_packages(where="src"),
    install_requires=get_dependencies(),
    package_dir={"": "src"},
)
