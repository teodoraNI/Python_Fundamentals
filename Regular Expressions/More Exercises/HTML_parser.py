import re

html_content = input()
pattern1 = r'<title>(.*)</title>.*<body>(.*)</body>'
match = re.search(pattern1, html_content )
if match:
    title = match.group(1)
    content_not_refined = match.group(2)
    pattern2 = r'(<.[^<>]*>)|(\\n)'
    content = re.sub(pattern2, '', content_not_refined)
    print(f"Title: {title}\nContent: {content}")