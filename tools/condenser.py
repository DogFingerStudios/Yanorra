from pathlib import Path

# Set these variables
SOURCE_DIR = Path("/path/to/your/markdown/files")
OUTPUT_FILE = Path("/path/to/output/combined.md")
STRIP_FRONTMATTER = True


def strip_frontmatter(content: str) -> str:
    """
    Removes YAML-style FrontMatter from the beginning of a Markdown file.

    FrontMatter is expected to look like:

    ---
    title: Example
    tags: [one, two]
    ---
    """
    lines = content.splitlines(keepends=True)

    if not lines:
        return content

    # FrontMatter must start on the first line
    if lines[0].strip() != "---":
        return content

    # Find the closing ---
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "".join(lines[i + 1:]).lstrip()

    # If no closing --- is found, leave the content unchanged
    return content


def combine_markdown_files(source_dir: Path, output_file: Path) -> None:
    md_files = sorted(source_dir.glob("*.md"))

    with output_file.open("w", encoding="utf-8") as out:
        for md_file in md_files:
            out.write(f"-------------- {md_file.name} -------------\n\n")

            with md_file.open("r", encoding="utf-8") as src:
                content = src.read()

            if STRIP_FRONTMATTER:
                content = strip_frontmatter(content)

            out.write(content)
            out.write("\n\n")


if __name__ == "__main__":
    combine_markdown_files(SOURCE_DIR, OUTPUT_FILE)