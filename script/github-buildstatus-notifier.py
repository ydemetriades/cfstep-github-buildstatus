#!/usr/bin/env python
import os
import requests

gh_url = os.getenv('GH_BSN_URL', 'https://api.github.com')
repo_owner = os.getenv('CF_REPO_OWNER')
repo_name = os.getenv('CF_REPO_NAME')
repo_auth_user = os.getenv('GH_BSN_REPO_AUTH_USER', repo_owner)
repo_token = os.getenv('GH_BSN_REPO_AUTH_TOKEN')

if repo_owner is None:
    print("Repository Owner Environment Variable [CF_REPO_OWNER] is not defined.")
    exit(2)

if repo_name is None:
    print("Repository Owner Environment Variable [CF_REPO_OWNER] is not defined.")
    exit(2)

if repo_token is None:
    print("Authentication User Token Environment Variable [GH_BSN_REPO_AUTH_TOKEN] is not defined.")
    exit(2)

cf_build_id = os.getenv('CF_BUILD_ID')
cf_status = os.getenv('CF_BUILD_STATUS', 'pending') # 'error', 'failure', 'pending', 'success'
cf_revision = os.getenv('CF_REVISION')
cf_build_url = os.getenv('CF_BUILD_URL')
description = os.getenv('GH_BSN_BUILD_DESCRIPTION', 'Build [{}]'.format(cf_build_id))
context = os.getenv('GH_BSN_BUILD_CONTEXT', 'codefresh-ci')

print('Will Attempt to update build status of commit [{}] to [{}] '.format(cf_revision, cf_status))

data = {
    'state': cf_status,
    'target_url': cf_build_url,
    'description': description,
    'context': context
}

# Construct URL
api_url = ('%(url)s/repos/%(owner)s/%(name)s/statuses/%(revision)s'
           % {'url': gh_url,
              'owner': repo_owner,
              'name': repo_name,
              'revision': cf_revision})

print('Sending request to:')
print(api_url)
print('with body')
print(data)

# Post build status to Github
response = requests.post(api_url, auth=(repo_auth_user, repo_token), json=data)

print('Response:')
print(response)
print(response.text)

if response:
    exit(0)
else:
    exit(1)