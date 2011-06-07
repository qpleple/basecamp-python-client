Basecamp Python Client
======================
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

# Prepare the interaction with Basecamp.
bc = Basecamp('http://yourBasecamp.projectpath.com/', username, password)

# Fetch the to-do lists of a project.
todolists = bc.todo_lists(yourProjectID)

# Let's use the ElementTree API to access data via path expressions:
for name in ET.fromstring(todolists).findall('todo-list/name'):
    print name.text

# See the ElementTree website for more information on how to use it.
</pre>

Original Code
-------------
This code is built from the code of Jochen Kupperschmidt <webmaster@nwsnet.de> (see http://homework.nwsnet.de/products/3cd4) under the MIT Licence.

Added also some suggestions from Greg Allard (see http://codespatter.com/2009/04/01/getting-basecamp-api-working-with-python).