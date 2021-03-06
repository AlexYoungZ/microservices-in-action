from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='account_transactions',
    version='0.0.1',
    description='Account Transactions microservice',
    long_description=long_description,
    url='https://github.com/pap/simplebank',

    author='Simplebank Engineering',
    author_email='engineering@simplebank.book',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',

        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],

    keywords='microservices orders',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'nameko==2.12.0',
        'logstash_formatter==0.5.17',
        'circuitbreaker==1.3.0',
        'gutter==0.5.0',
        'request-id==1.0',
        'statsd==3.3.0',
        'nameko-sentry==1.0.0',
        'pyopenssl==19.1.0',
        'Flask==1.1.2',
        'jaeger-client == 4.3.0',
        'requests==2.23.0',
        'opentracing==2.3.0',
        'opentracing_instrumentation==3.2.1',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
