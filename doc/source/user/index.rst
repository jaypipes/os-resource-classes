=====
Usage
=====

`os-resource-classes` is primarily composed of a set of constants that may be
referenced by simply importing the ``os_resource_classes`` module and
referencing one of the module's constants::

    $ python
    Python 2.7.11+ (default, Apr 17 2016, 14:00:29)
    [GCC 5.3.1 20160413] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import os_resource_classes as orc
    >>> print orc.VCPU
    <ResourceClass(name=VCPU, code=0)>
