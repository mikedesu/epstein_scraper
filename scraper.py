import requests
import json
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 scraper.py <search_string> <page_number>")
        sys.exit(-1)
    base_url = "https://www.justice.gov/multimedia-search?keys="
    search_term = sys.argv[1]
    page_var = int(sys.argv[2])
    url = f"{base_url}{search_term}&page={page_var}"
    cookie = ""
    with open("cookie.txt", "r") as f:
        cookie = f.read()
    headers = {
        "Cookie": "",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    }
    a = requests.get(url, headers=headers)
    my_dict = json.loads(a.text)
    hits_0 = my_dict["hits"]
    hits_1 = hits_0["hits"]
    uri_set = set()
    for hit in hits_1:
        source = hit["_source"]
        uri = source["ORIGIN_FILE_URI"]
        filename = source["ORIGIN_FILE_NAME"]
        uri = uri.replace(" ", "%20")
        uri_set.add((filename, uri))
        highlight = hit["highlight"]
        content = highlight["content"]
        print(uri)
        for line in content:
            print(line)
        print()
    for filename, uri in uri_set:
        print(uri)
        # print(filename)
        # try downloading...
        a = requests.get(uri, allow_redirects=True, headers=headers)
        with open(filename, "wb") as f:
            f.write(a.content)


if __name__ == "__main__":
    main()
