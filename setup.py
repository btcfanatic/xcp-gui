"""
This is a setup.py script generated by py2applet

Usage (Mac OS X):
    python setup.py py2app

Usage (Windows):
    python setup.py py2exe
"""
#import ez_setup
#ez_setup.use_setuptools()

import sys
from setuptools import setup
from constants import APP_NAME
MAIN_SCRIPT = 'gui.py'

if sys.platform == 'darwin':
    extra_options = dict(
        setup_requires=['py2app'],
        app=[MAIN_SCRIPT],
        # Cross-platform applications generally expect sys.argv to
        # be used for opening files.
        options={'py2app': dict(argv_emulation=True, includes=['sip', 'cherrypy.wsgiserver.wsgiserver3', 'PyQt5._qt', 'PyQt5.QtCore', 'PyQt5.QtWidgets', 'PyQt5.QtGui'])},
    )

elif sys.platform == 'win32':
    extra_options = dict(
        setup_requires=['py2exe'],
        app=[MAIN_SCRIPT],
    )
else:
    extra_options = dict(
        # Normally unix-like platforms will use "setup.py install"
        # and install the main script as such
        scripts=[MAIN_SCRIPT],
    )

setup(
    name=APP_NAME,
    **extra_options
)
