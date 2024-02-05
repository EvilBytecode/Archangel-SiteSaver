import os,requests
from bs4 import BeautifulSoup
from utils.javascriptsaver import save_js
from utils.cssscriptsaver import save_css
from utils.htmlsaver import save_html
# trying the def in func make readbale atleast like save html js or css option. also opt is = option
def scrape(url, folder_path, user_agent, save_html_opt=True, save_js_opt=True, save_css_opt=True):
    h = {'User-Agent': user_agent}

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    r = requests.get(url, headers=h)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        html_content = soup.prettify()
        
        if save_html_opt:
            save_html(folder_path, html_content)
        
        cl = [link['href'] for link in soup.find_all('link', rel='stylesheet')]
        jl = [script['src'] for script in soup.find_all('script', src=True)]
        
        if save_css_opt:
            save_css(folder_path, cl, url, h)
        
        if save_js_opt:
            save_js(folder_path, jl, url, h)
        
        print(f"Content saved successfully in {folder_path}")
    else:
        print(f"Failed to retrieve content from {url}. Status code: {r.status_code}")
        # learn about status codes, and about the website if it returns somthing than 200 its bad like 404/403/500 etc.
        # if the site provides why it returns the specific err stat code search for it if it has reason.
