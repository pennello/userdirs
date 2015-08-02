# chris 072315

'''UserDirs tests.

At the time of writing, it's not really worth it to make automated
verification of the correctness of the returned values.  So they're just
printed for manual verification.
'''

import os
import sys
import unittest

from contextlib import contextmanager
from userdirs import UserDirs

def log(x): sys.stderr.write('%s\n' % x)

vartypes = 'data','cache','config'
testpaths = (
  ('share',),
  ('etc',),
  ('var','cache'),
  ('lib',),
  ('tmp',),
  ('var','db'),
)

def cleanenv():
  for var in vartypes:
    os.environ.pop('XDG_%s_HOME' % var.upper(),'zuul')

@contextmanager
def whateverctx():
  for var in vartypes:
    os.environ['XDG_%s_HOME' % var.upper()] = 'xdg_whatever_%s' % var
  try: yield
  finally: cleanenv()

def logtest():
  for xdgstrict in True,False:
    log('xdgstrict %s' % xdgstrict)
    u = UserDirs(xdgstrict)
    for var in vartypes:
      log(getattr(u,var)())
    for testpath in testpaths:
      log(u.dir(*testpath))

class TestNoEnv(unittest.TestCase):
  def setUp(self): cleanenv()

  def test(self):
    '''
    Basically, just run through all the code paths without any
    environment variable overrides set.
    '''
    logtest()

class TestEnv(unittest.TestCase):
  def test(self):
    '''
    Run through all the code paths with environment variable overrides
    set.
    '''
    with whateverctx(): logtest()
