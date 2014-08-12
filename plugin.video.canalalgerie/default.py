import util, urllib2

def playVideo(pageUrl):
    pass

def buildMenu():
    url = WEB_PAGE_BASE + 'index.php'
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        print content
    else:
        util.showError(ADDON_ID, 'Could not open URL %s to create menu' % (url))
        
WEB_PAGE_BASE = 'http://www.entv.dz/tvfr/video/'
ADDON_ID = 'plugin.video.canalalgerie'

parameters = util.parseParameters('0 1 ? &')

if 'play' in parameters:
    playVideo(parameters['play'])
else:
    buildMenu()