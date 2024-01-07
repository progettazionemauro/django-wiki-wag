import markdown2

input_file = 'wiki_page.md'  # replace with the path to your markdown file
output_file = 'wiki_page.html'  # replace with the path to your desired output html file

# Read the markdown content
with open(input_file, 'r') as file:
    markdown_content = file.read()

# Convert markdown to HTML
html_content = markdown2.markdown(markdown_content)

# Save the converted HTML content to a file
with open(output_file, 'w') as file:
    file.write(html_content)

print(f'Successfully converted {input_file} to {output_file}')
