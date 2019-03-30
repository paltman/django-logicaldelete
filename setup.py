from setuptools import find_packages, setup

VERSION = "4.0"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/blank.svg
    :target: https://pypi.python.org/pypi/pinax-models/

============
Pinax Models
============

.. image:: https://img.shields.io/pypi/v/pinax-models.svg
    :target: https://pypi.python.org/pypi/pinax-models/

\ 

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-models.svg
    :target: https://circleci.com/gh/pinax/pinax-models
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-models.svg
    :target: https://codecov.io/gh/pinax/pinax-models
.. image:: https://img.shields.io/github/contributors/pinax/pinax-models.svg
    :target: https://github.com/pinax/pinax-models/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-models.svg
    :target: https://github.com/pinax/pinax-models/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-models.svg
    :target: https://github.com/pinax/pinax-models/pulls?q=is%3Apr+is%3Aclosed

\ 

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/pinax-models/

\ 

``pinax-models`` provides support for logical deletes on models and in the Django admin.
 
Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+-----+
| Django / Python | 2.7 | 3.4 | 3.5 | 3.6 |
+=================+=====+=====+=====+=====+
|  1.11           |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
|  2.0            |     |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxprojects.com",
    description="Provide Support for Logical Deletes on Models and in the Django Admin",
    name="pinax-models",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-models/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "models": []
    },
    test_suite="runtests.runtests",
    tests_require=[
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)