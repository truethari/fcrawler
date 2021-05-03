import pathlib

from setuptools import setup, find_packages
from fcrawler  import __version__

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="fcrawler",
    version=__version__,
    description="Python application that can be used to copy files of a given file type from a folder directory.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tharindu.dev",
    author_email="tharindu.nm@yahoo.com",
    url="https://github.com/truethari/fcrawler",
    keywords="files copy directory crawl",
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/truethari/fcrawler/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    packages=['fcrawler'],
    include_package_data=True,
    install_requires=["pyfiglet"],
    entry_points={
        "console_scripts": [
            "fcrawler=fcrawler.__main__:main",
        ]
    },
)
