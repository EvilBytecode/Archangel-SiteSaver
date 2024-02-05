# Archangel-SiteSaver
This Python code allows you to save the content (HTML, JS, and CSS) of a website.


## Example:
- Before importing, download this repository lol.
- btw these variables can be modified so like website_url just to wburi etc.
1. ex. code.:
   - this saves your specified options you can either choose if you want only the sites css or js or html! it all depenfs out you

    ```python
    from utils.savesitecontent import save_content

    website_url = 'https://example.com'
    output_folder = 'foldername'
    user_agent = 'Your User Agent'

    save_html = True
    save_js= True
    save_css = True

    save_content(website_url, output_folder, user_agent, save_html, save_js, save_css)
    ```

2. ex. code:
 - this saves the entire site without images, merges all css content and js into one html file.
```python
from utils.special import copysite

gay = 'https://celex.gg/'
put = 'celex'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
copysite(gay, put, UA)
```
