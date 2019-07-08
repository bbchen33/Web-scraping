from bs4 import BeautifulSoup
import requests

source = requests.get('https://university.graduateshotline.com/ubystate.html#AL').text

soup = BeautifulSoup(source, 'lxml')

dict = {}

paragraph = soup.find('p')

def scrape_school():
	for article in soup.find_all('p'):
		if article.b != None:
			dict[article.b.text] = ''
			
	ol = soup.find('ol')
	schools = ol.find_all('li')
	# list of all schools
	list_of_schools = []
	for s in schools:
		try:
			list_of_schools.append(s.a.text.strip())

		except AttributeError:
			print('some values are none type')
	dict['Alabama'] = list_of_schools[0:35]
	dict['Alaska'] = list_of_schools[35:42]
	dict['Arizona'] = list_of_schools[42:56]
	dict['Arkansas'] = list_of_schools[56:78]
	dict['California'] = list_of_schools[78:205]
	dict['Colorado'] = list_of_schools[205:230]
	dict['Connecticut'] = list_of_schools[230:253]
	#fix all states with university systems
	dict['Delaware'] = list_of_schools[253:258]
	dict['District of Columbia'] = list_of_schools[258:271]
	dict['Florida'] = list_of_schools[271:322]
	dict['Georgia'] = list_of_schools[322:372]	
	dict['Hawaii'] = list_of_schools[372:381]
	dict['Idaho'] = list_of_schools[381:388]
	dict['Illinois'] = list_of_schools[388:462]
	dict['Indiana'] = list_of_schools[462:522]
	dict['Iowa'] = list_of_schools[522:558]
	dict['Kansas'] = list_of_schools[558:585]
	dict['Kentucky'] = list_of_schools[585:617]
	dict['Louisiana'] = list_of_schools[617:644]
	dict['Maine'] = list_of_schools[644:663]
	dict['Maryland'] = list_of_schools[663:697]
	dict['Massachusetts'] = list_of_schools[697:773]
	dict['Michigan'] = list_of_schools[773:821]
	dict['Minnesota'] = list_of_schools[821:864]	
	dict['Mississippi'] = list_of_schools[864:881]
	dict['Missouri'] = list_of_schools[881:930]
	dict['Montana'] = list_of_schools[930:942]
	dict['Nebraska'] = list_of_schools[942:965]
	dict['Nevada'] = list_of_schools[965:969]
	dict['New Hampshire'] = list_of_schools[969:988]
	dict['New Jersey'] = list_of_schools[988:1018]
	dict['New Mexico'] = list_of_schools[1018:1027]
	dict['New York'] = list_of_schools[1027:1175]
	dict['North Carolina'] = list_of_schools[1175:1229]
	dict['North Dakota'] = list_of_schools[1229:1239]
	dict['Ohio'] = list_of_schools[1239:1311]
	dict['Oklahoma'] = list_of_schools[1311:1336]
	dict['Oregon'] = list_of_schools[1336:1363]
	dict['Pennsylvania'] = list_of_schools[1363:1492]
	dict['Rhode Island'] = list_of_schools[1492:1503]
	dict['South Carolina'] = list_of_schools[1503:1542]
	dict['South Dakota'] = list_of_schools[1542:1556]
	dict['Tennessee'] = list_of_schools[1556:1604]
	dict['Texas'] = list_of_schools[1604:1706]
	dict['Utah'] = list_of_schools[1706:1714]
	dict['Vermont'] = list_of_schools[1714:1733]
	dict['Virginia'] = list_of_schools[1733:1781]
	dict['Washington'] = list_of_schools[1781:1809]
	dict['West Virginia'] = list_of_schools[1809:1829]
	dict['Wisconsin'] = list_of_schools[1829:1866]
	dict['Wyoming'] = list_of_schools[1866:1867]
	dict['Guam'] = list_of_schools[1867:1868]
	dict['Puerto Rico'] = list_of_schools[1868:1894]
	dict['Virgin Islands'] = list_of_schools[1894:1895]
	return dict
  
  all_schools = scrape_school()
