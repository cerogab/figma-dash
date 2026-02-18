"""Format design features into a readable outline."""

from typing import Dict, Any


class OutlineFormatter:
    """Format extracted design features into a readable outline."""
    
    @staticmethod
    def format_outline(features: Dict[str, Any]) -> str:
        """Format features into a text outline.
        
        Args:
            features: Dictionary of extracted design features
            
        Returns:
            Formatted outline string
        """
        lines = []
        
        # Header
        lines.append("=" * 60)
        lines.append(f"FIGMA DESIGN OUTLINE: {features.get('file_name', 'Untitled')}")
        lines.append("=" * 60)
        lines.append("")
        
        # Components section
        components = features.get("components", {})
        if components:
            lines.append("📦 COMPONENTS")
            lines.append("-" * 60)
            for comp_id, comp_data in components.items():
                lines.append(f"  • {comp_data.get('name', 'Unnamed Component')}")
                if comp_data.get('description'):
                    lines.append(f"    Description: {comp_data['description']}")
            lines.append(f"\n  Total: {len(components)} component(s)")
            lines.append("")
        
        # Frames section
        frames = features.get("frames", [])
        if frames:
            lines.append("🖼️  FRAMES & PAGES")
            lines.append("-" * 60)
            for frame in frames:
                frame_type = frame.get("type", "")
                frame_name = frame.get("name", "Unnamed")
                lines.append(f"  • {frame_name} ({frame_type})")
            lines.append(f"\n  Total: {len(frames)} frame(s)")
            lines.append("")
        
        # Colors section
        colors = features.get("colors", [])
        if colors:
            lines.append("🎨 COLOR PALETTE")
            lines.append("-" * 60)
            for i, color in enumerate(colors, 1):
                lines.append(f"  {i}. {color}")
            lines.append(f"\n  Total: {len(colors)} unique color(s)")
            lines.append("")
        
        # Text styles section
        text_styles = features.get("text_styles", [])
        if text_styles:
            lines.append("📝 TEXT STYLES")
            lines.append("-" * 60)
            unique_styles = {}
            for style in text_styles:
                key = f"{style.get('font_family', '')}_{style.get('font_size', '')}_{style.get('font_weight', '')}"
                if key not in unique_styles:
                    unique_styles[key] = style
            
            for i, style in enumerate(unique_styles.values(), 1):
                font_family = style.get("font_family", "Unknown")
                font_size = style.get("font_size", "?")
                font_weight = style.get("font_weight", "?")
                lines.append(f"  {i}. {font_family} - {font_size}px (Weight: {font_weight})")
            lines.append(f"\n  Total: {len(unique_styles)} unique text style(s)")
            lines.append("")
        
        # Summary
        lines.append("=" * 60)
        lines.append("SUMMARY")
        lines.append("=" * 60)
        lines.append(f"Components: {len(components)}")
        lines.append(f"Frames: {len(frames)}")
        lines.append(f"Colors: {len(colors)}")
        lines.append(f"Text Styles: {len(text_styles)}")
        lines.append("=" * 60)
        
        return "\n".join(lines)
