import collections

CredentialPlugin = collections.namedtuple('CredentialPlugin', ['name', 'inputs', 'backend'])

def passwordstate_lookup(**kwargs):

    url = kwargs.get('url')
    token = kwargs.get('token')
    identifier = kwargs.get('identifier')

    raise ValueError(f'Could not find a value for {identifier}.')

passwordstate_plugin = CredentialPlugin(
    'PasswordState AWX Credential Plugin',

    inputs={
        'fields': [{
            'id': 'url',
            'label': 'PasswordState Server URL',
            'type': 'string',
        }, {
            'id': 'token',
            'label': 'PasswordState Api Key',
            'type': 'string',
            'secret': True,
        }],
        'metadata': [{
            'id': 'password_list_id',
            'label': _('Passwordlist ID'),
            'type': 'integer',
            'help_text': _('The Passwordlist id for the query'),
        }, {
            'id': 'hostname',
            'label': _('Hostname associated to record'),
            'type': 'string',
            'default': 'string',
            'help_text': _('Hostname to which the password belongs to. This is used as a match criteria when looking up passwords.')
        }, {
            'id': 'title',
            'label': _('Title associated to record'),
            'type': 'string',
            'help_text': _('Title of the password entry. This is used as a match criteria when looking up passwords.')
        }],
        'required': ['url', 'token'],
        
    },

    backend = passwordstate_lookup
)
