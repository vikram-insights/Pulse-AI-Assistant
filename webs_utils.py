import webbrowser
    
websites = {
        "youtube" : "https://www.youtube.com/",
        "google" : "https://www.google.com/",
        "leetcode" : "https://leetcode.com/",
        "github" : "https://github.com/",
        "instagram" : "https://www.instagram.com/",
        "vikram" : "https://www.instagram.com/viikram_11?igsh=MTd0djU2NHFnYWg1YQ==",
        "muskan" : "https://www.instagram.com/muskankashyap2672?igsh=MXdxYTY2YjBoNzQxcQ=="

    }

def open_website(name_or_url):
    
    clean_input = name_or_url.strip()

    
    if clean_input.lower() in websites:
        url = websites[clean_input.lower()]
    else:
        url = clean_input

    
    if not url.lower().startswith(("http://", "https://")):
        url = f"https://{url}"

    print(f"\nOpening: {url}")
    webbrowser.open_new_tab(url)








