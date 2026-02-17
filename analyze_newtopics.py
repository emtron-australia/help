#!/usr/bin/env python3
import os
import re
import json
from pathlib import Path

def sanitize_filename(title):
    """Convert title to filesystem-safe filename"""
    if not title:
        return "placeholder-empty"

    # Convert to lowercase
    name = title.lower()

    # Remove special characters, keep only alphanumeric, spaces, and hyphens
    name = re.sub(r'[^a-z0-9\s\-]', '', name)

    # Replace multiple spaces with single hyphen
    name = re.sub(r'\s+', '-', name)

    # Remove multiple consecutive hyphens
    name = re.sub(r'-+', '-', name)

    # Remove leading/trailing hyphens
    name = name.strip('-')

    if not name:
        return "placeholder-empty"

    return f"{name}.md"

def extract_title(content):
    """Extract title from file content"""
    lines = content.split('\n')

    # First, check for frontmatter title
    if lines[0].strip() == '---':
        for line in lines[1:]:
            if line.strip() == '---':
                break
            if line.startswith('title:'):
                # Extract title from YAML
                title = line.replace('title:', '').strip().strip('"').strip("'")
                return title

    # If no frontmatter title, look for markdown heading
    for line in lines:
        if line.startswith('#'):
            title = line.lstrip('#').strip()
            return title
        # Use first non-empty, non-yaml line
        elif line.strip() and not line.startswith('---'):
            return line.strip()

    return None

def analyze_files():
    """Analyze all Newtopic files"""
    base_path = r'c:\Users\phil_\dev\online-help\content\engine-management\uncategorised'
    pattern = os.path.join(base_path, 'Newtopic*.md')

    # Get all matching files
    files = sorted(Path(base_path).glob('Newtopic*.md'))

    mapping = []
    empty_count = 0
    categories = {}

    print(f"Found {len(files)} files to process")

    for idx, file_path in enumerate(files):
        if (idx + 1) % 50 == 0:
            print(f"Processing file {idx + 1} of {len(files)}...")

        original_name = file_path.name

        try:
            content = file_path.read_text(encoding='utf-8', errors='replace')
        except Exception as e:
            content = ""

        title = extract_title(content)

        if not title or title == '[EMPTY FILE]':
            empty_count += 1
            suggested_name = f"placeholder-empty-{empty_count:03d}.md"
            description = "[No content]"
        else:
            suggested_name = sanitize_filename(title)

            # Get first non-heading, non-empty line as description
            lines = content.split('\n')
            description = ""
            skip_frontmatter = True
            for line in lines:
                if skip_frontmatter:
                    if line.strip() == '---' and lines[0].strip() == '---':
                        # This is the closing --- of frontmatter
                        skip_frontmatter = False
                    continue

                line = line.strip()
                if line and not line.startswith('#') and not line.startswith('---'):
                    # Clean up some markdown syntax for description
                    description = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', line)[:100]
                    break

            if not description:
                description = "[No additional content]"

        # Extract category from title (first word or key term)
        if title:
            first_word = title.split()[0].lower()
            categories[first_word] = categories.get(first_word, 0) + 1

        mapping.append({
            "originalFilename": original_name,
            "suggestedFilename": suggested_name,
            "title": title if title else "[EMPTY]",
            "description": description
        })

    # Check for filename collisions
    suggested_names = [m["suggestedFilename"] for m in mapping]
    duplicates = {}
    for name in suggested_names:
        duplicates[name] = duplicates.get(name, 0) + 1

    duplicate_names = {k: v for k, v in duplicates.items() if v > 1}

    # Create summary
    summary = {
        "totalFiles": len(files),
        "emptyOrMinimalFiles": empty_count,
        "fileWithContent": len(files) - empty_count,
        "duplicateFilenameCount": len(duplicate_names),
        "duplicateFilenames": duplicate_names if duplicate_names else {},
        "topCategories": sorted(categories.items(), key=lambda x: x[1], reverse=True)[:20]
    }

    output = {
        "summary": summary,
        "mapping": mapping
    }

    # Save to JSON
    output_path = os.path.join(base_path, '..', '..', '..', 'newtopic-mapping.json')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nAnalysis complete!")
    print(f"Total files: {len(files)}")
    print(f"Files with content: {len(files) - empty_count}")
    print(f"Empty/minimal files: {empty_count}")
    print(f"Duplicate filenames: {len(duplicate_names)}")
    print(f"\nMapping saved to: {output_path}")

    return output

if __name__ == '__main__':
    result = analyze_files()
    print("\n=== Summary ===")
    print(json.dumps(result['summary'], indent=2, ensure_ascii=False))
