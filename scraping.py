from urllib.request import urlopen
import re

url = "https://www.tudublin.ie/study/undergraduate/courses/computer-science-tu856/"
page = urlopen(url)
html = page.read().decode()


title_start = html.find("<title>") + 7;
title_end = html.find("</title");
title = html[title_start:title_end]

search_term = "<h5>Number of Places</h5><p>"
extract = html[html.find(search_term) + len(search_term):]
places = extract[:extract.find("</p>")]

print("Programme Title:", title)
print("Places:", places)


title_pattern = "<title.*?>.*?</title>"
title = re.search(title_pattern, html, re.IGNORECASE).group()
title = re.sub("<.*?>", "", title)

places = re.findall(r"<h5>Number of Places</h5>\s*<p>(?P<places>.+\s*)</p>", html)[0].strip()
tu_code = re.findall(r"<h5>TU Code</h5>\s*<p>(?P<code>.+\s*)</p>", html)[0].strip()
level = re.findall(r"<h5>Level</h5>\s*<p>(?P<code>.+\s*)</p>", html)[0].strip()
award = re.findall(r"<h5>Award</h5>\s*<p>(?P<code>.+\s*)</p>", html)[0].strip()
duration = re.findall(r"<h5>Duration</h5>\s*<p>(?P<code>.+\s*)</p>", html)[0].strip()

print("Programme Title:", title)
print("Places:", places)
print("CAO Code:", tu_code)
print("Level:", level)
print("Award:", award)
print("Duration:", duration)


