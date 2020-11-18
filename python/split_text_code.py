# Split body in post into text and code block(s)

import re

# Remove HTML tags in text
def remove_tags(text):
	pat = re.compile(r'<.*?>')
	return pat.sub('', text)

# Input: the body of a post as a string
# Output: (a list of code blocks as strings, 
#		   the body with code blocks removed as a string)
def split(body):
	pat = re.compile(r"<code>(.+?)<\/code>", flags=re.DOTALL)
	codes = pat.findall(body) # extraction
	text = remove_tags(pat.sub('', body)) # removal
	return text, codes

def main():
	example = "<p>I want to write some automation to website. Simply filling in forms and simulating clicks on elements. But for some elements JavaScript function click() doesn't work. For example it is on this page: <a href=\"http://www1.plus.pl/bsm/\" rel=\"noreferrer\">http://www1.plus.pl/bsm/</a> If I do click() on \"Wy\u015blij\" button, nothing happens. It is my command:</p>\n\n<pre><code>document.getElementsByClassName('tab-button')[0].click()\n</code></pre>\n\n<p>What is wrong? Why on other elements this function works?</p>\n"
	text, code = split(example)
	print(text)
	print(code)

if __name__ == '__main__':
	main()