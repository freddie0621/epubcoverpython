from distutils.core import setup
import py2exe, sys, os,PIL,urllib,zipfile

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'optimize': 2}},
    windows = [{'script': "epub-thumbnailer.py"}],
    zipfile = "shared.lib",
)