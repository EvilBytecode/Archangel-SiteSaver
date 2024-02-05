import os,requests
# if you dont understand variables please read javascriptsaver.py,  and if youre lazy:
# c_url = css url, fp = filepath etc c defines css so thats it..

def save_css(fp, cl, b_url, h):
    for clink in cl:
        c_url = clink if clink.startswith('http') else b_url + clink
        c_content = requests.get(c_url, headers=h).text
        c_filename = os.path.basename(c_url)
        with open(os.path.join(fp, c_filename), 'w', encoding='utf-8') as cf:
            cf.write(c_content)