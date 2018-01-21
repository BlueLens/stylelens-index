from __future__ import print_function
from stylelens_index.index_objects import IndexObjects
from pprint import pprint
api_instance = IndexObjects()

try:
  res = api_instance.get_objects(version_id='5a50d4ba4dfd7d90b8b9369a',
                              sort_key='index',
                              sort_order=1,
                              offset=0,
                              limit=100)
  pprint(res)
except Exception as e:
  print("Exception when calling get_objects: %s\n" % e)
