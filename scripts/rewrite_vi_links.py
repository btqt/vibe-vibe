import os
import re
import argparse
import sys

def rewrite_links(root_dir, recursive=True, dry_run=False):
    """
    Scans *_vi.md files in root_dir.
    Rewrites links to non-vi files (e.g. guide.md) to their _vi counterpart (guide_vi.md)
    if the _vi counterpart exists.
    """
    
    # Regex to find markdown links: [text](path)
    # This is a basic regex and might need refinement for complex cases, 
    # but covers standard [link](url)
    link_pattern = re.compile(r'(\[.*?\])\((.*?)\)')

    for dirpath, _, filenames in os.walk(root_dir):
        if not recursive and dirpath != root_dir:
            continue
            
        for filename in filenames:
            if filename.endswith('_vi.md'):
                file_path = os.path.join(dirpath, filename)
                process_file(file_path, link_pattern, dry_run)

def process_file(file_path, link_pattern, dry_run):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return

    new_content = content
    modifications = []

    def replace_callback(match):
        full_match = match.group(0)
        text_part = match.group(1)
        url_part = match.group(2)

        # Ignore absolute URLs or anchors
        if url_part.startswith(('http://', 'https://', '#', 'mailto:')):
            return full_match
        
        # Check if the link already points to a _vi file
        if '_vi.md' in url_part:
            return full_match

        # We are looking for links to .md files
        if not url_part.endswith('.md'):
            return full_match
            
        # Construct the potential _vi filename
        # This handles cases like: ./foo.md, ../foo.md, foo.md, sub/foo.md
        # We want to insert _vi before .md
        
        # Split into path and extension
        base, ext = os.path.splitext(url_part)
        # e.g. ./guide -> ./guide_vi.md
        candidate_link = f"{base}_vi{ext}"

        # Now we need to check if this candidate file actually exists
        # relative to the current file (file_path)
        
        current_dir = os.path.dirname(file_path)
        
        # Resolve the path
        # Note: urls in markdown might use forward slashes even on Windows
        # so we should treat them as posix paths for the sake of joining,
        # but os.path.exists needs standard OS paths.
        
        # Convert url path to system path for checking existence
        system_url_part = candidate_link.replace('/', os.sep)
        candidate_abs_path = os.path.normpath(os.path.join(current_dir, system_url_part))
        
        if os.path.exists(candidate_abs_path) and os.path.isfile(candidate_abs_path):
            # The _vi file exists!
            new_link = f"{text_part}({candidate_link})"
            if new_link != full_match:
                modifications.append(f"  Line change: {url_part} -> {candidate_link}")
                return new_link
        
        return full_match

    new_content = link_pattern.sub(replace_callback, content)

    if modifications:
        print(f"Update needed for: {file_path}")
        for mod in modifications:
            print(mod)
        
        if not dry_run:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  Written changes to {file_path}")
            except Exception as e:
                print(f"  Error writing {file_path}: {e}", file=sys.stderr)
    else:
        # print(f"No changes for {file_path}")
        pass

def main():
    parser = argparse.ArgumentParser(description="Rewrite links in Vietnamese Markdown files to point to Vietnamese versions if they exist.")
    parser.add_argument("root_dir", help="Root directory to scan (e.g. docs)")
    parser.add_argument("--no-recursive", action="store_true", help="Do not search subdirectories recursively")
    parser.add_argument("--dry-run", action="store_true", help="Print what would happen without modifying files")

    args = parser.parse_args()

    if not os.path.isdir(args.root_dir):
        print(f"Error: Directory '{args.root_dir}' does not exist.", file=sys.stderr)
        sys.exit(1)

    rewrite_links(args.root_dir, recursive=not args.no_recursive, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
