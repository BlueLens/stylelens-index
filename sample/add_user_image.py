from __future__ import print_function
from stylelens_index.index_images import IndexImages
from pprint import pprint
api_instance = IndexImages()

image = {}
image['user_id'] = '111'

try:
  api_response = api_instance.add_user_image(image)
  pprint(api_response)
except Exception as e:
  print("Exception when calling add_user_image: %s\n" % e)
