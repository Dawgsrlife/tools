"""
extract_youtube_handles.py

Extracts YouTube handles from a text file, removes duplicates, sorts them alphabetically, and groups them by category using simple keyword-based logic. The output is written to a file, grouped by category (without headers), so the grouping appears seamless.

Credits: alexanderthemango
Date: 6:10PM July 4th, 2025
"""

import re
from collections import defaultdict
from typing import Set, Dict, List, DefaultDict
from textblob import TextBlob

input_path: str = 'data/sample_input.txt'
output_path: str = 'data/handles_output.txt'

def extract_handles(filepath: str) -> Set[str]:
    """
    Extract unique YouTube handles from the given file.
    Args:
        filepath: Path to the input text file.
    Returns:
        A set of unique YouTube handles (e.g., @example).
    """
    handles: Set[str] = set()
    with open(filepath, 'r', encoding='utf-8') as infile:
        for line in infile:
            match = re.match(r'(@[\w\.]+)', line.strip())
            if match:
                handles.add(match.group(1))
    return handles

def build_handle_descriptions(filepath: str) -> Dict[str, str]:
    """
    Build a mapping from each handle to its description (the line following the handle).
    Args:
        filepath: Path to the input text file.
    Returns:
        Dictionary mapping handle to description string.
    """
    handle_desc: Dict[str, str] = {}
    with open(filepath, 'r', encoding='utf-8') as infile:
        lines: List[str] = infile.readlines()
        for i, line in enumerate(lines):
            match = re.match(r'(@[\w\.]+)', line.strip())
            if match:
                handle: str = match.group(1)
                desc: str = ''
                if i + 1 < len(lines):
                    next_line: str = lines[i + 1].strip()
                    if not next_line.startswith('@'):
                        desc = next_line
                handle_desc[handle] = desc
    return handle_desc

def categorize_handles(handles: Set[str], handle_desc: Dict[str, str]) -> DefaultDict[str, List[str]]:
    """
    Categorize handles using simple keyword-based logic on their descriptions.
    Args:
        handles: Set of unique handles.
        handle_desc: Mapping from handle to description.
    Returns:
        DefaultDict mapping category name to list of handles.
    """
    categories: DefaultDict[str, List[str]] = defaultdict(list)
    for handle in handles:
        desc: str = handle_desc.get(handle, '').lower()
        if any(word in desc for word in ['music', 'song', 'piano', 'band', 'guitar', 'singer', 'artist']):
            categories['music'].append(handle)
        elif any(word in desc for word in ['car', 'auto', 'drive', 'bmw', 'mechanic', 'garage']):
            categories['cars'].append(handle)
        elif any(word in desc for word in ['code', 'program', 'software', 'developer', 'tech', 'algorithm', 'python']):
            categories['tech'].append(handle)
        elif any(word in desc for word in ['news', 'cnn', 'cbc', 'report', 'journalist']):
            categories['news'].append(handle)
        elif any(word in desc for word in ['game', 'gamer', 'gaming', 'minecraft', 'esports']):
            categories['gaming'].append(handle)
        elif any(word in desc for word in ['food', 'cook', 'chef', 'kitchen', 'recipe']):
            categories['food'].append(handle)
        elif any(word in desc for word in ['finance', 'money', 'invest', 'stock', 'trading']):
            categories['finance'].append(handle)
        elif any(word in desc for word in ['travel', 'vlog', 'adventure', 'explore']):
            categories['travel'].append(handle)
        else:
            categories['other'].append(handle)
    # Sort handles alphabetically within each category (case-insensitive)
    for cat in categories:
        categories[cat] = sorted(set(categories[cat]), key=lambda x: x.lower())
    return categories

def write_grouped_handles(categories: DefaultDict[str, List[str]], output_filepath: str) -> None:
    """
    Write the grouped, sorted handles to the output file (no category headers).
    Args:
        categories: DefaultDict mapping category name to list of handles.
        output_filepath: Path to the output text file.
    Returns:
        None
    """
    with open(output_filepath, 'w', encoding='utf-8') as outfile:
        for cat in sorted(categories.keys()):
            for handle in categories[cat]:
                outfile.write(handle + '\n')

def main() -> None:
    """
    Main function to extract, categorize, and write YouTube handles.
    Returns:
        None
    """
    handles: Set[str] = extract_handles(input_path)
    handle_desc: Dict[str, str] = build_handle_descriptions(input_path)
    categories: DefaultDict[str, List[str]] = categorize_handles(handles, handle_desc)
    write_grouped_handles(categories, output_path)

if __name__ == '__main__':
    main() 