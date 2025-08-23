# OpenF1 MCP

## Overview

This project provides a Model Context Protocol (MCP) server for the OpenF1 SDK/API. It allows language models and other tools to interact with Formula 1 data in a standardized way.

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1.  **Clone the repository:**

    ```bash
    git clone git@github.com:GianAndreaSechi/openf1.git
    cd openf1/mcp
    ```

2.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the MCP Server

To start the MCP server, run the following command:

```bash
python src/server.py
```

The server will start on `localhost:80` by default.

### Testing with the Inspector

You can use the MCP Inspector to test the server and interact with the available tools.

1.  **Install the Inspector:**

    ```bash
    npx @modelcontextprotocol/inspector
    ```

2.  **Run the Inspector:**

    The Inspector will automatically connect to the MCP server running on `localhost:80`.

## Project Structure

```
.
├── README.md
├── requirements.txt
└── src
    ├── __init__.py
    ├── server.py
    ├── dto
    │   └── McpResponse.py
    └── tools
        └── healthz_tools.py
```

-   `src/server.py`: The main entry point for the MCP server.
-   `src/dto/`: Contains the Data Transfer Objects (DTOs) for the MCP responses.
-   `src/tools/`: Contains the tools that can be invoked by the language model.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
