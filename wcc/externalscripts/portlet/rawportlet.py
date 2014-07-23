from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form

# XXX: Uncomment for z3cform

from z3c.form import field

from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.relationfield.schema import RelationList, RelationChoice

from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from wcc.externalscripts import MessageFactory as _


class IRawPortlet(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    header = schema.TextLine(
        title=_(u"Portlet Header"),
        description=_(u""),
        required=True
    )

    raw_content = schema.Text(
        title=_(u'Content'),
        description=_(u''),
        required=True
    )


class Assignment(base.Assignment):
    implements(IRawPortlet)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def title(self):
        return self.header


class Renderer(base.Renderer):

    render = ViewPageTemplateFile('templates/rawportlet.pt')

    @property
    def available(self):
        return True

# XXX: z3cform
# class AddForm(z3cformhelper.AddForm):
class AddForm(base.AddForm):

#    XXX: z3cform
#    fields = field.Fields(IRawPortlet)

    form_fields = form.Fields(IRawPortlet)

    label = _(u"Add Raw Portlet")
    description = _(u"")

    def create(self, data):
        return Assignment(**data)

# XXX: z3cform
# class EditForm(z3cformhelper.EditForm):
class EditForm(base.EditForm):

#    XXX: z3cform
#    fields = field.Fields(IRawPortlet)

    form_fields = form.Fields(IRawPortlet)

    label = _(u"Edit Raw Portlet")
    description = _(u"")
