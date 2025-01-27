# DNA/RNA Sequence Classifier

This script classifies an input sequence as DNA, RNA, or neither. Additionally, it can search for a specified motif within the sequence.

## Requirements
- Python 3
- Standard libraries: `sys`, `re`, and `argparse` (included in Python)

## Usage

Run the script from the command line with the following options:

### Required Argument:
- `-s` or `--seq`: The input sequence to be classified (e.g., `ACGT`, `AUCG`).

### Optional Argument:
- `-m` or `--motif`: A motif to search for within the sequence (e.g., `CGT`).

### Example:
python script.py -s ACGTACGT
