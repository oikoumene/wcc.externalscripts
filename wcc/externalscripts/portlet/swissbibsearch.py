from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from wcc.externalscripts import MessageFactory as _

class ISwissbibSearch(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    pass

class Assignment(base.Assignment):
    implements(ISwissbibSearch)

    @property
    def title(self):
        return _('Swissbib Search')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/swissbibsearch.pt')

    @property
    def available(self):
        return True

class AddForm(base.NullAddForm):
    form_fields = form.Fields(ISwissbibSearch)
    label = _(u"Add Swissbib Search")
    description = _(u"Swissbib search box")

    def create(self):
        return Assignment()
