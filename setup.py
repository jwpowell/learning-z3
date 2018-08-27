
from distutils.core import setup

setup(
    name='learn_z3',
    packages=['learn_z3'],
    install_requires=[
        'z3-solver',
    ],
    entry_points={
        'console_scripts' : ['learn_z3=learn_z3.cli:main']
    }
)