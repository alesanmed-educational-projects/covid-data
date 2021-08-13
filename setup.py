import os
import re
from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), "../", "pyproject.toml"), "r") as f:
    project_info = f.read()

    regex = r"version = \"(.*)\""

    __version__ = re.findall(regex, project_info)[0]


setup(
  name = 'covid_data',         # How you named your package folder (MyLib)
  packages = ['covid_data'],   # Chose the same as "name"
  version = __version__,      # Start with a small number and increase it with every change you make
  license='The Unlicense',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Data loader part of the mid-project for the Data Science bootcamp from Core Code School',   # Give a short description about your library
  author = 'alesanchez',                   # Type in your name
  author_email = 'hi@alesanchez.es',      # Type in your E-Mail
  url = 'https://github.com/alesanmed-educational-projects/core-data-covid-project',   # Provide either the link to your github or to your website
  download_url = f'https://github.com/alesanmed-educational-projects/core-data-covid-project/archive/v_{__version__}.tar.gz',    # I explain this later on
  keywords = ['covid', 'core'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
      'pandas',
      'beautifulsoup4',
      'click',
      'python',
      'requests',
      'psycopg2',
      'Unidecode',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Data Tools',
    'License :: OSI Approved :: The Unlicense',   # Again, pick a license
    'Programming Language :: Python :: 3.9',
  ],
)
