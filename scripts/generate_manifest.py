#!/usr/bin/env python3
"""Scans posts/*.md, reads frontmatter, and writes posts/manifest.json."""
import json
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(SCRIPT_DIR, "..", "posts")


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    fm_text = text[3:end].strip()
    body = text[end + 3:].strip()
    fields = {}
    lines = fm_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" not in line:
            i += 1
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip().strip('"\'')
        if value == "|":
            block = []
            i += 1
            while i < len(lines) and (lines[i].startswith("  ") or lines[i].strip() == ""):
                block.append(lines[i][2:] if lines[i].startswith("  ") else "")
                i += 1
            fields[key] = "\n".join(block).rstrip()
        else:
            fields[key] = value
            i += 1
    return fields, body


def coerce(fields):
    if "reading_time" in fields:
        try:
            fields["reading_time"] = int(fields["reading_time"])
        except ValueError:
            fields["reading_time"] = 5
    fields["featured"] = fields.get("featured", "false").lower() == "true"
    return fields


def main():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith(".md"):
            continue
        slug = filename[:-3]
        with open(os.path.join(POSTS_DIR, filename), encoding="utf-8") as f:
            raw = f.read()
        fields, _ = parse_frontmatter(raw)
        fields = coerce(fields)
        posts.append({
            "slug": slug,
            "title": fields.get("title", slug),
            "date": fields.get("date", ""),
            "tag": fields.get("tag", ""),
            "reading_time": fields.get("reading_time", 5),
            "excerpt": fields.get("excerpt", ""),
            "featured": fields.get("featured", False),
            "preview": fields.get("preview", ""),
        })

    posts.sort(key=lambda p: p["date"], reverse=True)

    out = os.path.join(POSTS_DIR, "manifest.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

    print(f"manifest.json gerado com {len(posts)} post(s).")


if __name__ == "__main__":
    main()
