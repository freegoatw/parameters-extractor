try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
import csv
import re;
import itertools;

#Import des urls

queries = [];
merged = [];

pattern = r'=|&';

with open("urls.txt", 'r') as f:
	corpus = f.read().split(",");
	print(corpus);
	for entry in corpus:
		o = urlparse(entry);
		q = o.query;
		m = (re.split(pattern, q));
		queries.append(m);
merged = list(itertools.chain(*queries))

# csv export
with open('urls.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for row in merged:
		writer.writerow([row])