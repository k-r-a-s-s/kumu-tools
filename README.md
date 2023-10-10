# Kumu Network Mapping Tools Repository

## Description

This repository focuses on providing tools and scripts for working with Kumu, a platform for network mapping. The initial script in this repository is designed to transform a Kumu Excel file into a merged format. This can be useful for an import into platforms like GreenRope or Airtable, or for more general data analysis. In the future, we aim to add more utility scripts and tools related to Kumu.

## Table of Contents

1. [Description](#description)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Roadmap](#roadmap)
6. [Contributing](#contributing)
7. [License](#license)
8. [Acknowledgments](#acknowledgments)

## Requirements

- Python 3.x
- pandas library

## Installation

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/username/kumu-tools.git
    ```
2. Navigate to the directory and install the required Python packages.
    ```bash
    cd kumu-tools
    pip install pandas
    ```

## Usage

### Kumu to Merged Format

This script (`kumu_transform.py`) takes a Kumu Excel file and merges it in such a way that each element has a list of connections. The following options are available within the script:

- `file_path`: The path to the input Kumu Excel file.
- `airtable_output`: A Boolean to specify the output format. If `True`, outputs suitable for Airtable import.
- `comma_replace_string`: A string to replace commas in the data. Only used when `airtable_output` is `True`.

#### Running the Script

Run the script using Python:
```bash
python your_script_name.py
```

The merged output will be saved as a CSV file named `filename-merged.csv`.

## Roadmap

- Extend the script to provide two-way transformation capabilities.
- Integrate directly with GreenRope and Airtable through their respective APIs.
- Develop additional Kumu-related utility scripts.

## Contributing

If you're interested in contributing, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
