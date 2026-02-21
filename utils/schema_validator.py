from jsonschema import validate

def validate_schema(response, schema):
    validate(instance=response, schema=schema)