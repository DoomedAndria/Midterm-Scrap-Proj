# 🏗️ Building Materials Scraper

This project is a simple web scraper designed to extract product information from an e-commerce website that sells building materials. It collects essential data such as product names, brands, prices, categories, descriptions, and image links.

## 📌 Features

- Scrapes structured product data
- Handles nested category structures with a custom data model
- Outputs clean and organized data
- Designed with future scalability in mind

## 📁 Project Structure



<pre><code>Midterm-Scrap-Proj/
├── main.py            
├── scraper/
│   ├── __init__.py     
│   ├── Scraper.py       
│   └── TsScraper.py       
│  
├── models/
│   ├── __init__.py     
│   ├── Category.py       
│   └── Product.py
├── utils/
│   ├── __init__.py     
│   ├── file_handler.py       
│   └── thread_pool_worker.py
├── data/
│   └── output.json     
├── README.md
└── requirements.txt 
</code></pre>


## 🛠️ Setup Instructions

1. **Clone the repository** or download the code.

2. **Install required packages** (preferably inside a virtual environment):

    ```bash
    pip install -r requirements.txt
    ```
3. **Run the scraper:**
    ```bash
    python main.py
    ```
   

<span style="color:orange">**Note:** As I’m not the best at writing content and  while the code is entirely mine, a big shoutout to GPT for helping me refine and structure the text for clarity and presentation.</span>