# read_text_to_html_grouped.py

from collections import defaultdict
import os
# Function to generate an HTML file from the text file with multiple images per label
def generate_html(input_file, output_file):
    # HTML structure (bootstrap for simple styling)
    html_start = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Synchro - PLanktivore Library</title>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </head>
    <body>
    <div class="container mt-5">
        <h1>Synchro Planktivore Library</h1>
    """

    html_end = """
    </div>
    </body>
    </html>
    """

    # Read the input text file and group images by label
    images_by_label = defaultdict(list)
    with open(input_file, 'r') as infile:
        for line in infile:
            filename, label = line.strip().split(',', 1)
            images_by_label[label].append(filename)

    # Create HTML content
    rows = ""
    for label, filenames in images_by_label.items():
        rows += f"<h2>{label}</h2>\n"
        rows += "<div class='row'>\n"
        for filename in filenames:
            fname = os.path.join('images', filename)
            rows += f"<div class='col-md-3'><img src='{fname}' alt='{label}' class='img-fluid' width='150'/></div>\n"
        rows += "</div><hr>\n"

    # Write the generated HTML to the output file
    with open(output_file, 'w') as outfile:
        outfile.write(html_start + rows + html_end)

# Call the function
generate_html('data.txt', 'index.html')