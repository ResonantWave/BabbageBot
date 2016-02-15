===========
Babbage Bot
===========

Simple bot for Slack written in Python

Installation
============

Install the needed dependencies with pip.

In case that you don't have pip, then do ``apt-get install update && apt-get install python-pip`` on Debian based systems.

In order to install them, invoke pip as follows::

  pip install -r requirements.txt

If you do not want to install the dependencies globally, use a virtualenv (you will need python-virtualenv or a similar package; or install virtualenv via pip globally)::

  virtualenv env
  source env/bin/activate
  pip install -r requirements.txt

The needed Python dependencies at the moment are:

   - `websocket-client`
   - `pyjokes` (https://github.com/pyjokes/pyjokes)
   - `wikipedia`

Also, `curl` is required for the `horoscope` module.

An API token is required to run this bot. Check out https://api.slack.com/ for more information on how to create and obtain a token.
Once you have this token, replace the ``TOKEN`` variable in `main.py`_ with your Slack bot token, or run the application with a ``TOKEN`` environment variable.

Also, please obtain an http://openweathermap.org/ API key if you want to use the ``weather`` command. Replace it in `modules/weather.py`_

Usage
=====

Once installed, run it by calling `python main.py`. It will automatically connect and start listening to all incoming messages.


Adding commands
===============

Adding a command is pretty straightforward. First create a python file in the `modules`_ directory. Create the function ``execute(data)``. The data argument is required even if you don't use it. Inside the ``execute`` function, put all your code. Don't forget to add the imports!

After this, open `modules/list.py`_ and add an import with the name of the module you just created (eg: ``import shakespeareQuotes``). Then add an entry for the ``commandModules`` dictionary, using the same name of the import (eg: ``'quote' : shakespeareQuotes``). As you can see the name of the entry is the string that will be used as the filter, and the value is the command to be executed.

Contributors
============

Development:

* `NiXijav`

Small contributions:

* `ssaavedra`

Contributing
============

* The code is licensed under the `GNU Lesser GPL V3`_
* The project source code is hosted on `GitHub`_
* Please use `GitHub issues`_ to submit bugs and report issues
* Feel free to contribute to the code

.. _main.py: main.py
.. _modules/weather.py: modules/weather.py
.. _modules: modules
.. _modules/list.py: modules/list.py
.. _GNU Lesser GPL V3: LICENSE
.. _GitHub: https://github.com/ResonantWave/BabbageBot
.. _GitHub Issues: https://github.com/ResonantWave/BabbageBot/issues
