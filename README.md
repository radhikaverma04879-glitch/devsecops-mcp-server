# DevSecOps & Cyber Threat Intelligence MCP Server

An Model Context Protocol (MCP) server integrated with SerpApi to fetch real-time vulnerability advisories, CVE details, and threat intelligence. Built for the SerpApi India Hackathon 2026.

## Features
- **Real-Time Threat Search**: Queries sources like NVD (NIST), CVE.org, and Exploit-DB via SerpApi.
- **Secure Configuration**: Uses environment variables for API key management following DevSecOps best practices.
- **MCP Native**: Standard STDIO transport interface for integration with Claude Desktop, Cursor, or custom LLM clients.

## Quick Start

### 1. Prerequisites
- Python 3.10+
- Virtual Environment (`python3-venv`)

### 2. Setup & Installation
```bash
# Clone repository & navigate into directory
cd devsecops-mcp-server

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt