import csv
import json
import os
import time
from pathlib import Path
from typing import Dict, List

def sanitize_filename(filename: str) -> str:
    """Convert a string into a valid filename."""
    # Replace spaces and special characters with underscores
    return "".join(c if c.isalnum() else "_" for c in filename).lower()

def process_csv_to_snippets(csv_path: str, output_base_dir: str = "snippets"):
    """
    Process a CSV file containing code snippets and create JSON files.
    
    Expected CSV columns:
    - title: The title of the snippet
    - description: Description/documentation of the snippet
    - code: The actual code content
    - language: (optional) Programming language of the snippet
    - tags: (optional) Comma-separated tags
    """
    # Create output directory if it doesn't exist
    Path(output_base_dir).mkdir(parents=True, exist_ok=True)
    
    # List to store all index entries
    index_entries: List[Dict] = []
    
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # Generate unique ID using timestamp and counter
            snippet_id = str(int(time.time() * 1000))
            time.sleep(0.001)  # Ensure unique IDs
            
            # Create a sanitized filename from the title
            filename = sanitize_filename(row['title'])
            
            # Determine the language folder (default to 'misc' if not specified)
            language = row.get('language', 'misc').lower()
            folder_path = os.path.join(output_base_dir, language)
            Path(folder_path).mkdir(parents=True, exist_ok=True)
            
            # Process tags (if present)
            tags = []
            if 'tags' in row and row['tags']:
                tags = [tag.strip() for tag in row['tags'].split(',')]
            
            # Create snippet object
            snippet = {
                "id": snippet_id,
                "title": row['title'],
                "description": row['description'],
                "code": row['code'],
                "language": language,
                "tags": tags,
                "createdAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "path": f"snippets/{language}/{filename}.json"
            }
            
            # Save snippet to JSON file
            snippet_path = os.path.join(folder_path, f"{filename}.json")
            with open(snippet_path, 'w', encoding='utf-8') as f:
                json.dump(snippet, f, indent=2, ensure_ascii=False)
            
            # Add to index entries
            index_entries.append({
                "path": snippet["path"],
                "id": snippet_id
            })
    
    # Create index file
    index = {"snippets": index_entries}
    with open(os.path.join(output_base_dir, "index.json"), 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

def main():
    # Update these values as needed
    csv_path = "queries.csv"  # Path to your CSV file
    output_dir = "app/snippets"    # Base directory for output files
    
    try:
        process_csv_to_snippets(csv_path, output_dir)
        print(f"Successfully processed snippets from {csv_path}")
        print(f"Output files created in {output_dir}")
    except Exception as e:
        print(f"Error processing snippets: {e}")

if __name__ == "__main__":
    main()