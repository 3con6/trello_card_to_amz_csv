# Trello to Amazon Bulk Upload Tool

## Introduction
This tool extracts images and information from Trello boards and generates an Excel file formatted for bulk product uploads to Amazon. It streamlines the process of managing product data, reducing manual effort and improving accuracy.

## Key Features
- Fetch product details and images from Trello.
- Generate an Excel file in Amazon's bulk upload format.
- Automate data collection to minimize errors.
- Support for multiple Trello boards and lists.

## System Requirements
- Python 3.8+
- Trello API Key and Token
- Pandas
- OpenPyXL

## Installation and Usage

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/trello-amazon-bulk-upload.git
   cd trello-amazon-bulk-upload
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up Trello API credentials in `data.py` file:
   ```sh
   TRELLO_API_KEY=your_api_key
   TRELLO_TOKEN=your_token
   BOARD_ID=your_board_id
   ```

### Running the Tool
```sh
python main.py
```


## Contribution
If you wish to contribute, please fork the repository, create a new branch, make changes, and submit a pull request.

## License
This project is released under the MIT License.

