import requests
from bs4 import BeautifulSoup

def scrape_website(website_url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        )
    }

    print(f"Fetching website: {website_url}")
    response = requests.get(website_url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch the website: {response.status_code}")

    return response.text


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]


# Example usage:
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Car"
    html = scrape_website(url)
    body_html = extract_body_content(html)
    cleaned_text = clean_body_content(body_html)
    chunks = split_dom_content(cleaned_text)

    print("\n--- First Chunk of Cleaned Content ---\n")
    print(chunks[0] if chunks else "No content found.")
