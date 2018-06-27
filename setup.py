from setuptools import setup

# https://caremad.io/2013/07/setup-vs-requirement/

with open('./requirements.txt') as r:
    # strip fixed version info from requirements file
    requirements = [line.split('=', 1)[0] for line in r]

setup(
    name='client-python',
    version='0.1.0',
    py_modules=['rancher'],
    url='https://github.com/rancher/client-python',
    license='MIT Style',
    description='Python client for the Rancher API',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'rancher = rancher:_main'
        ]
    }
)
