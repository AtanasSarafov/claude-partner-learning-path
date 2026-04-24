from mcp.server.fastmcp import FastMCP
from tools.math import add
from tools.document import document_path_to_markdown
from tools.file import read_file

mcp = FastMCP("docs")

mcp.tool()(add)
mcp.tool()(document_path_to_markdown)
mcp.tool()(read_file)

if __name__ == "__main__":
    mcp.run()
