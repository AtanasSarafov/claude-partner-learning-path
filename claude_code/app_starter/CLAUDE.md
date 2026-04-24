# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Setup
uv venv && source .venv/bin/activate
uv pip install -e .

# Run MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

## Architecture

This is an MCP (Model Context Protocol) server built with FastMCP. The server exposes Python functions as tools that AI assistants can call.

**Request flow:** MCP client → `main.py` (FastMCP server) → registered tool function → response

### Tool registration

Tools are plain Python functions defined in `tools/` and registered in `main.py`:

```python
mcp = FastMCP("docs")
mcp.tool()(my_function)  # registers the function as an MCP tool
```

Tool parameters use `pydantic.Field` for descriptions, which FastMCP surfaces to the client. Tools are tested independently — no running server is needed for tests.

### Adding a new tool

1. Define the function in the appropriate `tools/*.py` module using `Field` for all parameters.
2. Import and register it in `main.py` with `mcp.tool()(my_function)`.
3. Add tests under `tests/` using the fixture files in `tests/fixtures/` if document conversion is involved.
