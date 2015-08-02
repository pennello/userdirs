Philosophy
----------
There ought to be fewer dot-files.  They are, after all, the result of
[a hack implemented by Ken or Dennis][1].  This module, in
`userdirs.py`, implements functionality for Unix-based command-line
programs to compute user-specific directories for data storage and
retrieval, configuration, and caches.  In addition, the module supports
arbitrary user-specific paths, meant to be generated in the Unix
filesystem manner.  The code is [XDG-compatible][2].

One simple approach is to create and use Unix-like paths in your home
directory, such as `etc` and `bin`.  Many users already do this.
Another approach is outlined in the [XDG Base Directory
Specification][2].

Functionality
-------------
This module provides a class you instantiate in your application at
runtime.  Call the `dir` method on it to generate appropriate
user-specific directories for your application to use.

    u = UserDirs()
    etcdir = u.dir('etc')
    dbdir  = u.dir('var','db')
    # ...

Documentation
-------------
The `userdirs` module itself has more detailed PyDoc documentation.

Testing
-------
The tests just run through the different configuration and method
invocation combinations and dump the output for quick manual
verification.  More automated verification may be useful.  Run `make
test` to run the tests.

[1]: https://plus.google.com/+RobPikeTheHuman/posts/R58WgWwN9jp
[2]: http://standards.freedesktop.org/basedir-spec/basedir-spec-0.6.html
