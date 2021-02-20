from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="listcord.py",
    url="https://github.com/listcordteam/listcord.py",
    version="1.5.0",
    description="Simple listcord api wrapper for python!",
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=['listcord'],
    keywords="listcord",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    license="MIT",
)