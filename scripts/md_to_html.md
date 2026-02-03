# Vietnamese Documentation Tools Walkthrough

## 1. Link Rewriter ([scripts/rewrite_vi_links.py](file:///d:/00_wip/99_learning/03_AI/github_vibe-vibe/scripts/rewrite_vi_links.py))

See previous section.

## 2. Markdown to HTML Converter ([scripts/md_to_html.py](file:///d:/00_wip/99_learning/03_AI/github_vibe-vibe/scripts/md_to_html.py))

I have created a Python script [scripts/md_to_html.py](file:///d:/00_wip/99_learning/03_AI/github_vibe-vibe/scripts/md_to_html.py) that converts Vietnamese Markdown files to HTML and updates links to point to `.html` files.

### Features

- **File Discovery**: Recursively finds `*_vi.md` files.
- **Link Rewriting**:
  - `[Text](page.md)` -> `[Text](page.html)`
  - `[Text](page.md#frag)` -> `[Text](page.html#frag)`
  - `[Text](page.md?q=1)` -> `[Text](page.html?q=1)`
  - Preserves external links, anchors, and existing `.html` links.
- **HTML Conversion**: Uses the [markdown](file:///d:/00_wip/99_learning/03_AI/github_vibe-vibe/scripts/md_to_html.py#49-63) library to generate HTML.
- **Templating**: Wraps output in a clean, responsive HTML template with basic styling.

### Usage

Run the script pointing to your documentation directory:

```bash
python scripts/md_to_html.py docs --recursive
```

This will create `*_vi.html` files next to the original `*_vi.md` files.

### Verification

I verified the core logic with a unit test suite [scripts/test_md_to_html_logic.py](file:///d:/00_wip/99_learning/03_AI/github_vibe-vibe/scripts/test_md_to_html_logic.py) covering:

- Standard links
- External links (ignored)
- Already HTML links (ignored)
- Links with query parameters and fragments
- Image links ending in [.md](file:///d:/00_wip/99_learning/03_AI/github_vibe-vibe/README.md) (rewritten)
- Image links ending in `.png` (ignored)
- Links with titles
