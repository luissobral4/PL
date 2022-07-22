import re

f = open('relatorio.xml')

content = f.read()
content = re.sub(r'<\?xml version=".+" encoding="(.+)"\?>',
    r'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="\1">\n</head>', content)

content = re.sub(r'<relatorio>', r'<body>', content)
content = re.sub(r'<titulo>', r'<h1>', content)
content = re.sub(r'data', r'h2', content)
#content = re.sub(r'autores', r'hr', content)
content = re.sub(r'<autores>', r'<hr>\n<h3>Autores:</h3>\n<ul>', content)
content = re.sub(r'</autores>', r'</ul>', content)
content = re.sub(r'<autor>\n', r'<li>', content)
content = re.sub(r'</autor>', r'</li>', content)
content = re.sub(r'<email>', r'', content)
content = re.sub(r'</email>\n', r'', content)
content = re.sub(r'<nome>', r'', content)
content = re.sub(r'</nome>\n', r' ', content)
content = re.sub(r'<numero>', r'', content)
content = re.sub(r'</numero>\n', r':', content)



content = re.sub(r'<resumo>', r'<h3>Resumo:</h3>\n<p>', content)
content = re.sub(r'</resumo>', r'</p>', content)

content = re.sub(r'<referencias>', r'<h3>Referencias:</h3>\n<ol>', content)
content = re.sub(r'referencia', r'li', content)
content = re.sub(r'</referencias>', r'</ol>', content)
content = re.sub(r'</relatorio>', r'</body>\n</html>', content)
print(content)

f.close()
