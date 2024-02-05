import os
# fp = folderpath,  hc = html content. 
def save_html(fp, hc):
    with open(os.path.join(fp, 'index.html'), 'w', encoding='utf-8') as hf:
        hf.write(hc)