Displays the full path to the executable that pyenv will invoke when you run the given command:
$ pyenv which python3.3
/home/yyuu/.pyenv/versions/3.3.3/bin/python3.3


Lists all Python versions known to pyenv, and shows an asterisk next to the currently active version.
$ pyenv versions
2.5.6
2.6.8
* 2.7.6 (set by /home/yyuu/.pyenv/version)
3.3.3
jython-2.5.3
pypy-2.2.1

### How to display the currently active Python version, along with information on how it was set?

$ pyenv version
2.7.6 (set by /home/yyuu/.pyenv/version)

question id: 339e0ef5-94b0-4642-ba8c-7e44a3a8b282



Set a local application-specific Python version by writing the version name to a .python-version
file in the current directory.
This version overrides the global version, and can be overridden itself by setting the
PYENV_VERSION environment variable or with the pyenv shell command.
$ pyenv local 3.8


List the all available versions of Python, including Anaconda, Jython, pypy, and stackless
$ pyenv install --list


show local interpreter
$ pyenv local


Install a Python version
$ pyenv install 3.8.3

unset local version
$ pyenv local --unset


Lists all Python versions known to pyenv, and shows an asterisk next to the currently active version.
$ pyenv versions
2.5.6
2.6.8
* 2.7.6 (set by /home/yyuu/.pyenv/version)
3.3.3
jython-2.5.3
pypy-2.2.1