import pathlib

from setuptools import setup, find_packages
from file_crawler  import __version__

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="file_crawler",
    version=__version__,
    description="Python application that can be used to copy files of a given file type from a folder directory.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tharindu.dev",
    author_email="tharindu.nm@yahoo.com",
    url="https://github.com/truethari/file-crawler",
    keywords="files copy directory crawl",
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/truethari/file-crawler/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    packages=['file_crawler'],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "file-crawler=file_crawler.__main__:main",
        ]
    },
)
