============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given. 

Types of Contributions
----------------------

There are many ways to contribute in this project:

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/thinkingmachines/linksight-api-client/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* If you can, provide detailed steps to reproduce the bug.
* If you don't have steps to reproduce the bug, just note your observations in
  as much detail as you can. Questions to start a discussion about the issue
  are welcome.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "please-help" is open to whoever wants to implement it.

Please do not combine multiple feature enhancements into a single pull request.

Note: this project is very conservative, so new features that aren't tagged
with "please-help" might not get into core. We're trying to keep the code base
small, extensible, and streamlined. Whenever possible, it's best to try and
implement feature ideas as separate projects outside of the core codebase.

Write Documentation
~~~~~~~~~~~~~~~~~~~

LinkSight could always use more documentation, whether as part of the
official Cookiecutter docs, in docstrings, or even on the web in blog posts,
articles, and such.

If you want to review your changes on the documentation locally, you can do::

    pip install -r requirements-dev.txt
    cd docs
    make html

This will compile the documentation, open it in your browser and start
watching the files for changes, recompiling as you save.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/thinkingmachines/linksight-api-client/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `linksight-api-client` for local development.

1. Fork the `linksight-api-client` repo on GitHub.
2. Clone your fork locally

.. code-block:: shell

    git clone git@github.com:thinkingmachines/linksight-api-client.git

3. Install your local copy into a virtualenv. Assuming you have virtualenv installed, this is how you set up your fork for local development

.. code-block:: shell

   cd linksight-api-client   
   virtualenv venv
   source venv/bin/activate
   pip install -r requirements-dev.txt

4. Create a branch for local development

.. code-block:: shell

   git checkout -b name-of-your-bugfix-or-feature

Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox. In addition, ensure that your code is formatted using black

.. code-block:: shell

   flake8 linksight tests
   black linksight tests
   python setup.py test or py.test
   tox

To get flake8, black, and tox, just pip install them into your virtualenv. If you wish,
you can add pre-commit hooks for both flake8 and black to make all formatting easier.

6. Commit your changes and push your branch to GitHub

.. code-block:: shell

   git add .
   git commit -m "Your detailed description of your changes."
   git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Contributor Guidelines
----------------------

Pull Request Guidelines
~~~~~~~~~~~~~~~~~~~~~~~

Before you submit a pull request, check that it meets these guidelines:

1. There is an issue that the pull request corresponds to.
2. The pull request should include tests.
3. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
4. The pull request should work for Python 3.5 and 3.6

Coding Standards
~~~~~~~~~~~~~~~~

* We use PEP8 as our coding standard
* In addition, we use `black <https://github.com/ambv/black>`_ as our code formatter
