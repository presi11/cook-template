from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="cook-template",
    description="null",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Juan Esteban Ospina Escobar",
    url="https://github.com/presi11/cook-template",
    project_urls={
        "Issues": "https://github.com/presi11/cook-template/issues",
        "CI": "https://github.com/presi11/cook-template/actions",
        "Changelog": "https://github.com/presi11/cook-template/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["cook_template"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
