import os
import yaml

site_sources_dir = "site-sources" # Name of the directory in which site source files are placed.
export_sites_to = "sites" # Name of the directory to place the exported sites.

# To add tabs to a multi-line string
def add_tabs(content, number_of_tabs_to_add):
    tabs = '\t' * number_of_tabs_to_add
    return '\n'.join([tabs + line for line in content.splitlines()])

# Create export_sites_to folder if it doesn't exist.
os.makedirs(export_sites_to, exist_ok=True)

# Clear export_sites_to folder.
print(f"Clearing {export_sites_to} folder")
for filename in os.listdir(export_sites_to):
    file_path = os.path.join(export_sites_to, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)

print("Scanning 'sites' dir")
for dir_name in os.listdir(site_sources_dir): # Loop through all sites folders.
    dir_path = os.path.join(site_sources_dir, dir_name)

    print(f"Acquiring metadata for {dir_name}") # Acquiring metadata.
    with open(os.path.join(dir_path, "metadata.yaml"), "r") as rawdata:
        data = yaml.safe_load(rawdata)

    print(f"Creating html file for {dir_name}") # Creating html file
    
    with open(os.path.join(export_sites_to, data["filename"] + ".html"), "w") as htmlfile:
        htmlfile.write(
            f"""
<!DOCTYPE html>
<html lang="en">
<head>
\t<meta charset="UTF-8">
\t<meta name="viewport" content="width=device-width, initial-scale=1.0">
\t<link rel="stylesheet" href="../default-assets/styles.css">
\t<link href="https://fonts.googleapis.com/css2?family=Baloo+Paaji&display=swap" rel="stylesheet">
\t<link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
\t<title>{data["title"]}</title>
</head>
<body>
    <header class="sticky-header">
        <h1 class="site-logo">FaseehOfficial</h1>
        <a href="https://faseeh-official.github.io" _target=blank>
            <button class="homepage-btn">Homepage</button>
        </a>
    </header>
\t<div class="container">
"""
        )

        print("Pasting content") # Pasting content from content.html.
        with open(os.path.join(dir_path, "content.html"), "r") as content_file:
            content = add_tabs(content_file.read(), 2)
            htmlfile.write(content)
            htmlfile.write("\n")

        print("Creating downloads section")
        htmlfile.write(f"\t\t<div class='downloads-section'>\n") # Downloads section.
        for link in data["download_links"]: # Create download button for each link.
            htmlfile.write(f"""
\t\t\t<div class="item-div">
\t\t\t\t<p>{link[0]}</p>
\t\t\t\t<a href="{link[1]}" download><button class="download-btn">Download</button></a>
\t\t\t</div>
""")

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
</body>
</html>
"""
        )
