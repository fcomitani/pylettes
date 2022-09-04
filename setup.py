from setuptools import setup, find_packages
from codecs import open
from os import path

here    = path.abspath(path.dirname(__file__))
version = open("pylettes/_version.py").readlines()[-1].split()[-1].strip("\"'")

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='pylettes',

    version=version,

    description='Beautiful palettes in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/fcomitani/pylettes',
	download_url = 'https://github.com/fcomitani/pylettes/archive/'+version+'.tar.gz', 
    author='Federico Comitani',
    author_email='federico.comitani@gmail.com',

    license='GPL-3.0',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
	    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
	    'Programming Language :: Python :: 3.8'	
		],

    keywords=['palette', 'plotting', 'plots', 'color'], 

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['matplotlib>=1.3.1'],

    zip_safe=False,

)

