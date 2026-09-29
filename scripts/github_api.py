import os
import json
import urllib.request
import urllib.error
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

USERNAME = os.getenv("GITHUB_USERNAME", "RishvinReddy")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get(url):
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return json.loads(response.read().decode())
    except urllib.error.URLError as e:
        print(f"[ERROR] API request failed for {url}: {e}")
        return None

def fetch_repositories():
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{USERNAME}/repos?type=owner&sort=updated&per_page=100&page={page}"
        print(f"[INFO] Fetching page {page}...")
        data = get(url)
        if data is None: return None
        if not data: break
        repos.extend(data)
        if len(data) < 100: break
        page += 1
    return repos

def fetch_repository(repo_name):
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}"
    return get(url)

def fetch_languages(repo_name):
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/languages"
    return get(url)
