Pinax Models
============
.. image:: http://slack.pinaxproject.com/badge.svg
   :target: http://slack.pinaxproject.com/

.. image:: https://img.shields.io/travis/pinax/pinax-models.svg
    :target: https://travis-ci.org/pinax/pinax-models

.. image:: https://img.shields.io/coveralls/pinax/pinax-models.svg
    :target: https://coveralls.io/r/pinax/pinax-models

.. image:: https://img.shields.io/pypi/dm/pinax-models.svg
    :target:  https://pypi.python.org/pypi/pinax-models/

.. image:: https://img.shields.io/pypi/v/pinax-models.svg
    :target:  https://pypi.python.org/pypi/pinax-models/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target:  https://pypi.python.org/pypi/pinax-models/
    
    
Pinax
--------

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. 
This collection can be found at http://pinaxproject.com.

This app was developed as part of the Pinax ecosystem but is just a Django app and can be used independently of other Pinax apps.


pinax-models
-------------

``pinax-models`` provides support for logical deletes on models and in the Django admin.

This is a small and simple app that Patrick Altman wrote to get some reuse out
of something he did in nearly every project and every model he created.  It's
too easy for good data to get deleted and it be unrecoverable.  It's also too
easy to fix this by overriding the model's delete() method and just flagging
records as deleted and then leveraging Django's managers to override default
behavior so that logically deleted items are not returned in querysets.

There are two exceptions to this rule, however, that are useful.

#. In the admin it is nice to see everything with an indicator of whether or not
   it has been deleted, with the ability to filter down to just active records,
   (or deleted for that matter).
#. It is a valid request when an item is fetched by its primary key value, that
   the object should return, even if it is marked as deleted.
   
   
History
--------

On May 25, 2015, Patrick donated ``django-logicaldelete`` to Pinax and as part of
that process, ``pinax-models`` was born and the code incorporated into that
package. It remains just a Django app and can be quite independently of other
Pinax apps.


Installation
-----------------------

::

    pip install pinax-models
    

Usage
------------------

Using the app is pretty simple:

#. add `pinax.models` to your INSTALLED_APPS
#. Inherit from ``pinax.models.LogicalDeleteModel`` for all models that you wish
   to share in this functionality.
#. Create and/or Register admins for each of these models using
   ``pinax.models.LogicalDeleteModelAdmin``


Additional
----------

Logical deletes are handled by date stamping a `date_removed` column.


Backwards Incompatible Changes
------------------------------

2.0
***

* Renamed to ``pinax-models`` and base model renamed to ``LogicalDeleteModel``


1.1
***

* Changed ``everything`` to ``all_with_deleted`` on LogicalDeleteManager
* LogicalDeleteManager moved from ``logicaldelete.models`` to ``logicaldelete.managers``
* Removed ``deleted`` and ``everything`` querysets from ``logicaldelete.models.Model``


Documentation
--------------

The ``pinax-models`` documentation is currently under construction. If you would like to help us write documentation, please join our Pinax Project Slack team and let us know! The Pinax documentation is available at http://pinaxproject.com/pinax/.


Contribute
----------------

See this blog post http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/ including a video, or our How to Contribute (http://pinaxproject.com/pinax/how_to_contribute/) section for an overview on how contributing to Pinax works. For concrete contribution ideas, please see our Ways to Contribute/What We Need Help With (http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our Pinax Slack team (http://slack.pinaxproject.com) and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our Open Source and Self-Care blog post (http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).  


Code of Conduct
----------------

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found here  http://pinaxproject.com/pinax/code_of_conduct/. We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


Pinax Project Blog and Twitter
-------------------------------

For updates and news regarding the Pinax Project, please follow us on Twitter at @pinaxproject and check out our blog http://blog.pinaxproject.com.













