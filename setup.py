from setuptools import setup

setup(
    name='spacy-depmatcher-pattern-visualiser',
    version='0.1',
    packages=['sdpv', 'sdpv.nxpd', 'sdpv.nxpd.pydot'],
    url='https://github.com/Jacobe2169/spacy-depmatcher-pattern-visualiser',
    license='MIT',
    author='Jacques Fize',
    author_email='jacques.fize@gmail.com',
    description='Python module to visualize pattern used in Spacy Dependency Matcher',
    install_requires = open("requirements.txt").read().strip().split("\n")
)
