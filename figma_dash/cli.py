"""Command-line interface for Figma Dash."""

import argparse
import os
import sys
from dotenv import load_dotenv

from .client import FigmaClient
from .extractor import DesignFeatureExtractor
from .formatter import OutlineFormatter


def extract_file_key(figma_url_or_key: str) -> str:
    """Extract file key from Figma URL or return key if already provided.
    
    Args:
        figma_url_or_key: Either a Figma file URL or file key
        
    Returns:
        The Figma file key
    """
    # If it's a URL, extract the file key
    if "figma.com/file/" in figma_url_or_key:
        # Format: https://www.figma.com/file/FILE_KEY/Title
        parts = figma_url_or_key.split("figma.com/file/")[1].split("/")
        return parts[0]
    
    # Otherwise, assume it's already a file key
    return figma_url_or_key


def main():
    """Main entry point for the CLI."""
    # Load environment variables
    load_dotenv()
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Outline design features from a Figma file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  figma-dash --file https://www.figma.com/file/ABC123/MyDesign
  figma-dash --file ABC123 --token YOUR_TOKEN
  figma-dash --file ABC123  # Uses FIGMA_API_TOKEN from .env
        """
    )
    
    parser.add_argument(
        "--file", "-f",
        required=True,
        help="Figma file URL or file key"
    )
    
    parser.add_argument(
        "--token", "-t",
        help="Figma API token (or set FIGMA_API_TOKEN environment variable)"
    )
    
    args = parser.parse_args()
    
    # Get API token
    api_token = args.token or os.getenv("FIGMA_API_TOKEN")
    
    if not api_token:
        print("Error: Figma API token is required.")
        print("Provide it via --token argument or FIGMA_API_TOKEN environment variable.")
        print("\nTo get a token:")
        print("1. Go to https://www.figma.com/settings")
        print("2. Scroll to 'Personal access tokens'")
        print("3. Create a new token")
        sys.exit(1)
    
    # Extract file key
    file_key = extract_file_key(args.file)
    
    print(f"Fetching Figma file: {file_key}")
    print("-" * 60)
    
    # Initialize client and fetch file
    client = FigmaClient(api_token)
    file_data = client.get_file(file_key)
    
    if not file_data:
        print("Error: Could not fetch Figma file.")
        print("Please check:")
        print("- The file key/URL is correct")
        print("- Your API token is valid")
        print("- You have access to the file")
        sys.exit(1)
    
    # Extract features
    print("Extracting design features...")
    extractor = DesignFeatureExtractor(file_data)
    features = extractor.extract_all_features()
    
    # Format and display outline
    formatter = OutlineFormatter()
    outline = formatter.format_outline(features)
    
    print("\n")
    print(outline)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
