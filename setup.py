from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

__version__ = "0.1.4"

download_url = "https://github.com/alesanmed-educational-projects/covid-data/archive/refs/tags/{}.tar.gz".format(
    __version__
)

setup(
    name="covid_data",
    packages=["covid_data"],
    version=__version__,
    license="The Unlicense",
    description="Data loader part of the mid-project for the Data Science bootcamp from Core Code School",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="alesanchez",
    author_email="hi@alesanchez.es",
    url="https://github.com/alesanmed-educational-projects/covid-data",
    download_url=download_url,
    keywords=["covid", "core"],
    install_requires=[
        "pandas",
        "beautifulsoup4",
        "click",
        "python",
        "requests",
        "psycopg2",
        "Unidecode",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Programming Language :: Python :: 3.9",
    ],
)
