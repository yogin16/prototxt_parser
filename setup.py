from setuptools import setup, find_packages

setup(
    name="prototxt_parser",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['parsy'],

    package_data={},

    # metadata for upload to PyPI
    author="Yogin Patel",
    author_email="yogin.daiict@gmail.com",
    description="prototxt-parser allows to parse `*.prototxt` files to python dict objects",
    license="MIT",
    keywords="prototxt, dict",
    url="https://github.com/yogin16/prototxt_parser",  # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)