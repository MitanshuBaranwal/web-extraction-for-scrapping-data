

# Web Extraction to Word Document

This Django application extracts text content from a given URL, processes its text, and saves it as a Word document. It uses various libraries for web scraping, text processing, and document generation.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)


## Features

- Extracts text content from a provided URL.
- Handles basic text formatting such as bold and italic.
- Converts HTML content to Markdown format.
- Removes unnecessary URLs from the content.
- Generates a Word document with the extracted and formatted text.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/MitanshuBaranwal/web_extraction.git
   cd web_extraction
   ```
   
2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```


## Usage

1. Start the Django development server:
   ```sh
   python manage.py runserver
   ```

2. Access the API endpoint using a tool like curl or Postman.

      Example using curl:
   
      ```sh
      curl --location 'http://127.0.0.1:8000/extract_text' \
      --header 'Content-Type: application/x-www-form-urlencoded' \
      --data-urlencode 'url=https://www.wikiwand.com/en/Artificial_intelligence'
   ```

3. The extracted text will be processed and saved as a Word document named extracted_text.docx.


## Contact
For any enquiries please contact me at :
      
      mitanshubaranwal70232@gmail.com
      
