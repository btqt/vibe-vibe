"""
Markdown to HTML Converter for Vietnamese Documentation

Usage:
    python scripts/md_to_html.py <root_directory> [--recursive]

    Example:
    python scripts/md_to_html.py docs --recursive

Description:
    - Scans for *_vi.md files in the specified directory.
    - Rewrites markdown links ending in .md to .html.
    - Converts the markdown content to HTML.
    - Saves the output as *_vi.html in the same directory.
    - Preserves external links and non-md links.
"""

import os
import re
import argparse
import sys
import markdown

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{ font-family: system-ui, -apple-system, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; color: #333; }}
        pre {{ background: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }}
        code {{ background: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-family: monospace; }}
        a {{ color: #007bff; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        img {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
{content}
</body>
</html>
"""

def find_markdown_files(root_dir, recursive=False):
    """
    Yields paths to *_vi.md files.
    """
    if recursive:
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith('_vi.md'):
                    yield os.path.join(dirpath, filename)
    else:
        if os.path.exists(root_dir) and os.path.isdir(root_dir):
            for filename in os.listdir(root_dir):
                if filename.endswith('_vi.md'):
                    yield os.path.join(root_dir, filename)

def rewrite_links(content):
    """
    Rewrites internal .md links to .html.
    Returns (new_content, changes_list).
    """
    changes = []
    
    # Regex explanation:
    # (\[.*?\])  -> Group 1: The link text, e.g. [My Page] or ![Image]
    # \(         -> Literal opening parenthesis
    # ([^)\s]+)  -> Group 2: The URL. Matches anything except closing paren or whitespace. 
    #               (This is a simplification, assumes no spaces in URLs for now, 
    #                or at least no spaces without quoting, but standard markdown often allows spaces if encoded or quoted. 
    #                Standard markdown link is [text](url "title"). 
    #                The simplified regex might fail on "title", so let's handle it slightly better.)
    #
    # Better Regex for [text](url "title") handling:
    # details: 
    #   \[([^\]]*)\]        Matches [text]
    #   \(                  Matches (
    #     ([^ ")]+)         Matches URL (no spaces, no quotes, no closing paren) -> Group 2
    #     (?: "[^"]*")?     Optional "title"
    #   \)                  Matches )
    
    link_pattern = re.compile(r'(\[[^\]]*\])\(([^ ")]+)(?: "[^"]*")?\)')

    def callback(match):
        full_match = match.group(0)
        text_part = match.group(1)
        url_part = match.group(2)
        
        # Check constraints
        
        # 1. External links
        if re.match(r'^(http://|https://|ftp://|mailto:)', url_part):
            return full_match
            
        # 2. Anchors only
        if url_part.startswith('#'):
            return full_match
            
        # 3. Already html
        if '.html' in url_part:
            return full_match
            
        # 4. Check extension
        # We process query params/fragments if attached
        # url_part might be "file.md#sub" or "file.md?q=1"
        
        # Split fragment/query
        # Simple parsing:
        base_url = url_part
        suffix = ""
        
        if '#' in base_url:
            parts = base_url.split('#', 1)
            base_url = parts[0]
            suffix = '#' + parts[1]
        elif '?' in base_url:
             parts = base_url.split('?', 1)
             base_url = parts[0]
             suffix = '?' + parts[1]
             
        if base_url.endswith('.md'):
            # Perform rewrite
            new_base = base_url[:-3] + '.html'
            new_url = new_base + suffix
            
            # Reconstruct the link
            # We need to be careful if there was a title in the original match
            # My current regex group 2 only captured the URL part.
            # So reconstructing 'full_match' from parts is safer if I replace the URL in the full string?
            # Or just assume no title for now?
            # Actually, `match.group(0)` is the whole string.
            # I can just replace the url_part within the full_match? 
            # Be careful if url_part appears in text_part.
            
            # Safer way: return f"{text_part}({new_url})"
            # But what if there was a title?
            # The regex `([^ ")]+)` stopped before the space+title.
            # So `match.group(0)` contains the title if present.
            # `url_part` is just the url.
            # So I can replace `url_part` with `new_url`.
            # BUT, simple string replace might be dangerous if `url_part` is very short.
            
            # Let's inspect the suffix of the match group(0) after the url_part found.
            # `match.start(2)` give start index of url_part.
            # `match.end(2)` gives end index.
            
            start_idx = match.start(2)
            end_idx = match.end(2)
            
            # Calculate offset because match indices are relative to the string sent to sub? 
            # No, match object in `sub` works.
            
            # Actually, much simpler:
            # Re-construct:
            # We have text_part.
            # We have the rest of the string after the URL?
            # The regex matched the whole `[...](...)`. 
            # The part after url_part (group 2) is `(?: "[^"]*")?\)`
            
            # Let's capture the 'tail' in the regex.
            pass
            
            changes.append(f"{url_part} -> {new_url}")
            
            # To preserve title, we need to locate where url_part is in full_match
            # It should be right after `](` or `] (`? No standard is `](`.
            
            # Let's rely on simple string substitution for this specific match segment logic
            # OR better: use a regex with 3 groups: (prefix)(url)(suffix)
            # pattern: `(\[[^\]]*\]\()([^ ")]+)((?: "[^"]*")?\))`
            # Group 1: `[text](`
            # Group 2: `url`
            # Group 3: ` "title")` or `)`
            
            # This is safer.
            return full_match.replace(url_part, new_url, 1) 
            # Note: replace(..., 1) replaces only first occurrence. 
            # Since url_part is inside the parens, and we typically don't fail unless the link text contains the exact same url string.
            # e.g. [page.md](page.md). Replace 1 would replace the first one. That's WRONG.
            # We want to replace the ONE in the parentheses.
            
            # Let's try the 3-group regex approach inside the callback?
            # Or just refine the main regex.
        
        return full_match

    # Refined Regex with 3 groups
    # Group 1: `[...](`  (Lazy match on [...])
    # Group 2: `url`     (No spaces, quotes, parens)
    # Group 3: `...`     (Title + closing paren)
    
    pattern_detailed = re.compile(r'(\[[^\]]*\]\()([^ ")]+)(.*?\))')
    
    def detailed_callback(match):
        prefix = match.group(1)
        url = match.group(2)
        suffix = match.group(3)
        
        # Logic repeated
        if re.match(r'^(http://|https://|ftp://|mailto:)', url):
            return match.group(0)
            
        base_url = url
        extra = ""
        if '#' in base_url:
            p = base_url.split('#', 1)
            base_url = p[0]
            extra = '#' + p[1]
        elif '?' in base_url:
            p = base_url.split('?', 1)
            base_url = p[0]
            extra = '?' + p[1]
            
        if base_url.endswith('.md'):
            new_url = base_url[:-3] + '.html' + extra
            changes.append(f"{url} -> {new_url}")
            return f"{prefix}{new_url}{suffix}"
            
        return match.group(0)

    new_content = pattern_detailed.sub(detailed_callback, content)
    return new_content, changes

def convert_markdown_to_html(content):
    """
    Converts markdown content to HTML string.
    """
    html_body = markdown.markdown(content, extensions=['extra', 'tables', 'fenced_code'])
    return html_body

def main():
    parser = argparse.ArgumentParser(description="Convert Vietnamese Markdown files to HTML.")
    parser.add_argument("root_dir", help="Root directory to scan")
    parser.add_argument("--recursive", action="store_true", help="Recursively scan subdirectories")
    
    args = parser.parse_args()
    
    scan_dir = args.root_dir
    recursive = args.recursive
    
    if not os.path.isdir(scan_dir):
        print(f"Error: Directory {scan_dir} not found.")
        sys.exit(1)
        
    print(f"Scanning directory: {scan_dir} (Recursive: {recursive})")
    
    files = list(find_markdown_files(scan_dir, recursive))
    if not files:
        print("No *_vi.md files found.")
        return

    print(f"Found {len(files)} files.")
    
    for file_path in files:
        print(f"\nProcessing: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Rewrite links
            new_content, changes = rewrite_links(content)
            for change in changes:
                print(f"  [Link Rewrite] {change}")
            
            # Convert to HTML
            html_body = convert_markdown_to_html(new_content)
            
            # Wrap in template
            filename = os.path.basename(file_path)
            title = filename.replace('_vi.md', '').replace('-', ' ').title()
            full_html = HTML_TEMPLATE.format(title=title, content=html_body)
            
            # Determine output filename
            output_path = os.path.splitext(file_path)[0] + '.html'
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_html)
                
            print(f"  Saved: {output_path}")
            
        except Exception as e:
            print(f"  Error processing {file_path}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
