# Vietnamese Link Rewriter Walkthrough

I have created a Python script [scripts/rewrite_vi_links.py](file:///d:/00_wip/99_learning/03_AI/github_vibe-vibe/scripts/rewrite_vi_links.py) that automatically updates Markdown links in your Vietnamese documentation files.

## What it does

- Scans all `*_vi.md` files in the target directory.
- Finds links to non-Vietnamese files (e.g., `[Link](./guide.md)`).
- Checks if a corresponding [\_vi.md](file:///d:/00_wip/99_learning/03_AI/github_vibe-vibe/README_vi.md) file exists (e.g., `./guide_vi.md`).
- If it exists, rewrites the link to point to it (e.g., `[Link](./guide_vi.md)`).

## Usages

### Dry Run (Recommended first)

Check what changes will be made without modifying any files:

```bash
python scripts/rewrite_vi_links.py docs --dry-run
```

### Apply Changes

Run the script to update the files:

```bash
python scripts/rewrite_vi_links.py docs
```

### Options

- `--no-recursive`: Only scan the specified directory, do not look in subfolders.
- `--help`: key help message.

## Verification

I verified the script using a dedicated test suite [scripts/test_script_logic.py](file:///d:/00_wip/99_learning/03_AI/github_vibe-vibe/scripts/test_script_logic.py) (which I have since cleaned up) and performed a dry-run on your `docs` folder. The tests confirmed that:

1. Valid links to existing `_vi` files are updated.
2. Links to missing `_vi` files are left alone.
3. Links that already point to `_vi` files are untouched.
