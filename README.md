# Tools

A collection of utility tools and scripts for data processing, automation, and content management.

## Features

- **YouTube Handle Extractor**: Extract, categorize, and organize YouTube handles from subscription pages
- Intelligent duplicate removal and alphabetical sorting
- Content-based categorization without external APIs
- Clean, modular code with full type annotations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Dawgsrlife/tools.git
cd tools
```

2. Install required dependencies:
```bash
pip install textblob
```

## Usage

### YouTube Handle Extractor

Extract and categorize YouTube handles from a text file containing subscription page data.

```bash
python extract_youtube_handles.py
```

**Input**: Place your YouTube subscription page text in `data/sample_input.txt`
**Output**: Categorized handles will be written to `data/handles_output.txt`

#### Features:
- **Duplicate Removal**: Automatically removes duplicate handles
- **Alphabetical Sorting**: Sorts handles within each category
- **Smart Categorization**: Groups handles by content type:
  - Music (piano, bands, artists)
  - Cars (automotive, mechanics)
  - Tech (programming, software)
  - News (journalism, reporting)
  - Gaming (games, esports)
  - Food (cooking, recipes)
  - Finance (investing, trading)
  - Travel (vlogs, adventure)
  - Other (uncategorized)

#### Output Format:
Handles are grouped by category without headers, creating a seamless, organized list:

```
@musicchannel1
@musicchannel2
@techchannel1
@techchannel2
@gamingchannel1
...
```

## Project Structure

```
tools/
├── data/
│   ├── sample_input.txt      # Input file for YouTube subscription data
│   └── handles_output.txt    # Output file with categorized handles
├── extract_youtube_handles.py # Main extraction script
└── README.md                 # This file
```

## Development

### Code Standards
- Full type annotations following UTM UofT standards
- Comprehensive documentation and comments
- Modular function design
- Error handling and edge case consideration

### Adding New Tools
1. Create your script in the root directory
2. Add type annotations and docstrings
3. Update this README with usage instructions
4. Follow the existing code style and structure

## Credits

- **alexanderthemango** - Original YouTube handle extractor implementation
- **Date**: 6:10PM July 4th, 2025

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with proper documentation
4. Submit a pull request

## Support

For issues or questions, please open an issue on GitHub or contact the maintainers. 