"""
Web Scraping in Python - Main Entry Point

This project demonstrates different web scraping techniques:
- beauty_soup.py: Using BeautifulSoup to parse HTML
- regex_soup.py: Using regex for simple pattern matching
- mech_soup.py: Using MechanicalSoup for browser automation

Run this file for a quick demo, or run individual scripts for specific examples.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import apidection as apidection
from apidection import predict
predict()



def main():
    print("=" * 50)
    print("Web Scraping Demo - BeautifulSoup Example")
    print("=" * 50)
    
    url = "https://www.bromcomvle.com/Home/Dashboard"
    print(f"\nFetching: {url}")
    
    try:
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        
        print(f"\nPage Title: {soup.title.string}")
        
        images = soup.find_all("img")
        print(f"Images found: {len(images)}")
        for img in images:
            src = img.get("src", "No source")
            print(f"  - {src}")
        
        print("\n" + "=" * 50)
        print("Demo complete! Try running individual scripts:")
        print("  python beauty_soup.py  - BeautifulSoup parsing")
        print("  python regex_soup.py   - Regex-based parsing")
        print("  python mech_soup.py    - MechanicalSoup browser automation")
        print("=" * 50)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
