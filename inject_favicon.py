file_path = r'C:\Document\Profile\my-portfolio\portfolio_v7.html'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    favicon_tag = '  <link rel="icon" type="image/svg+xml" href="favicon.svg">\n'

    # Inject after <meta charset>
    old = '<meta charset="UTF-8">'
    new = '<meta charset="UTF-8">\n' + favicon_tag

    if 'rel="icon"' not in content:
        content = content.replace(old, new, 1)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Favicon injected successfully.")
    else:
        # Replace existing favicon
        import re
        content = re.sub(r'<link rel="icon"[^>]+>', favicon_tag.strip(), content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Favicon replaced successfully.")

except Exception as e:
    print(f"Error: {e}")
