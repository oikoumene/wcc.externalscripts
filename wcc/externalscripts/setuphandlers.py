from collective.grok import gs
from wcc.externalscripts import MessageFactory as _

@gs.importstep(
    name=u'wcc.externalscripts', 
    title=_('wcc.externalscripts import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.externalscripts.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
