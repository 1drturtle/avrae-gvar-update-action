import collections
import requests
import os
import json

ToPublish = collections.namedtuple('ToPublish', ['filename', 'abs_path', 'rel_path', 'gvar_id'])
GVAR_SUFFIXES = ('.gvar',)


def post_gvar(token: str, gvar: ToPublish):
    with open(gvar.abs_path, 'r') as f:
        code = f.read()
        data_post = {
            "value": code
        }
        # Make Requests
        auth = {'Authorization': token}
        request = f'https://api.avrae.io/customizations/gvars/{gvar.gvar_id}'
        print('POST Request Sent to ' + request)
        # POST New Alias Code
        post_result = requests.post(url=request,
                                    json=data_post,
                                    headers=auth
                                    )
        print(f'Result for ID {gvar.gvar_id}: {post_result.text}')


def main():
    gvar_id_file_name = os.environ.get('INPUT_GVAR-IDS-FILE')
    path_to_files = os.environ.get('GITHUB_WORKSPACE')
    avrae_token = os.getenv('INPUT_AVRAE-TOKEN', None)
    modified_files = json.loads(os.getenv('INPUT_MODIFIED-FILES', '[]'))

    if avrae_token is None:
        raise Exception('Invalid API token passed!')

    with open(path_to_files + '/' + gvar_id_file_name, 'r') as f:
        gvar_ids = json.loads(f.read())

    to_publish = []
    for root, dirs, files in os.walk(path_to_files):

        # Only get files that end in .gvar
        files = [str(filename) for filename in files if str(filename).endswith(GVAR_SUFFIXES)]

        # Make a list of modified files
        for name in files:
            abs_path = os.path.join(root, name)
            shared = os.path.commonprefix([abs_path, path_to_files])
            rel_path = os.path.relpath(abs_path, shared)
            if rel_path in modified_files and rel_path in gvar_ids:
                to_publish.append(ToPublish(name, abs_path=abs_path, rel_path=rel_path, gvar_id=gvar_ids[rel_path]))

    # Run API script
    for gvar in to_publish:
        post_gvar(avrae_token, gvar)


if __name__ == '__main__':
    main()
