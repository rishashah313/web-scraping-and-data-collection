import pandas as pd
import csv
import sys

def read_text_file(textfile):
    text_file = open(textfile, "r")
    read_vocab = [line.strip("\n") for line in text_file]
    return read_vocab

term_vocab = read_text_file("term_vocab.txt")
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found")
    
header=['Website', 'pages with vocabulary']
df=pd.DataFrame(columns=header)

file = open("input file.txt", "r")
all_destination_urls = []
unique_destination_urls = []
final = []
i=0

x = 1
next1 = 0


for line in file:                   
            
                        url = line.strip("\n")
                        print(i)
                        specificSearch = "site:" + url
                        for t in term_vocab:
                            newQuery = specificSearch + " \""+t+"\""
                            print(newQuery)

                    
                            #Use the site Search of the Domain 
                            for newSearch in search(newQuery, tld="com", num=10, stop=10, pause=2):
                                all_destination_urls.append(newSearch)
                                #print(newSearch.text)
                                print(all_destination_urls)
                        
                        unique_destination_urls = [url for url in all_destination_urls if url not in unique_destination_urls]
                                
                        df.loc[i] = [url,unique_destination_urls]
                        df.to_csv('result.csv')
                        i = i + 1
                        all_destination_urls = []
                        unique_destination_urls = []
file.close()
