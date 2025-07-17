import os
import yaml
from pathlib import Path

POSTS_DIR = "_posts"
TAGS_DIR = "tag"
CATEGORIES_DIR = "category"
TEMPLATE = """---
layout: {type}
title: "{name}"
tag: "{name}"
permalink: /{type}/{name}/
---
"""

def extract_front_matter(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.read()

    if lines.startswith("---"):
        _, front_matter, _ = lines.split("---", 2)
        return yaml.safe_load(front_matter)
    return {}

def collect_taxonomies():
    tags_set = set()
    categories_set = set()

    for post_file in Path(POSTS_DIR).glob("*.md"):
        fm = extract_front_matter(post_file)
        tags = fm.get("tags", [])
        categories = fm.get("categories", [])
        
        if isinstance(tags, str):
            tags_set.add(tags)
        else:
            tags_set.update(tags)

        if isinstance(categories, str):
            categories_set.add(categories)
        else:
            categories_set.update(categories)

    return tags_set, categories_set

def generate_pages(names, path, type_):
    os.makedirs(path, exist_ok=True)
    for name in names:
        filename = f"{name.replace(' ', '-').lower()}.md"
        filepath = Path(path) / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(TEMPLATE.format(name=name, type=type_))
        print(f"✅ Created: {filepath}")

def main():
    tags, categories = collect_taxonomies()
    generate_pages(tags, TAGS_DIR, "tag")
    generate_pages(categories, CATEGORIES_DIR, "category")

if __name__ == "__main__":
    main()
