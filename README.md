# Pinax Models

[![](https://img.shields.io/pypi/v/pinax-models.svg)](https://pypi.python.org/pypi/pinax-models/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-models.svg)](https://circleci.com/gh/pinax/pinax-models)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-models.svg)](https://codecov.io/gh/pinax/pinax-models)
[![](https://img.shields.io/github/contributors/pinax/pinax-models.svg)](https://github.com/pinax/pinax-models/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-models.svg)](https://github.com/pinax/pinax-models/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-models.svg)](https://github.com/pinax/pinax-models/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Table of Contents

* [About Pinax](#about-pinax)
* [Overview](#overview)
  * [Supported Django and Python versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Logical Deletion](#logical-deletion)
* [Change Log](#change-log)
* [Backwards Incompatible Changes](#backwards-incompatible-changes)
* [History](#history)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)


## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## pinax-models

### Overview

``pinax-models`` provides support for logical deletes on models and in the Django admin.

This is a small and simple app that Patrick Altman wrote to get some reuse out
of something he did in nearly every project and every model he created.  It's
too easy for good data to get deleted and it be unrecoverable.  It's also too
easy to fix this by overriding the model's delete() method and just flagging
records as deleted and then leveraging Django's managers to override default
behavior so that logically deleted items are not returned in querysets.

There are two exceptions to this rule, however, that are useful.

* In the admin it is nice to see everything with an indicator of whether or not
   it has been deleted, with the ability to filter down to just active records,
   (or deleted for that matter).
* It is a valid request when an item is fetched by its primary key value, that
   the object should return, even if it is marked as deleted.
   
#### Supported Django and Python versions

Django \ Python | 2.7 | 3.4 | 3.5 | 3.6
--------------- | --- | --- | --- | ---
1.11 |  *  |  *  |  *  |  *  
2.0  |     |  *  |  *  |  *


## Documentation

The ``pinax-models`` documentation is currently under construction. If you would like to help us write documentation, please join our Pinax Project Slack team and let us know! The Pinax documentation is available at http://pinaxproject.com/pinax/.

### Installation

To install pinax-models:

```shell
    $ pip install pinax-models
```

Add `pinax.models` to your `INSTALLED_APPS` setting:

```python
    INSTALLED_APPS = [
        # other apps
        "pinax.models",
    ]
```

### Usage

Using the app is pretty simple:

#. add `pinax.models` to your INSTALLED_APPS
#. Inherit from ``pinax.models.LogicalDeleteModel`` for all models that you wish
   to share in this functionality.
#. Create and/or Register admins for each of these models using
   ``pinax.models.LogicalDeleteModelAdmin``

### Logical Deletion

`pinax.models.models.LogicalDeleteModel` aims to provide a consistent interface for
managing logical deletion of models also reducing the need to implement
functionality at the model level.

* Logical Deletion instead of Physical Deletion
* Admin that can reveal which records are "Deleted" and allow you to reverse it.
* Provides some short cuts in the default manager

Logical deletes are handled by date stamping a `date_removed` column.  In
addition, a ``date_created`` and ``date_modified`` columns will be populated as a
convenience.


## Change Log

### 4.0

* Add Django 2.0 compatibility testing
* Drop Django 1.8, 1.9, 1.10, and Python 3.3 support
* Move documentation into README, standardize layout
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description


## Backwards Incompatible Changes

### 2.0

* Renamed to ``pinax-models`` and base model renamed to ``LogicalDeleteModel``

### 1.1

* Changed ``everything`` to ``all_with_deleted`` on LogicalDeleteManager
* LogicalDeleteManager moved from ``logicaldelete.models`` to ``logicaldelete.managers``
* Removed ``deleted`` and ``everything`` querysets from ``logicaldelete.models.Model``


## History

On May 25, 2015, Patrick donated ``django-logicaldelete`` to Pinax and as part of
that process, ``pinax-models`` was born and the code incorporated into that
package. It remains just a Django app and can be quite independently of other
Pinax apps.


## Contribute

For an overview on how contributing to Pinax works read this [blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/)
and watch the included video, or read our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section.
For concrete contribution ideas, please see our
[Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our [Pinax Slack team](http://slack.pinaxproject.com)
and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course
also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our blog post on [Open Source and Self-Care](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).


## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project
has a [code of conduct](http://pinaxproject.com/pinax/code_of_conduct/).
We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject)
and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-2019 James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).