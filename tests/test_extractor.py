"""Tests for design feature extraction."""

import unittest
from figma_dash.extractor import DesignFeatureExtractor
from figma_dash.formatter import OutlineFormatter


class TestDesignFeatureExtractor(unittest.TestCase):
    """Test the design feature extractor."""
    
    def test_extract_components(self):
        """Test extracting components from file data."""
        file_data = {
            "name": "Test File",
            "document": {
                "type": "DOCUMENT",
                "children": [
                    {
                        "type": "COMPONENT",
                        "id": "1:1",
                        "name": "Button",
                        "description": "A button component",
                        "children": []
                    }
                ]
            }
        }
        
        extractor = DesignFeatureExtractor(file_data)
        features = extractor.extract_all_features()
        
        self.assertEqual(features["file_name"], "Test File")
        self.assertEqual(len(features["components"]), 1)
        self.assertIn("1:1", features["components"])
        self.assertEqual(features["components"]["1:1"]["name"], "Button")
    
    def test_extract_colors(self):
        """Test extracting colors from file data."""
        file_data = {
            "name": "Test File",
            "document": {
                "type": "DOCUMENT",
                "children": [
                    {
                        "type": "RECTANGLE",
                        "name": "Shape",
                        "fills": [
                            {
                                "type": "SOLID",
                                "color": {"r": 1.0, "g": 0.0, "b": 0.0, "a": 1.0}
                            }
                        ],
                        "children": []
                    }
                ]
            }
        }
        
        extractor = DesignFeatureExtractor(file_data)
        features = extractor.extract_all_features()
        
        self.assertEqual(len(features["colors"]), 1)
        self.assertIn("#FF0000", features["colors"])
    
    def test_extract_text_styles(self):
        """Test extracting text styles from file data."""
        file_data = {
            "name": "Test File",
            "document": {
                "type": "DOCUMENT",
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
                    }
                ]
            }
        }
        
        extractor = DesignFeatureExtractor(file_data)
        features = extractor.extract_all_features()
        
        self.assertEqual(len(features["text_styles"]), 1)
        self.assertEqual(features["text_styles"][0]["font_family"], "Inter")
        self.assertEqual(features["text_styles"][0]["font_size"], 24)
        self.assertEqual(features["text_styles"][0]["font_weight"], 700)
    
    def test_extract_frames(self):
        """Test extracting frames from file data."""
        file_data = {
            "name": "Test File",
            "document": {
                "type": "DOCUMENT",
                "children": [
                    {
                        "type": "CANVAS",
                        "name": "Page 1",
                        "children": [
                            {
                                "type": "FRAME",
                                "name": "Frame 1",
                                "children": []
                            }
                        ]
                    }
                ]
            }
        }
        
        extractor = DesignFeatureExtractor(file_data)
        features = extractor.extract_all_features()
        
        self.assertEqual(len(features["frames"]), 2)
        frame_names = [f["name"] for f in features["frames"]]
        self.assertIn("Page 1", frame_names)
        self.assertIn("Frame 1", frame_names)


class TestOutlineFormatter(unittest.TestCase):
    """Test the outline formatter."""
    
    def test_format_outline(self):
        """Test formatting features into an outline."""
        features = {
            "file_name": "Test Design",
            "components": {
                "1:1": {"name": "Button", "description": "A button"}
            },
            "colors": ["#FF0000", "#00FF00"],
            "text_styles": [
                {"font_family": "Inter", "font_size": 16, "font_weight": 400}
            ],
            "frames": [
                {"name": "Page 1", "type": "CANVAS"}
            ]
        }
        
        formatter = OutlineFormatter()
        outline = formatter.format_outline(features)
        
        self.assertIn("Test Design", outline)
        self.assertIn("COMPONENTS", outline)
        self.assertIn("Button", outline)
        self.assertIn("COLOR PALETTE", outline)
        self.assertIn("#FF0000", outline)
        self.assertIn("TEXT STYLES", outline)
        self.assertIn("Inter", outline)
        self.assertIn("FRAMES & PAGES", outline)
        self.assertIn("Page 1", outline)


if __name__ == "__main__":
    unittest.main()
