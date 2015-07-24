# chris 072315

import os

class UserDirs(object):
  def __init__(self,xdgmode):
    '''
    xdgmode can be 'strict', 'compat', or None.
    '''
    self.xdgmode = xdgmode

  def env(self,key): return os.environ.get('XDG_%s_HOME' % key.upper())

  def home(self): return os.path.expanduser('~')

  def join(self,*a): return os.path.join(self.home(),*a)

  def dir(self,env,strict,compat,default):
    xdg = self.env(env)
    if xdg is not None: return xdg
    if self.xdgmode == 'strict': return self.join(*strict)
    if self.xdgmode == 'compat': return self.join(*compat)
    return self.join(*default)

  def data(self):
    return self.dir('data',('.local','share'),('.local','var'),('var',))

  def config(self):
    return self.dir('config',('.config',),('.local','etc'),('etc',))

  def cache(self):
    return self.dir('cache',('.cache',),('.local','tmp'),('tmp',))
