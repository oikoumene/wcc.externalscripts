wcc.externalscripts Installation
--------------------------------

To install wcc.externalscripts using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``wcc.externalscripts`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        wcc.externalscripts

* Re-run buildout, e.g. with:

    $ ./bin/buildout

