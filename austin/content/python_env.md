Title: Python development environment
Date: 2017-11-05 12:00
Category: Python

I haven't been programming in python for very long.  It has a lot of features that immediately drew me in over other languages.  
Most importantly, it enabled me to get things done.  However, when I started to use 3rd party packages, my project dependencies began to pollute my default python installation.

No one should have to worry about which of the four different versions of "requests" they are using in their python script.

After reading through this document, you will be able develop in python without having to worry about Python version, or dependency hell.

### What Tools do I Use 
#### 1. [Jetbrains PyCharmCE](https://www.jetbrains.com/pycharm/)
Some people prefer to use Vi, or Emacs and develop entirely within their terminal.  I am not one of those people.  I do not consider myself to be a native of *nix and need a little assistance to visualize file structures.

Pycharm is a python specific IDE with some great features.  It enables me to focus on the code and prevents my brain from context switching.
#### 2. [Pyenv](https://github.com/pyenv/pyenv)
[How to install pyenv](https://github.com/pyenv/pyenv#homebrew-on-mac-os-x)

I use pyenv to effortlessly switch between versions of python.  I really wanted to develop in Python 3.x, but was having difficulty dealing with macOS's default python 2.7 installation. 

######Using pyenv to install a new version of python
Pyenv makes it really easy to install a different version of python.
    
    austin $ pyenv

#### 3. [Virtualenv](https://virtualenv.pypa.io/en/stable/)
[How to install virtualenv](https://virtualenv.pypa.io/en/stable/installation/)