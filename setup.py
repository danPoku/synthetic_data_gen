from setuptools import setup, find_packages

setup(
    name='synthetic_data_toolkit',
    version='0.1.0',
    description='A modular toolkit for generating synthetic datasets for respiratory disease incidence in Accra, Ghana.',
    author='Dan Gyinaye Poku',
    author_email='dan.gyinaye@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'toolkit': ['assumptions.yaml'],
    },
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib'
    ],
    python_requires='>=3.7',
)
