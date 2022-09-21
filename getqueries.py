#list the most used parameters in a url list
from urllib.parse import urlparse
from pprint import pprint
import csv

corpuslist = [];

with open("urls.txt", 'r') as f:
    corpus = f.read().split(",");
  
query_counter = {};  

def get_query(url):
    url = url
    query = urlparse(url).query;
    query = query.split("&");
    query = [x.split("=")[0] for x in query];
    query = list(set(query));
    return query;

#count the number of times a query is used           
for url in corpus:
    query = get_query(url);
    corpuslist.append(query);
    for q in query:
        if q in query_counter:
            query_counter[q] += 1;
        else:
            query_counter[q] = 1;


pprint(corpuslist);

# csv export one query per line
with open("queries.csv", 'w') as f:
    for query in corpuslist:
        for q in query:
            f.write(q + "\n");