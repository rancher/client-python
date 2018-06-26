# client-python

A Python client for the Rancher API

## Installing
```
pip install git+https://github.com/rancher/client-python.git@HEAD
```

## Running as command line client
NOTE: The fact that this can be ran as a CLI at all is primarily due to legacy. The real Rancher CLI can be found [here](https://github.com/rancher/cli).


```bash
export RANCHER_URL=https://localhost:8443/v3
export RANCHER_ACCESS_KEY=<some valid access key>
export RANCHER_SECRET_KEY=<some valid secret key>
export RANCHER_VERIFY=False # If you're using a self-signed or otherwise invalid cert

rancher --help

# curl -s https://localhost:8443/v3/widgets?me=true
./rancher.py list-user list-user --me=true

# curl -s -X POST https://localhost:8443/v3/users -H 'Content-Type: application/json' -d '{ "username" : "user1", "password": "Password1" }'
./rancher.py create-user --username=user1 --password=Password1

# curl -s -X PUT https://localhost:8443/v3/users/user-xyz123 -H 'Content-Type: application/json' -d '{ "description" : "A user" }'
rancher update-user --id=user-xyz123 --description='A user'

# curl -s -X DELETE https://localhost:8443/v3/users/user-xyz123
rancher delete-user --id=user-xyz123
```

### Environment variables

|Name               | Description    | Example                                 |
|-------------------|----------------|-----------------------------------------|
|RANCHER_URL        | URL of the API | https://localhost:8443/v3                |
|RANCHER_ACCESS_KEY | Access Key     | 4C27AB31828A4E469C09                    |
|RANCHER_SECRET_KEY | Secrey Key     | fDxEzyxdFMWbmugstPpzykj2qA84Tn9DPDiAc3Sb|
|RANCHER_VERIFY     | Verify cert    | False                                   |

The above environment variables can be passed as arguments on the command line such as `--url`, `--access-key`, and `--secret-key`.

### Bash Autocompletion

Add the below to your `.bashrc` or similar profile script:
```
eval "$(register-python-argcomplete rancher)"
```

## Using API

```python

import rancher

client = rancher.Client(url='https://localhost:8443/v3',
                        access_key='<some valid access key>',
                        secret_key='<some valid secret key>')

# curl -s https://localhost:8443/v3/users?me=true
client.list_user(me='true')

# curl -s -X POST https://localhost:8443/v3/users -H 'Content-Type: application/json' -d '{ "username" : "user1", "password": "Password1" }'
client.create_user(username='user1', password='Password1')

# curl -s -X PUT https://localhost:8443/v3/users/user-xyz123 -H 'Content-Type: application/json' -d '{ "description" : "A user" }'
user = client.by_id_user('user-xyz123')
client.update(user, description='A user')

# curl -s -X DELETE https://localhost:8443/v3/users/user-xyz123
user = client.by_id_widget('user-xyz123')
client.delete(user)

# Links
# curl -s https://localhost:8443/v3/clusterRoleTemplateBindings?userId=user-xyz123
user = client.by_id_user('user-xyz123')
widget.clusterRoleTemplateBindings()
```

# Contact
For bugs, questions, comments, corrections, suggestions, etc., open an issue in
 [rancher/rancher](//github.com/rancher/rancher/issues) with a title starting with `[rancher-python] `.

Or just [click here](//github.com/rancher/rancher/issues/new?title=%5Brancher-python%5D%20) to create a new issue.
