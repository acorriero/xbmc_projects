import sys, urllib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin

def playMedia(title, thumbnail, link, mediaType='Video'):
    """Plays a video
    
    Arguments:
    title: the title to be displayed
    thumbnail: the thumbnail to be used as an icon and thumbnail
    link: the link to the media to be played
    mediaType: the type of media to play, defaults to Video. Known values are Video, Pictures, Music and Programs
    """
    
    li = xbmcgui.ListItem(label=title, iconImage=thumbnail, thumbnailImage=thumbnail, path=link)
    li.setInfo(type=mediaType, infoLabels={ "Title": title })
    xbmc.Player().play(item=link, listitem=li)
    
def parseParameters(inputString): #=sys.argv[2]):
    """Parses a parameter string starting at the first ? found in inputString
    
    Argument:
    inputString: the string to be parsed, sys.argv[2] by default
    
    Returns a directory with parameters names as keys and parameter values as values
    """
    parameters = {}
    p1 = inputString.find('?')
    if p1 >= 0:
        splitParameters = inputString[p1 + 1].split('&')
        for nameValuePair in splitParameters:
            if len(nameValuePair) > 0:
                pair = nameValuePair.split('=')
                key = pair[0]
                value = urllib.unquote(urllib.unquote_plus(pair[1])).decode('utf-8')
                paramaters[key] = value
    return parameters