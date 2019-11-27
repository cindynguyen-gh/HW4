import glob
# all_html_files = glob.glob("content/*.html")
# print(all_html_files)

import os
pages = []
# file_path = "content/blog.html"
# file_name = os.path.basename(file_path)
# print(file_name)
# name_only, extension = os.path.splitext(file_name)
# print(name_only)

from jinja2 import Template
# index_html = open("index.html").read()
# template_html = open("base.html").read()
# template = Template(template_html)
# template.render(
#     title="Homepage",
#     content=index_html,
# )


all_html_files = glob.glob("content/*.html")
# print("here are my html files")
print(all_html_files)
# print("done printing")

pages = []
for file in all_html_files:
    file_path = file
    print(file_path)

    file_name = os.path.basename(file_path)
    print(file_name)
    name_only, extension = os.path.splitext(file_name)
    print(name_only)
    print(extension)

    pages.append({
        "filename": file_name,
        "title": name_only,
        "output":'docs/' + file_name,
    }) 
print(pages)  

all_html_files = open(file).read()
template_html = open("templates/base.html").read()
template = Template(template_html)
template.render(
    title = pages
    content = file
)




# # def main():
# #     base = open("templates/base.html").read()
    

# pages = [
#     {   
#         "filename": "content/index.html",
#         "output": "docs/index.html",
#         "title": "Blog",
#     }, 
#     {   "filename": "content/projects.html",
#         "output": "docs/projects.html",
#         "title": "Projects",
#     }, 
#     { 
#         "filename": "content/contact.html",
#         "output": "docs/contact.html",
#         "title": "About Me",
#     }
# ]

# # if __name__ == "__main__":
# #     main()    

# # Read in the entire template
# template = open("./templates/base.html").read()

# for page in pages:
#     print("page:",page['title']) # Replace this line eventually with other stuff...
#     content_file = page['filename']

#     index_content = open(content_file).read()
#     finished_index_page = template.replace("{{content}}", index_content).replace("{{ title }}", page['title'])
#     output_file = page['output']
#     open(output_file, "w+").write(finished_index_page)

# # print('success!')

# # Where "page" is a dictionary with a key "title"
# # page_title = page['title']
# # print(page_title)



# # Read in the content of the index HTML page



# # Use the string replace

# # out_file = open("./templates/base.html").read()

# # index_content = open("content/index.html").read()
# # finished_index_page = template.replace("{{content}}", index_content)
# # open("docs/index.html", "w+").write(finished_index_page)

# # projects_content = open("content/projects.html").read()
# # finished_projects_page = template.replace("{{content}}", projects_content)
# # open("docs/projects.html", "w+").write(finished_projects_page)

# # contact_content = open("content/contact.html").read()
# # finished_contact_page = template.replace("{{content}}", contact_content)
# # open("docs/contact.html", "w+").write(finished_contact_page)

# # def apply_template(content):
# # TODO: Read in template, do string replacing, and return result return results

# # def main():
# #     content = open('docs/index.html').read()
# #     resulting_html_for_index = apply_template(content)

# # def main():
# #     content = open('docs/projects.html').read()
# #     resulting_html_for_projects = apply_template(content)

# # def main():
# #     content = open('docs/contact.html').read()
# #     resulting_html_for_contact = apply_template(content)

# # <html>
# #   <head>
# #     {% if user %}
# #     <title>Hey there {{ user }}</title>
# #     {% else %}
# #     <title>I don't know you!</title>
# #     {% endif %}
# #   </head>
# #   <body>
# #     <header>
# #         {% include "header.html" %}
# #     </header>
# #     <div class="content">
# #         {% include "content.html" %}
# #     </div>
# #     <footer>
# #         {% include "footer.html" %}
# #     </footer>
# #   </body>
# # </html>


# index_html = open("index.html").read()
# template_html = open("base.html").read()
# template = Template(template_html)
# template.render(
# title="Homepage",
# content=index_html,
# )

# {% for page in pages %}
# <a href="{{ page.output_filename }}">{{ page.title }}</a>
# {% endfor %}
