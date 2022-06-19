

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of CF.setup.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


from setuptools import find_packages
from setuptools import setup


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="runawayClock",
  url="https://github.com/ComfortableSoftware/commonFunctions_py",
  version="0.9.3-1",
  package_dir={"runawayClock": "runawayClock"},
  package_data={
      "runawayClock": [
          "../doc/*",
          "BUTTONS_D/*",
          "CLOCKS_D/*",
      ]
  },
  packages=["runawayClock"],
  install_requires=[
      "CF",
      "PySimpleGUI",
  ],
  extras_require={
  },
  scripts=["scripts/runawayClock"],
)
