import re
import github


def get_repo_file_info(owner, repo_name):
    g = github.Github()
    repo = g.get_repo(owner + "/" + repo_name)

    file_info = []
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            if file_content.type == "file":
                file_path = file_content.path
                updated_at = file_content.last_modified
                file_info.append((file_path, updated_at))

    return file_info


def get_owner_and_repo(url):
    """
    Extract the owner and repo name from a GitHub URL
    """
    pattern = r"github\.com/([\w-]+)/([\w-]+)"
    match = re.search(pattern, url)
    if match:
        owner = match.group(1)
        repo = match.group(2)
        return owner, repo
    else:
        return None, None


def ma():
    # Example usage
    owner, repo_name = get_owner_and_repo(
        "https://github.com/mitmproxy/mitmproxy/tree/main?tab=readme-ov-file"
    )
    print(f"owner  is : {owner}")
    print(f"repo_name is : {repo_name}")
    file_info = get_repo_file_info(owner, repo_name)
    for path, updated_at in file_info:
        print(f"{path}, {updated_at}")


ma()
