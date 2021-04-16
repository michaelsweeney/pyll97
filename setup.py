
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyll97", 
    version="0.0.1",
    author="Michael Sweeney",
    author_email="michael.samuel.sweeney@gmail.com",
    description="simple calculator for NYC LL97 fines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michaelsweeney/pyll97",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)