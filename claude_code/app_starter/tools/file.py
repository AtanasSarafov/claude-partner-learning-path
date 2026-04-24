from pathlib import Path
from pydantic import Field
from tools.document import binary_document_to_markdown


def read_file(
    path: str = Field(description="Absolute or relative path to a PDF or DOCX file"),
) -> str:
    """Read the contents of a PDF or DOCX file and return as markdown text.

    When to use:
    - When you need to read a local PDF or DOCX file

    When not to use:
    - For plain text or markdown files
    """
    file = Path(path)

    if not file.exists():
        raise ValueError(f"File not found: {path}")

    suffix = file.suffix.lstrip(".").lower()
    if suffix not in ("pdf", "docx"):
        raise ValueError(f"Unsupported file type '.{suffix}': must be pdf or docx")

    return binary_document_to_markdown(file.read_bytes(), suffix)
