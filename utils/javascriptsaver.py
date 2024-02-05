import os,requests
# j is like javascript but i just named it j, ok? so dont get confused it has like names
# like j url is = javascript url and j content = javascript content, j filename = javascript filename etc etc.
def save_js(fp, jl, b_url, h):
    for jlink in jl:
        j_url = jlink if jlink.startswith('http') else b_url + jlink
        j_content = requests.get(j_url, headers=h).text
        j_filename = os.path.basename(j_url)
        with open(os.path.join(fp, j_filename), 'w', encoding='utf-8') as j_file:
            j_file.write(j_content)