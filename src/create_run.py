import os

import requests


def getEnv(key: str, default: str = None) -> str | None:
    value = os.environ.get(key)

    if value is None or value == "":
        return default

    return value


client_host = getEnv("GRAI_CLIENT_HOST")
api_key = getEnv("GRAI_API_KEY")
action = getEnv("GRAI_ACTION", "update")

connection_id = getEnv("GRAI_CONNECTION_ID")

connector_name = getEnv("GRAI_CONNECTOR_NAME")
connector_namespace = getEnv("GRAI_CONNECTOR_NAMESPACE")
connector_metadata = getEnv("GRAI_CONNECTOR_METADATA")
connector_secrets = getEnv("GRAI_CONNECTOR_SECRETS")
file_path = getEnv("GRAI_FILE_PATH")

github_owner = getEnv("GITHUB_OWNER")
github_repo = getEnv("GITHUB_REPO")
git_branch = getEnv("GIT_BRANCH")
git_head_sha = getEnv("GIT_HEAD_SHA")
git_commit_message = getEnv("GIT_COMMIT_MESSAGE")
github_pr_reference = getEnv("GITHUB_PR_REFERENCE")
github_pr_title = getEnv("GITHUB_PR_TITLE")

data = {"action": action}

if connection_id is not None:
    data["connection_id"] = connection_id
elif connector_name is not None:
    data["connector_name"] = connector_name
    data["connector_namespace"] = connector_namespace
    data["connector_metadata"] = connector_metadata
    data["connector_secrets"] = connector_secrets
if github_owner is not None:
    data["github_owner"] = github_owner
    data["github_repo"] = github_repo
    data["git_branch"] = git_branch
    data["git_head_sha"] = git_head_sha
    data["git_commit_message"] = git_commit_message
    data["github_pr_reference"] = github_pr_reference
    data["github_pr_title"] = github_pr_title

headers = {"Authorization": f"Api-Key {api_key}"}

res = None

if file_path:
    with open(file_path, "rb") as file:
        res = requests.post(
            f"{client_host.rstrip('/')}/api/v1/external-runs/",
            data=data,
            headers=headers,
            files={"file": file},
        )
else:
    res = requests.post(
        f"{client_host.rstrip('/')}/api/v1/external-runs/",
        data=data,
        headers=headers,
    )

res.raise_for_status()
print(res.json())
