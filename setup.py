# setup.py

from setuptools import setup, find_packages

setup(
    name="mypackage",  
    version="0.1.0",  
    packages=find_packages(),
    install_requires=[],  # List any dependencies here
    author="Your Name",
    author_email="your_email@example.com",
    description="A simple package to greet users",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mypackage",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
