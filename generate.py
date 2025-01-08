import os
import yaml

site_sources_dir = "site-sources" # Name of the directory in which site source files are placed.

# To add tabs to a multi-line string
def add_tabs(content, number_of_tabs_to_add):
    tabs = '\t' * number_of_tabs_to_add
    return '\n'.join([tabs + line for line in content.splitlines()])

# Create download and articles folders.
os.makedirs("download", exist_ok=True)
os.makedirs("article", exist_ok=True)

# Clear folders.
print(f"Clearing 'download' folder")
for filename in os.listdir("download"):
    file_path = os.path.join("download", filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
print(f"Clearing 'article' folder")
for filename in os.listdir("article"):
    file_path = os.path.join("article", filename)
    if os.path.isfile(file_path):
        os.remove(file_path)



print("Scanning 'site-sources' dir")
for dir_name in os.listdir(site_sources_dir): # Loop through all sites folders.
    dir_path = os.path.join(site_sources_dir, dir_name)

    print(f"Acquiring metadata for {dir_name}") # Acquiring metadata.
    with open(os.path.join(dir_path, "metadata.yaml"), "r") as rawdata:
        data = yaml.safe_load(rawdata)

    print(f"Creating html file for {dir_name}") # Creating html file
    
    # Determine the location to export.
    if data["type"] == "download":
        export_to = "download"
    elif data["type"] == "article":
        export_to = "article"
    else:
        print(f"Make sure 'type' attribute in metadata.yaml is properly configured.")
        break

    with open(os.path.join(export_to, data["filename"] + ".html"), "w") as htmlfile:
        htmlfile.write(
            f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../default-assets/styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Baloo+Paaji&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
    <title>{data["title"]}</title>\n"""
        )

        # Add MathJax if the type is "article".
        if data["type"] == "article":
            htmlfile.write("""
    <script type="text/javascript" async
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>\n"""
            )

        htmlfile.write("""
</head>
<body>
    <header class="sticky-header">
        <h1 class="site-logo">Faseeh-Z</h1>
        <a href="https://faseeh-z.github.io" _target=blank>
            <button class="homepage-btn">
                <img src="../default-assets/home.svg" alt="Homepage" class='home-icon' />
            </button>
        </a>
    </header>
    <div class="container">\n"""
        )

        print("Pasting content") # Pasting content from content.html.
        with open(os.path.join(dir_path, "content.html"), "r") as content_file:
            content = add_tabs(content_file.read(), 2)
            htmlfile.write(content)
            htmlfile.write("\n")

        print("Creating downloads/article section")
        htmlfile.write(f"\t\t<div class='downloads-section'>\n") # Downloads section.
        if data["type"] == "article": # Only if type is article.
            htmlfile.write(f"""\t\t\t<h2 style="text-align: center;">Related Articles</h2>\n""")

        for link in data["links"]: # Create button for each link.
            htmlfile.write(f"""
            <div class="item-div">
                <p>{link[0]}</p>\n"""
            )

            if data["type"] == "download": # Create download button
                htmlfile.write(f'\t\t\t\t<a href="{link[1]}" download><button class="download-btn">Download</button></a>\n')
            if data["type"] == "article":
                htmlfile.write(f'\t\t\t\t<a href="{link[1]}"><button class="download-btn">Read</button></a>\n')
            htmlfile.write("\t\t\t</div>")

        print("Closing file")
        htmlfile.write("""
        </div>
    </div>
    <div class="footer">
        <div class="link-container">
            <section class="link-grid">
                <div class="link-box">
                    <h4>Thanks!</h4>
                    <p>It is your support that keeps me motivated throughout each project's development journey. Every piece of feedback, suggestion, and encouragement helps me improve and strive to create better results. Thank you for being an invaluable part of this journey. I look forward to achieving even greater things together!</p>
                </div>
                <div class="link-box">
                    <h4>My Software</h4>
                    <ul>
                        <li><a href="https://faseeh-official.itch.io/apple-jump/">Apple Jump</a></li>
                        <li><a href="https://faseeh-official.github.io/file-encrypter-dist/">File Encrypter</a></li>
                        <li><a href="https://faseeh-official.github.io/dot-dash-dist/">Dot Dash</a></li>
                        <li><a href="https://faseeh-official.github.io/tkinter-tutorial/">Tkinter Tutorial</a></li>
                        <li><a href="https://github.com/faseeh-official/programming-solutions/">Programming Solutions</a></li>
                    </ul>
                </div>
                <div class="link-box">
                    <h4>Support</h4>
                    <ul>
                        <li><a href="https://youtube.com/@coderapids?si=Pd3PXfRjw141buM_">YouTube</a></li>
                        <li><a href="https://github.com/faseeh-official">GitHub</a></li>
                        <li><a href="#">Instagram</a></li>
                        <li><a href="https://faseeh-official.github.io/tkinter-tutorial/">Feedback</a></li>
                    </ul>
                </div>
            </section>
        </div>
    </div>
    <script src="../default-assets/script.js"></script>
</body>
</html>
"""
        )

print("\nProcess completed.")
input("Press any key to finish.")
