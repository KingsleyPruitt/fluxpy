# setup.py

from setuptools import setup, find_packages

setup(
    name="fluxpy",  # Package name is fluxpy
    version="0.1.0",  # Version of the package
    packages=find_packages(),  # This finds all the submodules
    install_requires=[],  # List any dependencies here
    author="Your Name",
    author_email="your_email@example.com",
    description="A simple package for fluxpy functionality",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fluxpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

