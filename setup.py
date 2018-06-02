from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
with open("version.txt") as f:
    version = f.read()  # TODO: handle this better

setup(
    name='Tokage',
    author='SynderBlack',
    version="1.4",
    packages=['tokage'],
    license='MIT',
    description='Async wrapper for the MyAnimeList API',
    url='https://github.com/SynderBlack/Tokage',
    include_package_data=True,
    install_requires=requirements
)
