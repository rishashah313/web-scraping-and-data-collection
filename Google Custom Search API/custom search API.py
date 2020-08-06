from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyBi-gsqHZ4NQfmYnSKWX7ZDLs99Aug8V5Q"
my_cse_id = "000937740905453591135:kv5ru58tlau" #after creating a new id remove the site later!


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

####################################################################################
file = open("input list.txt", "r")
while file.readline():
	#Clean and Print the universiy name
	for universityName in file:
		cleanQuery = universityName.strip("\n")
		query = cleanQuery  
		print(query)

		#Construct the queries for the following searches
		uniSHC = query + " student health center"
		uniWC =  query + " wellness center"


		uniWebsite = google_search(query, my_api_key, my_cse_id, num=1, )
		uniSHC_web = google_search(uniSHC, my_api_key, my_cse_id, num=1, )

		#University website
		for result in uniWebsite:
			pprint.pprint(result.get('link', 'none'))

			#Student Health Center website
			for result in uniSHC_web:
				pprint.pprint(result.get('link', 'none'))

				#Construct the query for the site specific search
				specificSearch = "site:" + result.get('link', 'none')
				newQuery = specificSearch + ' "birth control"'
				try:
					siteSearch = google_search(newQuery, my_api_key, my_cse_id, num=5, )
					for result in siteSearch:
						pprint.pprint(result.get('link', 'none'))
				except: 
					print("''")


		
		print("\n")		
file.close()

