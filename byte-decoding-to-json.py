import json
import requests
from zipfile import ZipFile
from io import BytesIO

def get_ocr_result():
  '''
  Gets ocr result, which is byte encoded, then decodes it
  and saves it in a json format
  '''
  # Requesting API calls that return byte encoded results
  ocr_response = requests.get('url_ocr_api_call')
  
  # Decoding bytes
  with ZipFile(BytesIO(ocr_response.content), 'r') as my_zip:
    zipped_json = my_zip.filelist[0]
    with my_zip.open(zipped_json, 'r') as json_file:
        pages = json.loads(json_file.read())

    # Saving result in JSON format
    filename = 'filename.json'
    with open(outputPath + "\\" + filename, 'w') as f:
            json.dump(pages, f)

def parse_json(doc_id):
    '''
    Converting json to text
    '''
    filename = 'filename.json'
    with open(filename) as f:
        data = json.load(f)
        return data[0]['ExtractedText'].lower()
