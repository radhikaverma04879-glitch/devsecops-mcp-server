import os
import json
from mcp.server.mcpserver import MCPServer
from serpapi import Client

# Initialize MCP Server
mcp = MCPServer("DevSecOps & Threat Intel MCP Server")

# Fetch SerpApi Key from Environment variable
SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")

@mcp.tool()
def search_cve_threats(query: str) -> str:
    """
    Searches recent CVE vulnerabilities, exploits, and threat intelligence using SerpApi.
    Input should be a security query like 'CVE-2024-3094 exploit' or 'Log4j vulnerability fix'.
    """
    if not SERPAPI_KEY:
        return "Error: SERPAPI_API_KEY environment variable not set."

    params = {
        "q": f"site:nvd.nist.gov OR site:cve.org OR site:exploit-db.com {query}",
        "engine": "google"
    }

    try:
        client = Client(api_key=SERPAPI_KEY)
        results = client.search(params)
        organic_results = results.get("organic_results", [])

        if not organic_results:
            return "No specific threat intelligence or CVE details found."

        summary = []
        for result in organic_results[:5]:  # Top 5 results
            summary.append(f"Title: {result.get('title')}\nLink: {result.get('link')}\nSnippet: {result.get('snippet')}\n---")

        return "\n".join(summary)
    except Exception as e:
        return f"Error executing threat search: {str(e)}"

if __name__ == "__main__":
    mcp.run()