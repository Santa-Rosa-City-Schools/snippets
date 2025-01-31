# scripts/generate_index.py
import json
import os
from pathlib import Path

def generate_index():
    snippets_dir = Path("snippets")
    index = {"snippets": []}
    
    # Walk through all JSON files in the snippets directory
    for json_file in snippets_dir.rglob("*.json"):
        # Skip index.json itself
        if json_file.name == "index.json":
            continue
            
        # Read the snippet file to get its ID
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                snippet_data = json.load(f)
                
            # Convert path to use forward slashes and be relative to root
            relative_path = str(json_file).replace("\\", "/")
            
            # Add to index
            index["snippets"].append({
                "path": relative_path,
                "id": snippet_data["id"]
            })
        except json.JSONDecodeError as e:
            print(f"Error reading {json_file}: {e}")
            continue
        except KeyError as e:
            print(f"Missing required field 'id' in {json_file}")
            continue
    
    # Sort snippets by path for consistency
    index["snippets"].sort(key=lambda x: x["path"])
    
    # Write the index file
    with open(snippets_dir / "index.json", 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)
        
    print(f"Generated index.json with {len(index['snippets'])} snippets")

if __name__ == "__main__":
    generate_index()