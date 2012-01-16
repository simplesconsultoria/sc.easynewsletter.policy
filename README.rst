sc.easynewsletter.policy
**************************************************************

.. contents:: Table of Contents
   :depth: 2

Overview
--------

    Basic policy for Products.EasyNewsletter

Requirements
------------

    * Products.EasyNewsletter > 2.6.1

Installation
------------

To enable this product in a buildout-based installation:

    1. Edit your buildout.cfg and add ``sc.easynewsletter.policy``
       to the list of eggs to install ::

        [buildout]
        ...
        eggs =
            sc.easynewsletter.policy


After updating the configuration you need to run ''bin/buildout'',
which will take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the
'Add-ons' link.

Check the box next to ''EasyNewsletter'' and click the 'Activate' button.

Note: You may have to empty your browser cache and save your resource
registries in order to see the effects of the product installation.

Sponsoring
----------

Development of this product was sponsored by :
    
    * `Simples Consultoria <http://www.simplesconsultoria.com.br/>`_.


Credits
-------

    * Simples Consultoria (products at simplesconsultoria dot com dot br) - 
      Implementation
    
