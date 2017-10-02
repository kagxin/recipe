from setuptools import setup


# Remove build status and move Gitter link under title for PyPi

setup(
    name='test_setup',
    version='0.0.1',
    author='kagxin',
    author_email='kagxin@gmail.com',

    description='just for test setup.py',
    long_description='readme',
    url='http://github.com/kagxin/recipe/test_setup/',
    license='BSD',

    packages=['test_setup'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ]
)