#!/usr/bin/env python
"""Setup pymdown-lexers."""
from setuptools import setup, find_packages

entry_points = '''
[pygments.lexers]
uniview=pymdown_lexers:UniviewLexer
'''

setup(
    name='qupa-pymdown-lexers',
    version='1.0.0',
    description='Pygments lexer package for PyMdown.',
    author='Ajani Bilby',
    author_email='',
    url='https://github.com/qupa-project/pymdown-lexers',
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=[
        'Pygments>=2.0.1'
    ],
    zip_safe=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
