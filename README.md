# 🔧 DK3Y Combo Splitter

A high-performance Python tool for splitting large text files into smaller parts. Perfect for combo lists, wordlists, and large datasets.

## ✨ Features

- 🚀 **High Performance**: Memory-efficient processing of large files
- 📊 **Flexible Splitting**: Split by number of parts OR lines per file
- 🎨 **Colored Terminal**: Hacker-style green interface with ASCII banner
- 📁 **Smart Management**: Auto output directory creation and overwrite protection
- 🔄 **Progress Tracking**: Real-time updates for large files

## 📋 Requirements

- Python 3.6+
- Optional: `pyfiglet` for ASCII art banner

## 🚀 Installation & Usage

```bash
git clone https://github.com/dk3yyyy/auto-split.git
cd auto-split
pip install pyfiglet  # optional
python splitter.py
```

## 📖 How It Works

1. **File Selection**: Enter path to your text file
2. **Split Method**: Choose by number of parts or lines per file
3. **Output**: Files saved as `filename_part1.txt`, `filename_part2.txt`, etc.

## Example

```text
$ python splitter.py

Enter the path to the text file to split: combo_list.txt
How would you like to split the file?
1. By number of parts
2. By lines per file
Enter 1 or 2: 2
Enter the number of lines per file: 1000000

Created: combo_list_part1.txt (1000000 lines)
Created: combo_list_part2.txt (500000 lines)

Summary: 1500000 lines processed, 2 file(s) created.
```

## 📊 Performance

- **Memory**: Constant usage regardless of file size
- **Speed**: ~1M lines per minute
- **File Size**: No practical limit

## �‍💻 Developer

**Built by:** [dk3yyyy](https://github.com/dk3yyyy)

**Tech Stack:** Python, python-telegram-bot, aiohttp, asyncio

## 📄 License

MIT License - Free to use and modify

## ⭐ Support

If you find this useful:

- ⭐ Star the repository
- 🍴 Fork and contribute

## ☕️ Buy Me Coffee

If you'd like to support the project, you can send tips to any of the following addresses:

- **SOL:** `CZXTNF5k7BWTW8fR7KGNjXTmyUedRgMMPXmi8jWKPfeK`
- **ETH:** `0x6327E5374d244a11cf1d68f189E55f27e3EEe043`
- **BTC:** `bc1qtwe8mxt8nu9guquh0s9g3ap9uuftd057qfp57s`
- **USDT (Tron):** `TJMSyxu2J8zvMCcv6buN7zJNkmWn1n9qMQ`
