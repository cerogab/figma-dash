"""Figma API client for fetching design data."""

import requests
from typing import Dict, Any, Optional


class FigmaClient:
    """Client for interacting with the Figma API."""
    
    BASE_URL = "https://api.figma.com/v1"
    
    def __init__(self, api_token: str):
        """Initialize the Figma client with an API token.
        
        Args:
            api_token: Personal access token from Figma
        """
        self.api_token = api_token
        self.headers = {
            "X-Figma-Token": api_token
        }
    
    def get_file(self, file_key: str) -> Optional[Dict[str, Any]]:
        """Fetch a Figma file by its key.
        
        Args:
            file_key: The Figma file key/ID
            
        Returns:
            Dictionary containing the file data, or None if request fails
        """
        url = f"{self.BASE_URL}/files/{file_key}"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Figma file: {e}")
            return None
    
    def get_file_components(self, file_key: str) -> Optional[Dict[str, Any]]:
        """Fetch components from a Figma file.
        
        Args:
            file_key: The Figma file key/ID
            
        Returns:
            Dictionary containing the file components, or None if request fails
        """
        url = f"{self.BASE_URL}/files/{file_key}/components"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Figma components: {e}")
            return None
    
    def get_file_styles(self, file_key: str) -> Optional[Dict[str, Any]]:
        """Fetch styles from a Figma file.
        
        Args:
            file_key: The Figma file key/ID
            
        Returns:
            Dictionary containing the file styles, or None if request fails
        """
        url = f"{self.BASE_URL}/files/{file_key}/styles"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Figma styles: {e}")
            return None
