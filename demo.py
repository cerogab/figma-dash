#!/usr/bin/env python
"""Demo script to show how figma-dash works with sample data."""

from figma_dash.extractor import DesignFeatureExtractor
from figma_dash.formatter import OutlineFormatter


def main():
    """Run a demo with sample Figma file data."""
    
    # Sample Figma file data structure (simplified)
    sample_data = {
        "name": "Design System Demo",
        "document": {
            "type": "DOCUMENT",
            "children": [
                {
                    "type": "CANVAS",
                    "name": "Components Library",
                    "children": [
                        {
                            "type": "FRAME",
                            "name": "Buttons",
                            "children": [
                                {
                                    "type": "COMPONENT",
                                    "id": "1:1",
                                    "name": "Button/Primary",
                                    "description": "Primary action button with brand color",
                                    "fills": [
                                        {
                                            "type": "SOLID",
                                            "color": {"r": 0.0, "g": 0.4, "b": 1.0, "a": 1.0}
                                        }
                                    ],
                                    "children": [
                                        {
                                            "type": "TEXT",
                                            "name": "Label",
                                            "style": {
                                                "fontFamily": "Inter",
                                                "fontSize": 16,
                                                "fontWeight": 600
                                            },
                                            "children": []
                                        }
                                    ]
                                },
                                {
                                    "type": "COMPONENT",
                                    "id": "1:2",
                                    "name": "Button/Secondary",
                                    "description": "Secondary action button with outline style",
                                    "fills": [
                                        {
                                            "type": "SOLID",
                                            "color": {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0}
                                        }
                                    ],
                                    "children": []
                                }
                            ]
                        },
                        {
                            "type": "FRAME",
                            "name": "Cards",
                            "children": [
                                {
                                    "type": "COMPONENT",
                                    "id": "2:1",
                                    "name": "Card/Default",
                                    "description": "Standard card component with shadow",
                                    "fills": [
                                        {
                                            "type": "SOLID",
                                            "color": {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0}
                                        }
                                    ],
                                    "children": [
                                        {
                                            "type": "TEXT",
                                            "name": "Title",
                                            "style": {
                                                "fontFamily": "Inter",
                                                "fontSize": 24,
                                                "fontWeight": 700
                                            },
                                            "children": []
                                        },
                                        {
                                            "type": "TEXT",
                                            "name": "Body",
                                            "style": {
                                                "fontFamily": "Inter",
                                                "fontSize": 14,
                                                "fontWeight": 400
                                            },
                                            "fills": [
                                                {
                                                    "type": "SOLID",
                                                    "color": {"r": 0.4, "g": 0.4, "b": 0.4, "a": 1.0}
                                                }
                                            ],
                                            "children": []
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "CANVAS",
                    "name": "Color Palette",
                    "children": [
                        {
                            "type": "FRAME",
                            "name": "Brand Colors",
                            "children": [
                                {
                                    "type": "RECTANGLE",
                                    "name": "Primary",
                                    "fills": [
                                        {
                                            "type": "SOLID",
                                            "color": {"r": 0.0, "g": 0.4, "b": 1.0, "a": 1.0}
                                        }
                                    ],
                                    "children": []
                                },
                                {
                                    "type": "RECTANGLE",
                                    "name": "Success",
                                    "fills": [
                                        {
                                            "type": "SOLID",
                                            "color": {"r": 0.0, "g": 0.78, "b": 0.33, "a": 1.0}
                                        }
                                    ],
                                    "children": []
                                },
                                {
                                    "type": "RECTANGLE",
                                    "name": "Error",
                                    "fills": [
                                        {
                                            "type": "SOLID",
                                            "color": {"r": 1.0, "g": 0.32, "b": 0.32, "a": 1.0}
                                        }
                                    ],
                                    "children": []
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }
    
    print("=" * 60)
    print("FIGMA-DASH DEMO")
    print("=" * 60)
    print("\nThis demo shows how figma-dash extracts and outlines")
    print("design features from a Figma file.\n")
    print("Processing sample design file...")
    print("-" * 60)
    
    # Extract features
    extractor = DesignFeatureExtractor(sample_data)
    features = extractor.extract_all_features()
    
    # Format and display outline
    formatter = OutlineFormatter()
    outline = formatter.format_outline(features)
    
    print("\n")
    print(outline)
    
    print("\n" + "=" * 60)
    print("This is what figma-dash outputs when you run:")
    print("  figma-dash --file YOUR_FIGMA_FILE_URL")
    print("=" * 60)


if __name__ == "__main__":
    main()
