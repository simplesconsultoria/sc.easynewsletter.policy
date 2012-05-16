# -*- coding: utf-8 -*-
import urllib
import urlparse
from Products.EasyNewsletter.content import EasyNewsletter
from Products.EasyNewsletter.content import ENLIssue
from Products.EasyNewsletter.utils.ENLHTMLParser import ENLHTMLParser


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


def patch_image_parser():
    def handle_startendtag(self, tag, attrs):
        """
        """
        self.html += "<%s" % tag
        for attr in attrs:
            if attr[0] == "src":
                image_url = urlparse.urlparse(attr[1]).path
                if 'http' in attr[1]:
                    url = attr[1]
                    self.html += ' src="%s"' % url
                else:
                    o = self.context.restrictedTraverse(
                                    urllib.unquote(image_url))
                    url = o.absolute_url()
                    self.html += ' src="%s"' % url
            else:
                self.html += ' %s="%s"' % (attr)

        self.html += " />"
    setattr(ENLHTMLParser, 'handle_startendtag', handle_startendtag)


def run():
    patch_newsletter()
    patch_issue()
    patch_image_parser()
