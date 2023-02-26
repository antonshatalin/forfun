import markdown


with open('./sorry.md', encoding='utf-8') as file:
    markdown_text = file.read()

html = markdown.markdown(
    markdown_text
)

print(html)

