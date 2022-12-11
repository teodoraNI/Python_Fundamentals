def htlm_format_content(content, html_atribute):
    return f"<{html_atribute}>\n    {content}\n</{html_atribute}>"

title = input()
content = input()
comments = []
result = ''
while True:
    comment = input()
    if comment == 'end of comments':
        break
    comments.append(comment)

print(htlm_format_content(title, 'h1'))
print(htlm_format_content(content, 'article'))
for comment in comments:
    print(htlm_format_content(comment, 'div'))

