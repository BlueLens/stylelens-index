from __future__ import print_function
from stylelens_index.index_objects import IndexObjects
from pprint import pprint
api_instance = IndexObjects()

object = {}
object['user_id'] = '111'

try:
  api_response = api_instance.add_user_object(object)
  pprint(api_response)
except Exception as e:
  print("Exception when calling add_user_object: %s\n" % e)
