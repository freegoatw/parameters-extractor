#This script lists the most used parameters in a url list
from urllib.parse import urlparse
from pathlib import Path
from detect_delimiter import detect

scriptError = False

corpuslist = [];

workingDirectory = str(Path(__file__).parent.absolute())
workingDirectory = workingDirectory[-20:]
filePath = str(Path().absolute())
filePath = filePath[-20:]

if workingDirectory != filePath : print("attention ton terminal n’est pas au bon endroit, le working directory est : " + workingDirectory +"\n et le filepath est : " + filePath)
else : print("zeee partii")

#Open the url file and splits it for each ",""
try :
    with open("urls.txt", 'r') as f:
        corpus = f.read().split("\n");
except :
    print("il y a un problème avec le fichier des urls")
    scriptError = True
  
query_counter = {};  

#Main function of the script. get the parameters.
def get_query(url):
    url = url
    query = urlparse(url).query;
    query = query.split("&");
    query = [x.split("=")[0] for x in query];
    query = list(set(query));
    return query;

#Check if there is a problem before
if scriptError == False :

    #count the number of times a parameter is used.
    for url in corpus:
        query = get_query(url);
        corpuslist.append(query);
        for q in query:
            if q in query_counter:
                query_counter[q] += 1;
            else:
                query_counter[q] = 1;

    # csv export one query per line.
    with open("queries.csv", 'w') as f:
        for query in corpuslist:
            for q in query:
                f.write(q + "\n");

    print("\n\n\n##################################### \n   ding ding - votre csv est prêt \n#####################################\n\n\n")

else : print("\n\n\n_.~\"~._.~\"~._.~\"~._.~\"~._ Débug nécéssaire frr_.~\"~._.~\"~._.~\"~._.~\"~._\n\n\n")