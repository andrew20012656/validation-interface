# Project Name

[Short description of your project]

## Table of Contents
1. [Installation](#installation)
2. [Project Structure](#project-structure)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)


## Installation

To install the dependencies required for this project, run the following command:

```bash
pip install -r requirements.txt
```

Make sure you have Python and pip installed on your system.

## Project Structure

The project follows the following directory structure:
```bash
├── assets
│   ├── css
│   │   ├── **/*.css
│   ├── favicon.ico
│   ├── images
├── data
│   ├── participant1
│   │   ├── google-takeout
│   │   │   ├── Semantic-Location-History
│   │   ├── **
├── README.md
├── app.py
├── common_utils.py
├── data_validator.py
├── location_anonymizer.py
├── requirements.txt
└── .gitignore
```

## Usage

To start the validator app, you can run the following command in Terminal:

```bash
python app.py ./data/participant1/google-takeout/Semantic-Location-History ./data/output/participant1
```

Then, a localhost url will be shown in Terminal (e.g. http://127.0.0.1:8050/). Open the url in your preferred browser. 

If you are interested, you can find the anonymized data saved under `./data/output/participant1` directory.

