print(">>> SCRIPT STARTED")

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

CSRF_FIELD_NAMES = {
    "csrf", "_csrf", "csrfmiddlewaretoken", "authenticity_token",
    "xsrf", "_xsrf", "__requestverificationtoken", "_token", "csrf_token"
}

def is_same_domain(start_url, new_url):
    start_netloc = urlparse(start_url).netloc
    new_netloc = urlparse(new_url).netloc
    return start_netloc == new_netloc or new_netloc == ""

def extract_forms(html, url):
    soup = BeautifulSoup(html, "html.parser")
    forms = []

    for form in soup.find_all("form"):
        method = (form.get("method") or "get").lower()
        action = form.get("action") or ""
        full_action = urljoin(url, action)

        inputs = form.find_all("input")
        has_csrf = False

        for inp in inputs:
            name = (inp.get("name") or "").lower()
            t = (inp.get("type") or "text").lower()

            if t == "hidden" and name in CSRF_FIELD_NAMES:
                has_csrf = True

        forms.append({
            "method": method,
            "action": full_action,
            "has_csrf": has_csrf
        })

    return forms

def crawl(start_url, max_pages=20, max_depth=2):
    visited = set()
    queue = deque([(start_url, 0)])
    vulnerable_forms = []

    headers = {
        "User-Agent": "CSRF-Scanner/1.0 (educational)"
    }

    while queue and len(visited) < max_pages:
        url, depth = queue.popleft()
        if url in visited or depth > max_depth:
            continue

        visited.add(url)
        print(f"[+] Crawling: {url}")

        try:
            resp = requests.get(url, headers=headers, timeout=10)
        except Exception as e:
            print(f"[!] Error fetching {url}: {e}")
            continue

        if "text/html" not in resp.headers.get("Content-Type", ""):
            continue

        forms = extract_forms(resp.text, url)

        for f in forms:
            if f["method"] in ("post", "put", "delete", "patch") and not f["has_csrf"]:
                vulnerable_forms.append({
                    "page": url,
                    "action": f["action"],
                    "method": f["method"]
                })

        soup = BeautifulSoup(resp.text, "html.parser")
        for link in soup.find_all("a", href=True):
            href = link["href"]
            full_url = urljoin(url, href)
            if is_same_domain(start_url, full_url) and full_url not in visited:
                queue.append((full_url, depth + 1))

    print("\n===== SCAN RESULTS =====")

    if not vulnerable_forms:
        print("No vulnerable forms found.")
    else:
        for v in vulnerable_forms:
            print("\n[!] Possible CSRF Vulnerability:")
            print(f" Page   : {v['page']}")
            print(f" Action : {v['action']}")
            print(f" Method : {v['method']}")

if __name__ == "__main__":
    target = "https://safwancs7.github.io/CSRF_Demo/"
    print(">>> Target:", target)

    crawl(target)
