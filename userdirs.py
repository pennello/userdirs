# chris 072315

import os

class UserDirs(object):
  def __init__(self,prog,xdgstrict=False):
    self.prog = prog
    self.xdgstrict = xdgstrict

  def env(self,key): return os.environ.get('XDG_%s_HOME' % key.upper())

  def home(self): return os.path.expanduser('~')

  def join(self,*a): return os.path.join(self.home(),*a)

  def data(self):
    xdg = self.env('data')
    if xdg is not None: return xdg
    if self.xdgstrict: return self.join('.local','share',self.prog)
    return self.join('var',self.prog)

  def config(self):
    xdg = self.env('config')
    if xdg is not None: return xdg
    if self.xdgstrict: return self.join('.config',self.prog)
    return self.join('etc',self.prog)

  def cache(self):
    xdg = self.env('config')
    if xdg is not None: return xdg
    if self.xdgstrict: return self.join('.cache',self.prog)
    return self.join('tmp',self.prog)
