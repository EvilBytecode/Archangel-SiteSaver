import os,requests
from bs4 import BeautifulSoup

def copysite(url, folder_path, user_agent):
    h = {'User-Agent': user_agent}
#the only clean def in the func is folder_path lol and useraent noobies
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    r = requests.get(url, headers=h)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        
        uwuhtmlcontent = soup.prettify()
        
        cl = [link['href'] for link in soup.find_all('link', rel='stylesheet')]
        cc = ''
        for clink in cl:
            c_url = clink if clink.startswith('http') else url + clink
            cececontent = requests.get(c_url, headers=h).text
            cc += f'<style>\n{cececontent}\n</style>\n'
        
        jl = [script['src'] for script in soup.find_all('script', src=True)]
        jc = ''
        for jlink in jl:
            j_url = jlink if jlink.startswith('http') else url + jlink
            gugugagajcontent = requests.get(j_url, headers=h).text
            jc += f'<script>\n{gugugagajcontent}\n</script>\n'

        uwufinal = f"{uwuhtmlcontent}\n{cc}\n{jc}"

        with open(os.path.join(folder_path, 'site.html'), 'w', encoding='utf-8') as html_file:
            html_file.write(uwufinal)

        print(f"Site content saved successfully in {folder_path}/MergedSite.html")
    else:
        print(f"Failed to retrieve content from {url}. Status code: {r.status_code}")
        # learn about status codes, and about the website if it returns somthing than 200 its bad like 404/403/500 etc.
        # if the site provides why it returns the specific err stat code search for it if it has reason.
