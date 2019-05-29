from setuptools import setup
from setuptools import find_packages


setup(name='keras-rl2',
      version='1.0.1',
      description='Deep Reinforcement Learning for Tensorflow 2 Keras',
      author='Taylor McNally',
      author_email='taylor.mcnally@emory.edu',
      url='https://github.com/wau/keras-rl2',
      license='MIT',
      install_requires=['tf-nightly-2.0-preview'],
      extras_require={
          'gym': ['gym'],
      },
      packages=find_packages())
