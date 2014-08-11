import xbmcgui, xbmc

def playMedia(title, thumbnail, link, mediaType='Video'):
    '''Plays a video
    Arguments:
    title: the title to be displayed
    thumbnail: the thumbnail to be used as an icon
    link: the link to the media to be played
    mediaType: the type of media to play: Video, Pictures, Music, or Programs
    '''
    li = xbmcgui.ListItem(label=title, iconImage=thumbnail, thumbnailImage=thumbnail, path=link)
    li.setInfo(type=mediaType, infoLabels={ "Title": title })
    xbmc.Player().play(item=link, listitem=li)