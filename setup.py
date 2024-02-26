from setuptools import setup

setup(name='ssave',
      version='v1.0.3',
      description="SCOS Save Utility",
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      url='https://github.com/SCOS-Apps/Save-Utility',
      readme="README.md",
      keywords = ["save", "scos", "ssave"],
      packages=["ssave"],
      zip_safe=False)