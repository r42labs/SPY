from setuptools import setup, find_packages

setup(
    name='SPY',
    version=0.1,
    package_dir={'':'.'},
    packages=find_packages(
        where='.'
    )
)
