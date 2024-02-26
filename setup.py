from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='ssave',
      version='v1.0.3',
      long_description=readme()
      url='https://github.com/SCOS-Apps/Save-Utility',
      readme="README.md",
      keywords = ["save", "scos", "ssave"],
      packages=["ssave"],
      zip_safe=False)