# def main():
#     base = open("templates/base.html").read()
    

pages = [
    {   
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Blog",
    }, 
    {   "filename": "content/projects.html",
        "output": "docs/projects.html",
        "title": "Projects",
    }, 
    { 
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "About Me",
    }
]

# if __name__ == "__main__":
#     main()    

# Read in the entire template
template = open("./templates/base.html").read()

for page in pages:
    print("page:",page['title']) # Replace this line eventually with other stuff...
    content_file = page['filename']

    index_content = open(content_file).read()
    finished_index_page = template.replace("{{content}}", index_content)
    open(output_file, "w+").write(finished_index_page)

# Where "page" is a dictionary with a key "title"
page_title = page['title']
# print(page_title)



# Read in the content of the index HTML page



# Use the string replace
index_content = open("content/index.html").read()
finished_index_page = template.replace("{{content}}", index_content)
open("docs/index.html", "w+").write(finished_index_page)

projects_content = open("content/projects.html").read()
finished_projects_page = template.replace("{{content}}", projects_content)
open("docs/projects.html", "w+").write(finished_projects_page)

contact_content = open("content/contact.html").read()
finished_contact_page = template.replace("{{content}}", contact_content)
open("docs/contact.html", "w+").write(finished_contact_page)

# def apply_template(content):
# TODO: Read in template, do string replacing, and return result return results

# def main():
#     content = open('docs/index.html').read()
#     resulting_html_for_index = apply_template(content)

# def main():
#     content = open('docs/projects.html').read()
#     resulting_html_for_projects = apply_template(content)

# def main():
#     content = open('docs/contact.html').read()
#     resulting_html_for_contact = apply_template(content)