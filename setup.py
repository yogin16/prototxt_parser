from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="prototxt_parser",
    version="0.1.6",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['parsy'],

    package_data={},

    # metadata for upload to PyPI
    author="Yogin Patel",
    author_email="yogin.daiict@gmail.com",
    description="prototxt-parser allows to parse *.prototxt files to python dict objects",

    license="MIT",
    keywords="prototxt, dict",
    url="https://github.com/yogin16/prototxt_parser",  # project home page

    # could also include long_description, download_url, classifiers, etc.
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)