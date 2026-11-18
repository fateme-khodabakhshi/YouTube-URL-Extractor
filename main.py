
import re

html = input()

pattern = r'''src\s*=\s*["']https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]+)'''

match = re.search(pattern, html)

if match:
    print("https://youtu.be/" + match.group(1))
else:
    print("None")
