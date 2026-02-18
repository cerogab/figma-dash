"""Extract and analyze design features from Figma file data."""

from typing import Dict, Any, List, Set


class DesignFeatureExtractor:
    """Extract important design features from Figma file data."""
    
    def __init__(self, file_data: Dict[str, Any]):
        """Initialize the extractor with Figma file data.
        
        Args:
            file_data: The complete Figma file data from the API
        """
        self.file_data = file_data
        self.document = file_data.get("document", {})
        self.components = {}
        self.styles = {}
        self.colors = set()
        self.text_styles = []
        self.frames = []
        
    def extract_all_features(self) -> Dict[str, Any]:
        """Extract all design features from the file.
        
        Returns:
            Dictionary containing all extracted features
        """
        self._traverse_node(self.document)
        
        return {
            "file_name": self.file_data.get("name", "Untitled"),
            "components": self.components,
            "colors": sorted(list(self.colors)),
            "text_styles": self.text_styles,
            "frames": self.frames,
        }
    
    def _traverse_node(self, node: Dict[str, Any], depth: int = 0):
        """Recursively traverse the node tree to extract features.
        
        Args:
            node: Current node in the tree
            depth: Current depth in the tree
        """
        node_type = node.get("type", "")
        node_name = node.get("name", "")
        
        # Extract components
        if node_type == "COMPONENT":
            self.components[node.get("id", "")] = {
                "name": node_name,
                "description": node.get("description", ""),
            }
        
        # Extract frames/pages
        if node_type in ["FRAME", "CANVAS"]:
            self.frames.append({
                "name": node_name,
                "type": node_type,
            })
        
        # Extract colors from fills
        if "fills" in node:
            for fill in node.get("fills", []):
                if fill.get("type") == "SOLID" and "color" in fill:
                    color = fill["color"]
                    rgb = self._color_to_hex(color)
                    if rgb:
                        self.colors.add(rgb)
        
        # Extract text styles
        if node_type == "TEXT":
            style = node.get("style", {})
            if style:
                text_style = {
                    "font_family": style.get("fontFamily", ""),
                    "font_size": style.get("fontSize", ""),
                    "font_weight": style.get("fontWeight", ""),
                }
                if text_style not in self.text_styles:
                    self.text_styles.append(text_style)
        
        # Recursively process children
        for child in node.get("children", []):
            self._traverse_node(child, depth + 1)
    
    def _color_to_hex(self, color: Dict[str, float]) -> str:
        """Convert Figma color object to hex string.
        
        Args:
            color: Color object with r, g, b, a values (0-1 range)
            
        Returns:
            Hex color string (e.g., "#FF5733")
        """
        try:
            r = int(color.get("r", 0) * 255)
            g = int(color.get("g", 0) * 255)
            b = int(color.get("b", 0) * 255)
            return f"#{r:02X}{g:02X}{b:02X}"
        except (ValueError, TypeError):
            return ""
