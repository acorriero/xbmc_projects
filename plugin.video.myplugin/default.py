import xbmcaddon
import util

addon = xbmcaddon.Addon('plugin.video.myplugin')

util.playMedia(addon.getAddonInfo('name'), addon.getAddonInfo('icon'),
               'rtmp://stream2.france24.yacast.net:80/france24_live/fr playpath=f24_livefr app=france24_live/fr')
