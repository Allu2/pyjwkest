.. _install:

Quick install guide
###################

<<<<<<< HEAD
Before you can use pyOIDC, you'll need to get it installed. This guide
will guide you to a simple, minimal installation.

Install pyJWKEST
================
=======
Before you can use PyOIDC, you'll need to get it installed. This guide
will guide you to a simple, minimal installation.

Install PyOIDC
==============
>>>>>>> d8858378e9d3351804dba5654444cc23b9e1c07c

For all this to work you need to have Python installed.
The development has been done using 2.7.
There will shortly be a 3.4 version.

Prerequisites
<<<<<<< HEAD
=============

For installing pyJWKEST you will need

* pycrypto
=======
==============

For installing pyOIDC you will need

* requests
* pycrypto
* pyjwkest
* pysaml2
* dirg-util
>>>>>>> d8858378e9d3351804dba5654444cc23b9e1c07c

To build the documentation you will need

* alabaster

and for running the examples:

<<<<<<< HEAD
* pycrypto
=======
* mako
* cherrypy
* beaker
* pyOpenSSL
* argparse
* importlib
* M2Crypto
* swig
>>>>>>> d8858378e9d3351804dba5654444cc23b9e1c07c

For running the tests you will additionally need to install:

* pytest

<<<<<<< HEAD
Debian/Mac
==========

If you don't want to install pyjwkest and all it's dependencies manually you can use yais
=======
If you wish your LDAP tests to pass, ensure you have installed the following package as well:

* python-ldap (not supported in windows)

Debian/Mac
==============
If you don't want to install pyoidc and all it's dependencies manually you can use yais
>>>>>>> d8858378e9d3351804dba5654444cc23b9e1c07c

Open a terminal and enter::

    git clone https://github.com/its-dirg/yais [your path]
    cd [your path]
    sudo python setup.py install
    cd [your path]/yais/script
    ./yais.sh

<<<<<<< HEAD
On the question “Do you want to install pyjwkest (Y/n):”, type Y. Everything else should be ignored, by typing n. The script will install pyoidc and all it's dependencies.
=======
On the question “Do you want to install pyoidc (Y/n):”, type Y. Everything else should be ignored, by typing n. The script will install pyoidc and all it's dependencies.
>>>>>>> d8858378e9d3351804dba5654444cc23b9e1c07c

Quick build instructions
------------------------

Once you have installed all the necessary prerequisites a simple::

    python setup.py install

will install the basic code.

Note for rhel/centos 6: cffi depends on libffi-devel, and cryptography on
openssl-devel to compile. So you might want first to do:
yum install libffi-devel openssl-devel

After this you ought to be able to run the tests without an hitch.
The tests are based on the pypy test environment, so::

    cd tests
    py.test

is what you should use. If you don't have py.test, get it it's part of pypy!
It's really good!
<<<<<<< HEAD
=======

Windows (beta)
==============

Above all pyoidc is developed and used in unix environments. In order to make it easier for people to use it in windows
environments a install script named install.bat has been developed which installs most of the necessary dependencies.
There are still some applications which is not included in .bat file like Python, Git, PyOpenSSL and Microsoft
Visual C++ Compiler.

NOTE: The script has been developed and used on windows 10.

A complete zip file containing all det executable files and the install script could be downloaded here:
https://dirg.org.umu.se/static/pyoidc_windows_install_full.zip

If you only want the install script it could be downloaded here:
https://dirg.org.umu.se/static/pyoidc_windows_install_script.zip

Start of by installing the program in the "Executables" folder. In order for it to work appropriate install the
applicaions in the following order.

1. python-2.7.9 		    (https://www.python.org/downloads/)
2. Git-1.9.5-preview 		(http://git-scm.com/downloads)
  2.1 On the "ajusting your path environment" page select "Use Git from the windows command prompt"
3. PyOpenSSL-0.13.1 		(https://pypi.python.org/pypi/pyOpenSSL/0.13.1#downloads)
4. VCForPython27 		    (http://aka.ms/vcpython27)

After installing the executable files go back to the root folder and run the file named install.bat

NOTE: If you are planing to start the .bat file from a command prompt make sure the command prompt where started after installing Git-1.9.5-preview.
>>>>>>> d8858378e9d3351804dba5654444cc23b9e1c07c
