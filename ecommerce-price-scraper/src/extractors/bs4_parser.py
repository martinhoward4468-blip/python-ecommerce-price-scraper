thonpython
class BS4Parser:
 def extract_text(self, soup, selectors):
 for sel in selectors:
 el = soup.select_one(sel) if sel.startswith(".") or sel.startswith("#") else soup.find(sel)
 if el and el.text.strip():
 return el.text.strip()
 return None