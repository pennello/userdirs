# chris 072315

import os

def home(): return os.path.expanduser('~')
def join(base,*a): return os.path.join(base,*a)

class XdgSpecial(object):
  localpath = '.local'
  @classmethod
  def defaultroot(cls): return join(home(),cls.localpath)
  def __init__(self,name,path): self.name,self.path = name,path
  def default(self): return join(home(),*self.path)

class UserDirs(object):
  # normal path -> xdg special
  _special = {
    ('share',):     XdgSpecial('data', ('.local','share')),
    ('etc',):       XdgSpecial('config',('.config',)),
    ('var','cache'):XdgSpecial('cache', ('.cache',)),
  }

  def __init__(self,xdgstrict=False): self.xdgstrict = xdgstrict

  def _env(self,key): return os.environ.get('XDG_%s_HOME' % key.upper())

  def _root(self):
    r = self._env('share')
    if r is None:
      if self.xdgstrict: return XdgSpecial.defaultroot()
      return home()
    r = os.path.normpath(r) # Might have a trailing slash.
    r = os.path.dirname(r)
    return r

  def dir(self,*a):
    s = self._special.get(a)
    if s is not None:
      e = self._env(s.name)
      if e is not None: return e
      if self.xdgstrict: return s.default()
    return join(self._root(),*a)

  def data(self): return self.dir('share')
  def config(self): return self.dir('etc')
  def cache(self): return self.dir('var','cache')
