from pathlib import Path

# Set these variables
SOURCE_DIR = Path("S:/dfs/yanorra/yanorra-wiki/Wiki")
TOP_FILES = ["S:/dfs/yanorra/yanorra-wiki/README.md", "S:/dfs/yanorra/yanorra-wiki/Indices/nations.md"]
OUTPUT_FILE = Path("S:/dfs/yanorra/yanorra-wiki/tools/combined.md")
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
        for top_file in TOP_FILES:
            top_path = Path(top_file)
            if top_path.is_file():
                out.write(f"-------------------------------------------------------- {top_path.name} -------------------------------------------------------- \n\n")
                with top_path.open("r", encoding="utf-8") as src:
                    content = src.read()
                if STRIP_FRONTMATTER:
                    content = strip_frontmatter(content)
                out.write(content)
                out.write("\n\n")
            else:
                print(f"Warning: Top file '{top_file}' not found. Skipping.")


        for md_file in md_files:
            out.write(f"-------------------------------------------------------- {md_file.name} -------------------------------------------------------- \n\n")

            with md_file.open("r", encoding="utf-8") as src:
                content = src.read()

            if STRIP_FRONTMATTER:
                content = strip_frontmatter(content)

            out.write(content)
            out.write("\n\n")


if __name__ == "__main__":
    combine_markdown_files(SOURCE_DIR, OUTPUT_FILE)