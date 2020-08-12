from setuptools import setup

# Use README.rst for the long description
with open('README.rst') as fh:
    long_description = fh.read()

# Scan the script for the version string
VERSION_FILE = 'hdlparse/minilexer.py'
VERSION = None
with open(VERSION_FILE) as fh:
    try:
        VERSION = [line.split('=')[1].strip().strip("'") for line in fh if \
            line.startswith('__version__')][0]
    except IndexError:
        pass

if VERSION is None:
    raise RuntimeError(
        'Unable to find version string in file: {0}'.format(VERSION_FILE))

setup(name='hdlparse-fork',
      version=VERSION,
      author='Elliott Villars',
      author_email='elliottvillars@gmail.com',
      description='HDL parser',
      long_description=long_description,
      platforms=['Any'],
      install_requires=[],
      packages=['hdlparse-fork'],
      py_modules=[],
      include_package_data=True,
      use_2to3=False,
      keywords='HDL parser',
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Operating System :: OS Independent',
          'Intended Audience :: Developers',
          'Topic :: Text Processing :: General', 'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: MIT License'
      ])
