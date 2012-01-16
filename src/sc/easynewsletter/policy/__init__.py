# -*- coding: utf-8 -*-
import patch
from five import grok

from Products.CMFPlone.interfaces import INonInstallable


class HiddenProfiles(grok.GlobalUtility):

    grok.implements(INonInstallable)
    grok.provides(INonInstallable)
    grok.name('sc.easynewsletter.policy')

    def getNonInstallableProfiles(self):
        profiles = ['sc.easynewsletter.policy:uninstall',
                    'Products.EasyNewsletter:default',
                    'Products.EasyNewsletter:uninstall']
        return profiles

patch.run()