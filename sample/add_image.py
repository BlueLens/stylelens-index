from __future__ import print_function
from stylelens_index.index_images import IndexImages
from pprint import pprint
api_instance = IndexImages()

image = {}
image['product_id'] = '1234'
image['host_code'] = 'HCxxx'
image['product_no'] = '1'
image['version_id'] = 'test'

try:
  api_response = api_instance.add_image(image)
  pprint(api_response)
except Exception as e:
  print("Exception when calling add_image: %s\n" % e)
