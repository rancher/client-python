# gdapi-python

A Python client for Rancher APIs

## Installing

    pip install gdapi-python

## Running as command line client

```bash
export GDAPI_URL=http://localhost:8080/v1

gdapi --help

# curl -s http://localhost:8080/v1/widgets?foo=bar
gdapi list-widget --foo=bar

# curl -s -X POST http://localhost:8080/v1/widgets -H 'Content-Type: application/json' -d '{ "foo" : "bar" }'
gdapi create-widget --foo=bar

# curl -s -X PUT http://localhost:8080/v1/widgets/42 -H 'Content-Type: application/json' -d '{ "foo" : "bar" }'
gdapi update-widget --id=42 --foo=bar

# curl -s -X DELETE http://localhost:8080/v1/widgets/42
gdapi delete-widget --id=42
```

### Environment variables

|Name             | Description    | Example                                 |
|-----------------|----------------|-----------------------------------------|
|GDAPI_URL        | URL of the API | http://localhost:8080/v1                |
|GDAPI_ACCESS_KEY | Access Key     | 4C27AB31828A4E469C09                    |
|GDAPI_SECRET_KEY | Secrey Key     | fDxEzyxdFMWbmugstPpzykj2qA84Tn9DPDiAc3Sb|

The above environment variables can be passed as arguments on the command line such as `--url`, `--access-key`, and `--secret-key`.

### Bash Autocompletion

Add the below to your `.bashrc` or similar profile script:
```
eval "$(register-python-argcomplete gdapi)"
```

## Using API

```python

import gdapi

client = gdapi.Client(url='http://localhost:8080/v1',
                      access_key='4C27AB31828A4E469C09',
                      secret_key='fDxEzyxdFMWbmugstPpzykj2qA84Tn9DPDiAc3Sb')

# curl -s http://localhost:8080/v1/widgets?foo=bar
client.list_widget(foo='bar')

# curl -s -X POST http://localhost:8080/v1/widgets -H 'Content-Type: application/json' -d '{ "foo" : "bar" }'
client.create_widget(foo='bar')

# curl -s -X PUT http://localhost:8080/v1/widgets/42 -H 'Content-Type: application/json' -d '{ "foo" : "bar" }'
widget = client.by_id_widget('42')
client.update(widget, foo='bar')

# curl -s -X DELETE http://localhost:8080/v1/widgets/42
widget = client.by_id_widget('42')
client.delete(widget)

# Links
# curl -s -X DELETE http://localhost:8080/v1/widgets/42/foobars
widget = client.by_id_widget('42')
widget.foobars()
```

# Contact
For bugs, questions, comments, corrections, suggestions, etc., open an issue in
 [rancher/rancher](//github.com/rancher/rancher/issues) with a title starting with `[gdapi-python] `.

Or just [click here](//github.com/rancher/rancher/issues/new?title=%5Bgdapi-python%5D%20) to create a new issue.
