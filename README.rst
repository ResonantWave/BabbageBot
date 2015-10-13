===========
Babbage Bot
===========

Simple bot for Slack written in Python

Installation
============

Install the following dependencies with pip.

In case that you don't have pip, then do ``apt-get install update && apt-get install python-pip`` on Debian based systems.

Required dependencies:

   - `websocket-client`
   - `pyjokes` (https://github.com/pyjokes/pyjokes)
   - `wikipedia`

An API token is required to run this bot. Check out https://api.slack.com/ for more information on how to create and obtain a token.
Once you have this token, replace the TOKEN variable in `main.py`_ with your Slack bot token.

Also, please obtain an http://openweathermap.org/ API key if you want to use the ``weather`` command. Replace it in `modules/weather.py`_

Usage
=====

Once installed, run it by calling `python main.py`. It will automatically connect and start listening to all incoming messages.


Contributors
============

Development:

* `NiXijav`

Contributing
============

* The code is licensed under the `GNU Lesser GPL V3`_
* The project source code is hosted on `GitHub`_
* Please use `GitHub issues`_ to submit bugs and report issues
* Feel free to contribute to the code

.. _main.py: main.py
.. _modules/weather.py: modules/weather.py
.. _GNU Lesser GPL V3: LICENSE
.. _GitHub: https://github.com/ResonantWave/BabbageBot
.. _GitHub Issues: https://github.com/ResonantWave/BabbageBot/issues
