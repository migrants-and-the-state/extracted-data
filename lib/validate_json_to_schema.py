import alive_progress
import glob
import json
import jsonschema
import os

def validate_record(json_path, validator):
  with open(json_path, 'r') as fp:
    test_json = json.load(fp)
    valid = validator.is_valid(test_json)
    if not valid:
      print(f'{json_path} failed!') 
      print(validator.validate(test_json))
    return valid
  
def validate_records(json_paths, schema_path):
  schema = json.load(open(schema_path))
  with alive_progress.alive_bar(len(json_paths), title='validating...', spinner='waves') as bar:
    validator = jsonschema.Draft202012Validator(schema)
    for json_path in json_paths:
      validate_record(json_path, validator)
      bar() 

afile_schema_path = './schemas/afile-schema-kc-2023.json'
afile_json_paths  = glob.glob('./data/afiles/*.json')
page_schema_path = './schemas/page-schema-kc-2023.json'
page_json_paths  = glob.glob('./data/pages/*.json')

validate_records(afile_json_paths, afile_schema_path)
validate_records(page_json_paths, page_schema_path)

