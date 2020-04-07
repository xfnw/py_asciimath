import re
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = re.search(
    r'^__version__\s*=\s*"(.*)"', open("py_asciimath/__init__.py").read()
).group(1)

setuptools.setup(
    name="py_asciimath",
    version=version,
    author="Federico Belotti",
    author_email="belo.fede@outlook.com",
    description="A simple converter from ASCIIMath to LaTeX",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/belerico/py-asciimath",
    packages=["py_asciimath", "tests"],
    entry_points={
        "console_scripts": ["py_asciimath=py_asciimath.py_asciimath:main"]
    },
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["lark-parser", "docopt"],
    python_requires=">=3.6",
)
