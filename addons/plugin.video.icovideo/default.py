import xbmc
import xbmcaddon
 
__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')
__version__     = __addon__.getAddonInfo('version')
 
line1 = __addonname__ + "-" + __version__ + " just started"
time = 5000  #in miliseconds
 


# plugin constants
version = __version__
plugin = "IcoVideo-" + version
author = "Ico"
url = "Ico"

# xbmc hooks
settings = xbmcaddon.Addon(id='plugin.video.icovideo')
language = settings.getLocalizedString
dbg = settings.getSetting("debug") == "true"
dbglevel = 3

# Main imports
if (__name__ == "__main__" ):
    if dbg:
        print plugin + " ARGV: " + repr(sys.argv)
    else:
        print plugin
    
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))