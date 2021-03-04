import sys
from setuptools import setup

if sys.version_info.major != 3:
    raise RuntimeError("This package requires Python 3+")

# https://caremad.io/2013/07/setup-vs-requirement/

with open('./requirements.txt') as r:
    # strip fixed version info from requirements file
    requirements = [line.split('=', 1)[0] for line in r]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='client-python',
    version='0.2.0',
    py_modules=['rancher'],
    url='https://github.com/rancher/client-python',
    license='MIT Style',
    description='Python client for the Rancher API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
    ]
)
