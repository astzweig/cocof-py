from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='cocof',
    version="1.0.0",
    author='Astzweig UG(haftungsbeschränkt) & Co. KG',
    author_email='it@astzweig.de',
    description='Consistent CLI config file modifier',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/astzweig/cocof-py',
    keywords=['toml', 'yaml', 'json', 'terminal', 'cli', 'edit'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
        'Topic :: Database',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ]
)
