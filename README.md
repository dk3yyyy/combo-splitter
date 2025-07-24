# 🔧 DK3Y Combo Splitter

A high-performance Python tool for efficiently splitting large text files into smaller, manageable parts. Perfect for processing large datasets, combo lists, wordlists, or any large text files that need to be divided.

## ✨ Features

- 🚀 **High Performance**: Optimized for very large files with efficient memory usage
- 📊 **Flexible Splitting**: Split by number of parts OR lines per file
- 🎨 **Colored Terminal Output**: Hacker-style green terminal interface
- 📁 **Smart File Management**: Automatic output directory creation and overwrite protection
- 🔄 **Progress Tracking**: Real-time progress updates for large files
- 💾 **Memory Efficient**: Handles files larger than available RAM
- 🛡️ **Error Handling**: Robust error handling and validation
- 🎯 **ASCII Art Banner**: Cool terminal banner with pyfiglet support

## 📋 Requirements

- Python 3.6 or higher
- Optional: `pyfiglet` for enhanced ASCII art banner

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/dk3yyyy/auto-split.git
cd auto-split
```

### Install Dependencies (Optional)

```bash
pip install pyfiglet
```

### Quick Start

```bash
python splitter.py
```

## 📖 Usage

### Interactive Mode

Simply run the script and follow the prompts:

```bash
python splitter.py
```

The script will guide you through:

1. **File Selection**: Enter the path to your text file
2. **Split Method**: Choose between splitting by number of parts or lines per file
3. **Configuration**: Set your preferred split parameters
4. **Output Directory**: Specify where to save the split files (optional)

### Example Workflow

```text
$ python splitter.py

 ____  _  _____ __   __   ____                  _             ____        _ _ _   _            
|  _ \| |/ /___|\ \ / /  / ___|___  _ __ ___   | |__   ___   / ___| _ __ | (_) |_| |_ ___ _ __ 
| | | | ' // _ | \ V /  | |   / _ \| '_ ` _ \  | '_ \ / _ \  \___ \| '_ \| | | __| __/ _ \ '__|
| |_| | . \ (_) | | |   | |__| (_) | | | | | | | |_) | (_) |  ___) | |_) | | | |_| ||  __/ |   
|____/|_|\_\___/  |_|    \____\___/|_| |_| |_| |_.__/ \___/  |____/| .__/|_|_|\__|\__\___|_|   
                                                                   |_|                         

Enter the path to the text file to split: large_combo_list.txt
How would you like to split the file?
1. By number of parts
2. By lines per file
Enter 1 or 2: 2
Enter the number of lines per file: 1000000
Enter output directory (leave blank for same as input file): ./output

Created: ./output/large_combo_list_part1.txt (1000000 lines)
Created: ./output/large_combo_list_part2.txt (1000000 lines)
Created: ./output/large_combo_list_part3.txt (500000 lines)

Summary: 2500000 lines processed, 3 file(s) created.
```

## 🔧 Advanced Features

### Splitting Options

#### 1. Split by Number of Parts

```text
Choose option 1, then specify how many files you want.
Example: Split a 1,000,000 line file into 4 parts = 250,000 lines each
```

#### 2. Split by Lines per File

```text
Choose option 2, then specify lines per output file.
Example: 100,000 lines per file from any size input
```

### File Handling

- **Automatic Extension Preservation**: Output files maintain the same extension as input
- **Overwrite Protection**: Prompts before overwriting existing files
- **Empty File Cleanup**: Automatically removes empty output files
- **Large File Support**: Efficiently processes files of any size

### Output Naming Convention

```text
Input:  myfile.txt
Output: myfile_part1.txt, myfile_part2.txt, myfile_part3.txt...
```

## 📊 Performance

- **Memory Usage**: Constant memory usage regardless of file size
- **Processing Speed**: ~1,000,000 lines per minute (varies by system)
- **File Size Support**: No practical limit on input file size
- **Progress Updates**: Real-time progress for files over 1M lines

## 🛠️ Technical Details

### Architecture

- **Streaming Processing**: Reads files line-by-line to minimize memory usage
- **Buffered I/O**: Uses 1MB write buffers for optimal performance
- **Error Recovery**: Graceful handling of interruptions and errors

### Supported File Types

- Plain text files (.txt)
- CSV files (.csv)
- Log files (.log)
- Any text-based file format

## 🐛 Troubleshooting

### Common Issues

#### File Not Found Error

```text
Make sure the file path is correct and the file exists
Use absolute paths if having issues with relative paths
```

#### Permission Denied

```text
Ensure you have read permissions for the input file
Ensure you have write permissions for the output directory
```

#### Memory Issues

```text
The tool is designed to handle large files efficiently
If you encounter memory issues, try closing other applications
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📈 Changelog

### v1.0.0

- Initial release
- Interactive file splitting
- Support for splitting by parts or lines
- Colored terminal interface
- Progress tracking for large files
- Comprehensive error handling

Made with ❤️ by [dk3yyyy]
