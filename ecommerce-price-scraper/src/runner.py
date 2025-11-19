thonpython
import json
import logging
from pathlib import Path
from spiders.ecommerce_spider import EcommerceSpider
from outputs.exporter import Exporter

logging.basicConfig(level=logging.INFO)

def load_urls(input_file: str):
 path = Path(input_file)
 if not path.exists():
 logging.error(f"Input file not found: {input_file}")
 return []

 with open(path, "r", encoding="utf-8") as f:
 return [line.strip() for line in f.readlines() if line.strip()]

def main():
 urls = load_urls(str(Path(__file__).parent.parent / "data" / "inputs.sample.txt"))
 if not urls:
 logging.error("No URLs to scrape.")
 return

 spider = EcommerceSpider()
 results = []

 for url in urls:
 try:
 data = spider.scrape(url)
 if data:
 results.append(data)
 except Exception as e:
 logging.error(f"Error scraping {url}: {e}")

 exporter = Exporter()
 output_path = Path(__file__).parent.parent / "data" / "sample.json"
 exporter.to_json(results, output_path)
 logging.info(f"Scraping completed. Output saved to {output_path}")

if __name__ == "__main__":
 main()