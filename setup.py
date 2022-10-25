from setuptools import setup 

setup(
    name='toftil-miepy',
    version='0.0.1',
    description=' Simple Mie theory for optics and acoustics. Includes vector spherical harmonics.',
    py_modules=['mie-acoustics'],
    package_dir={'': 'src'},
)