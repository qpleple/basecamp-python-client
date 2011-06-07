# Import ElementTree and the Basecamp wrapper module.
import elementtree.ElementTree as ET
from basecamp import Basecamp

bc = Basecamp('https://example.basecamphq.com', 'API_KEY', 'X')
# or 
# bc = Basecamp('https://example.basecamphq.com', 'user', 'password')

# Fetch one todo list from its ID
xml = bc.todo_list(14499317)
items = ET.fromstring(xml).findall('todo-items/todo-item')

# Let's use the ElementTree API to access data via path expressions:
for item in items:
    print item.find("content").text