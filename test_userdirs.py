# chris 072315

import os
import sys
import unittest

from contextlib import contextmanager
from userdirs import UserDirs

def log(x):
  sys.stderr.write('%s\n' % x)

fns = 'data','cache','config'

@contextmanager
def whateverctx():
  for fn in fns:
    os.environ['XDG_%s_HOME' % fn.upper()] = 'xdg_whatever_%s' % fn
  try: yield
  finally:
    for fn in fns:
      del os.environ['XDG_%s_HOME' % fn.upper()]

class TestCase(unittest.TestCase):
  def test_noenv(self):
    '''
    Just run through all modes and methods to make sure nothing blows
    up.
    '''
    modes = (
      'strict',
      'compat',
      None,
      '_zuul', # "Bad" value.
    )
    for mode in modes:
      u = UserDirs(mode)
      for fn in fns:
        x = getattr(u,fn)()
        log('%s, %s: %s' % (mode,fn,x))

  def test_env(self):
    '''
    Test environment precedence.
    '''

    with whateverctx():
      u = UserDirs(None)
      for fn in fns:
        log('%s: %s' % (fn, getattr(u,fn)()))
