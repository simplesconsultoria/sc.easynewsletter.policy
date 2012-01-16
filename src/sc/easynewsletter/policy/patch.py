# -*- coding: utf-8 -*-
from Products.EasyNewsletter.content import EasyNewsletter
from Products.EasyNewsletter.content import ENLIssue


HIDE = {'view': 'invisible', 'edit': 'invisible'}


def patch_newsletter():
    # Patch Newsletter
    schema = EasyNewsletter.schema
    schema['salutations'].default = ("sr|Sr.", "sra|Sra.", u"default|Olá")
    schema['fullname_fallback'].default = u"Olá"
    schema['unsubscribe_string'].default = u"Clique aqui para se descadastrar"
    schema['sendToAllPloneMembers'].widget.visible = HIDE
    schema['ploneReceiverMembers'].widget.visible = HIDE
    schema['ploneReceiverGroups'].widget.visible = HIDE
    schema['subscriberSource'].widget.visible = HIDE
    schema['deliveryService'].widget.visible = HIDE
    EasyNewsletter.schema = schema

def patch_issue():
    # Patch Newsletter
    schema = ENLIssue.schema
    schema['sendToAllPloneMembers'].widget.visible = HIDE
    schema['ploneReceiverMembers'].widget.visible = HIDE
    schema['ploneReceiverGroups'].widget.visible = HIDE
    schema['customViewFields'].widget.visible = HIDE
    schema['allowDiscussion'].widget.visible = HIDE
    schema['subject'].widget.visible = HIDE
    schema['location'].widget.visible = HIDE
    schema['effectiveDate'].widget.visible = HIDE
    schema['expirationDate'].widget.visible = HIDE
    schema['creators'].widget.visible = HIDE
    schema['contributors'].widget.visible = HIDE
    schema['rights'].widget.visible = HIDE
    schema['relatedItems'].schemata = "settings"
    schema['language'].schemata = "settings"
    schema['excludeFromNav'].schemata = "settings"
    ENLIssue.schema = schema

def run():
    patch_newsletter()
    patch_issue()


