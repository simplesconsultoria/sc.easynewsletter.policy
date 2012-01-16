# -*- coding: utf-8 -*-
import logging

from zope import component

from Products.CMFCore.utils import getToolByName
from Products.GenericSetup import interfaces as gsinterfaces
from Products.GenericSetup.upgrade import listUpgradeSteps

PROJECT = 'sc.easynewsletter.policy'


def fromZero(context):
    ''' Upgrade from Zero to version 1000
    '''
    qi = getToolByName(context,'portal_quickinstaller')

    qi.installProduct('EasyNewsletter',
                       locked=False,
                       hidden=True,
                       profile='Products.EasyNewsletter:default')
