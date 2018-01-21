from __future__ import print_function
from stylelens_index.index_images import IndexImages
from pprint import pprint
api_instance = IndexImages()

try:
  res = api_instance.get_sim_images('5a5b4471632e51d6e2b9a797')
  pprint(res)
except Exception as e:
  print("Exception when calling get_sim_images: %s\n" % e)
