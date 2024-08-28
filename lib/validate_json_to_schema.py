import alive_progress
import glob
import json
import jsonschema
import os

schema_path = './schemas/document-schema.json'
json_paths  = glob.glob('./data/metadata_outputs/*.json')
schema      = json.load(open(schema_path))
validator   = jsonschema.Draft202012Validator(schema)

with alive_progress.alive_bar(len(json_paths), title='validating...', spinner='waves') as bar:
  for json_path in json_paths:
    with open(json_path, 'r') as fp:
      filename  = os.path.basename(json_path)
      test_json = json.load(fp)
      valid     = validator.is_valid(test_json)

      if not valid:
        print(f'{filename} failed!') 
        print(validator.validate(test_json))
      bar()  