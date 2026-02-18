# figma-dash

A command-line tool to outline important design features from your Figma files.

## Features

Figma Dash extracts and displays an organized outline of your Figma design, including:

- 📦 **Components**: All reusable components with descriptions
- 🖼️ **Frames & Pages**: Page and frame structure
- 🎨 **Color Palette**: All unique colors used in the design
- 📝 **Text Styles**: Font families, sizes, and weights

## Installation

### Prerequisites

- Python 3.7 or higher
- A Figma account with API access

### Install from source

```bash
git clone https://github.com/cerogab/figma-dash.git
cd figma-dash
pip install -r requirements.txt
pip install -e .
```

## Setup

### Get your Figma API Token

1. Go to [Figma Settings](https://www.figma.com/settings)
2. Scroll to **Personal access tokens**
3. Click **Create a new personal access token**
4. Give it a name and copy the token

### Configure the token

You can provide the token in two ways:

**Option 1: Environment Variable (Recommended)**

Create a `.env` file in the project directory:

```bash
cp .env.example .env
# Edit .env and add your token
FIGMA_API_TOKEN=your_actual_token_here
```

**Option 2: Command-line Argument**

Pass the token directly when running the command (see Usage below).

## Usage

### Basic Usage

```bash
figma-dash --file <FIGMA_FILE_URL_OR_KEY>
```

### Examples

**Using a Figma file URL:**

```bash
figma-dash --file https://www.figma.com/file/ABC123DEF456/MyDesignSystem
```

**Using just the file key:**

```bash
figma-dash --file ABC123DEF456
```

**Providing token via command line:**

```bash
figma-dash --file ABC123DEF456 --token your_figma_token_here
```

### Command-line Options

- `--file`, `-f`: Figma file URL or file key (required)
- `--token`, `-t`: Figma API token (optional if set in environment)

## Example Output

```
============================================================
FIGMA DESIGN OUTLINE: My Design System
============================================================

📦 COMPONENTS
------------------------------------------------------------
  • Button/Primary
    Description: Primary action button
  • Button/Secondary
    Description: Secondary action button
  • Card/Default
  
  Total: 3 component(s)

🖼️  FRAMES & PAGES
------------------------------------------------------------
  • Design System (CANVAS)
  • Components (FRAME)
  • Colors (FRAME)
  
  Total: 3 frame(s)

🎨 COLOR PALETTE
------------------------------------------------------------
  1. #0066FF
  2. #00C853
  3. #FF5252
  4. #FFFFFF
  
  Total: 4 unique color(s)

📝 TEXT STYLES
------------------------------------------------------------
  1. Inter - 16px (Weight: 400)
  2. Inter - 24px (Weight: 700)
  3. Roboto - 14px (Weight: 400)
  
  Total: 3 unique text style(s)

============================================================
SUMMARY
============================================================
Components: 3
Frames: 3
Colors: 4
Text Styles: 3
============================================================
```

## How It Works

1. **Connects to Figma API**: Uses your personal access token to authenticate
2. **Fetches File Data**: Retrieves the complete design file structure
3. **Extracts Features**: Analyzes the design tree to identify components, colors, text styles, and frames
4. **Generates Outline**: Formats the extracted information into a readable outline

## Troubleshooting

### "Error: Could not fetch Figma file"

- Verify the file key/URL is correct
- Ensure your API token is valid
- Check that you have access to the file (it should be in your team or shared with you)

### "Error: Figma API token is required"

- Make sure you've set the `FIGMA_API_TOKEN` in your `.env` file, or
- Provide it via the `--token` argument

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

See [LICENSE](LICENSE) file for details.