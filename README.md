# Archangel-SiteSaver
This Python code allows you to save the content (HTML, JS, and CSS) of a website.


## Example:
- Before importing, download this repository lol.
- btw these variables can be modified so like website_url just to wburi etc.
1. ex. code.:

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

## Options

- `website_url`: The URL of the website you want to save.
- `output_folder`: The folder where the website content will be saved.
- `user_agent`:    This is requiered most of the time cuz sites wont let you even in without it lol.
- `save_html_option`: Set to `True` if you want to save the HTML content.
- `save_js_option`: Set to `True` if you want to save the JS files.
- `save_css_option`: Set to `True` if you want to save the CSS files.
