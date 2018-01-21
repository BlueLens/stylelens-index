from __future__ import print_function
from stylelens_index.index_images import IndexImages
from pprint import pprint
api_instance = IndexImages()

try:
  res = api_instance.get_image('5a5aedd4632e51d6e2afa3a2')
  pprint(res)
except Exception as e:
  print("Exception when calling get_image: %s\n" % e)
