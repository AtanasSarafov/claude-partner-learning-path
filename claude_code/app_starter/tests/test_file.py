import os
import pytest
from tools.file import read_file


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
PDF_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.pdf")
DOCX_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.docx")


class TestReadFile:
    def test_with_pdf_returns_string(self):
        result = read_file(PDF_FIXTURE)
        assert isinstance(result, str)

    def test_with_pdf_returns_content(self):
        result = read_file(PDF_FIXTURE)
        assert len(result) > 0

    def test_with_docx_returns_string(self):
        result = read_file(DOCX_FIXTURE)
        assert isinstance(result, str)

    def test_with_docx_returns_content(self):
        result = read_file(DOCX_FIXTURE)
        assert len(result) > 0

    def test_pdf_content_accuracy(self):
        result = read_file(PDF_FIXTURE)
        assert "MCP" in result or "Model Context Protocol" in result

    def test_docx_content_accuracy(self):
        result = read_file(DOCX_FIXTURE)
        assert "MCP" in result or "Model Context Protocol" in result

    def test_file_not_found(self):
        with pytest.raises(ValueError, match="File not found"):
            read_file("/tmp/nonexistent_file.pdf")

    def test_directory_raises_error(self, tmp_path):
        with pytest.raises(ValueError):
            read_file(str(tmp_path))

    def test_unsupported_txt_extension(self, tmp_path):
        txt_file = tmp_path / "notes.txt"
        txt_file.write_text("hello")
        with pytest.raises(ValueError, match="Unsupported file type"):
            read_file(str(txt_file))

    def test_unsupported_csv_extension(self, tmp_path):
        csv_file = tmp_path / "data.csv"
        csv_file.write_text("a,b,c")
        with pytest.raises(ValueError, match="Unsupported file type"):
            read_file(str(csv_file))

    def test_no_extension_raises_error(self, tmp_path):
        no_ext_file = tmp_path / "noextension"
        no_ext_file.write_text("hello")
        with pytest.raises(ValueError, match="Unsupported file type"):
            read_file(str(no_ext_file))
