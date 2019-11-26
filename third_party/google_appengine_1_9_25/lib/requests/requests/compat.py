# -*- coding: utf-8 -*-

"""
pythoncompat
"""


from .packages import chardet

import sys
import six

# -------
# Pythons
# -------

# Syntax sugar.
_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)

try:
    import simplejson as json
except (ImportError, SyntaxError):
    # simplejson does not support Python 3.2, it throws a SyntaxError
    # because of u'...' Unicode literals.
    import json

# ---------
# Specifics
# ---------

if is_py2:
    from six.moves.urllib.parse import quote, unquote, quote_plus, unquote_plus, urlencode
    from six.moves.urllib.parse import urllib.parse, urlunparse, urljoin, urlsplit, urldefrag
    from urllib2 import parse_http_list
    import six.moves.http_cookiejar
    from six.moves.http_cookies import Morsel
    from io import StringIO
    from .packages.urllib3.packages.ordered_dict import OrderedDict

    builtin_str = str
    bytes = str
    str = six.text_type
    six.string_types = six.string_types
    numeric_types = (int, int, float)

elif is_py3:
    from urllib.parse import urllib.parse, urlunparse, urljoin, urlsplit, urlencode, quote, unquote, quote_plus, unquote_plus, urldefrag
    from urllib.request import parse_http_list, getproxies, proxy_bypass
    from http import cookiejar as cookielib
    from http.cookies import Morsel
    from io import StringIO
    from collections import OrderedDict

    builtin_str = str
    str = str
    bytes = bytes
    six.string_types = (str, bytes)
    numeric_types = (int, float)
