from setuptools import setup

from mountapi import version


package_info = {
    'name': version.__name__,
    'version': version.__version__,
    'description': version.__description__,
    'author': version.__author__,
    'author_email': version.__author_email__,
    'url': version.__url__,
    'license': version.__license__,
}

with open('README.rst', 'r') as f:
    readme = f.read()

packages = ['mountapi', 'mountapi/core']

setup(
    name=package_info['name'],
    version=package_info['version'],
    description=package_info['description'],
    long_description=readme,
    author=package_info['author'],
    author_email=package_info['author_email'],
    url=package_info['url'],
    packages=packages,
    license=package_info['license'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
