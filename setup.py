from setuptools import setup, find_packages

NAME = 'Cherry'
VERSION = '0.0.1'
DESCRIPTION = 'Yet another pomodoro-type app'
AUTHOR = 'gedfalk'
EMAIL = 'blite.co.stn@gmail.com'

REQUIRED_PACKAGES = [
    'click',
    'rich',
    'configparser',
]

# EXTRA_PACKAGES...

with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()


setup(
    name=NAME,
    verion=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    # extras_require=EXTRA_PACKAGES,
    # classifiers...,
    py_modules=['launcher'],
    entry_points='''
        [console_scripts]
        cherry=launcher:main
    ''',
)
