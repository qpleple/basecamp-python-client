Basecamp Python Client
======================
**Warning** : it seems like the URLs for the API are now deprecated. They should be updated according to the API reference (http://www.basecamphq.com/api/)

Description
-----------
This module provides an (almost) complete wrapper around the Basecamp API
(http://www.basecamphq.com/api/). It is written in Python and based upon the
excellent ElementTree package (http://effbot.org/zone/element-index.htm).
Requests will be made as XML, not YAML. Responses will be XML, too.

Make sure to allow access to the API (Dashboard > Account > Basecamp API) for
your projects.

Usage
-----
<pre>
# Import ElementTree and the Basecamp wrapper module.
import elementtree.ElementTree as ET
from basecamp import Basecamp

bc = Basecamp('https://example.basecamphq.com', 'API_KEY')
# or 
# bc = Basecamp('https://example.basecamphq.com', 'user', 'password')

# Fetch one todo list from its ID
xml = bc.todo_list(14499317)
items = ET.fromstring(xml).findall('todo-items/todo-item')

# Let's use the ElementTree API to access data via path expressions:
for item in items:
    print item.find("content").text
</pre>

Original Code
-------------
This code is built from the code of Jochen Kupperschmidt <webmaster@nwsnet.de> (see http://homework.nwsnet.de/products/3cd4) under the MIT Licence.

Added also some suggestions from Greg Allard (see http://codespatter.com/2009/04/01/getting-basecamp-api-working-with-python).