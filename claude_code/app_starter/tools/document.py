from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pathlib import Path
from pydantic import Field


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(
    path: str = Field(description="Absolute or relative path to a PDF or DOCX file"),
) -> str:
    """Convert a PDF or DOCX file to markdown-formatted text.

    Reads the file at the given path and converts its contents to markdown
    using the MarkItDown library.

    When to use:
    - When you have a local file path to a PDF or DOCX document
    - When you need to extract readable text from a document for further processing

    When not to use:
    - When you already have the file contents as bytes (use binary_document_to_markdown instead)
    - For file types other than PDF or DOCX

    Examples:
    >>> document_path_to_markdown("/tmp/report.pdf")
    '# Report Title\\n\\nSome content...'
    >>> document_path_to_markdown("/tmp/notes.docx")
    '# Notes\\n\\n- Item one...'
    """
    file = Path(path)

    if not file.exists():
        raise ValueError(f"File not found: {path}")

    suffix = file.suffix.lstrip(".").lower()
    if suffix not in ("pdf", "docx"):
        raise ValueError(f"Unsupported file type '.{suffix}': must be pdf or docx")

    return binary_document_to_markdown(file.read_bytes(), suffix)
