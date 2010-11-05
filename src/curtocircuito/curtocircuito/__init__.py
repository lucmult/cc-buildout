# django imports
from django.utils.translation import ugettext_lazy as _

# lfc imports
from lfc.utils.registration import register_content_type
from lfc.utils.registration import unregister_content_type
from lfc.utils.registration import register_sub_type
from lfc.utils.registration import register_template
from lfc.utils.registration import unregister_template

# portlets imports
from portlets.utils import register_portlet
from portlets.utils import unregister_portlet

name = "curtocircuito"
description = _(u"Social network for sharing eletronic circuit")

def install():
    """Installs the curtocircuito application.
    """
    # register your stuff here
    
def uninstall():
    """Uninstalls the curtocircuito application.
    """
    # unregister your stuff here
