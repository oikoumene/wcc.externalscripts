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

class IEbscoSearch(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    pass

class Assignment(base.Assignment):
    implements(IEbscoSearch)

    @property
    def title(self):
        return _('Ebsco Search')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/ebscosearch.pt')

    @property
    def available(self):
        return True

class AddForm(base.NullAddForm):
    form_fields = form.Fields(IEbscoSearch)
    label = _(u"Add Ebsco Search")
    description = _(u"Ebsco search box")

    def create(self):
        return Assignment()
