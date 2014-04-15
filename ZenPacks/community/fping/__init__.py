
import os
import Globals
from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
from Products.ZenUtils.Utils import zenPath
from Products.CMFCore.DirectoryView import registerDirectory

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

class ZenPack(ZenPackBase):
    """
    ZenPack class to add new zProperties and perform other installation and
    removal tasks.
    """
    def install(self, app):
        super(ZenPack, self).install(app)
        self.symlinkPlugin()
    def remove(self, app, leaveObjects=False):
        if not leaveObjects:
            self.removePluginSymlink()
        super(ZenPack, self).remove(app, leaveObjects=leaveObjects)
    def symlinkPlugin(self):
        os.system('ln -sf %s/check_fping %s/' %
            (self.path('libexec'), zenPath('libexec')))
    def removePluginSymlink(self):
        os.system('rm -f %s/check_fping' % (zenPath('libexec')))
