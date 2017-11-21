# import libraries
import urllib2
import json
from bs4 import BeautifulSoup



# specify the url
quote_page = 'https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%221182748%22%5D&keywords=apega&origin=GLOBAL_SEARCH_HEADER'


opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'bcookie="v=2&ce4fe073-0436-4071-828a-ffb5bda680fe"'))
opener.addheaders.append(('Cookie', '_ga=GA1.2.358098630.1511215779'))
opener.addheaders.append(('Cookie', 'RT=s=1511216311522&r=https%3A%2F%2Fwww.linkedin.com%2F'))
opener.addheaders.append(('Cookie', 'sl="v=1&dowlo"'))
opener.addheaders.append(('Cookie', 'lang="v=2&lang=en-us"'))
opener.addheaders.append(('Cookie', 'liap=true'))
opener.addheaders.append(('Cookie', 'JSESSIONID="ajax:4849649980279285355"'))
opener.addheaders.append(('Cookie', 'mst="v=1&dowlo"'))
opener.addheaders.append(('Cookie', 'li_at=AQEDAQCUwtcC_6xIAAABX9uD5BIAAAFf_5BoElYAN2ZrWG6Hm39MVZfRrpyxNK9T1cj2ws5444ISzdC0lk9Y_bAUBowcgoYSHNo1JCiQMIqfYPH2Bv1_3-gRhXzX51pxIGyCW7cGz5bSVZp-hlhSqzf4'))
opener.addheaders.append(('Cookie', 'lidc="b=OB07:g=642:u=346:i=1511216376:t=1511302776:s=AQFKAzYadBr44J4gysCyXXjP4COQQ06Q"'))


page = opener.open(quote_page)

# parse the html using beautiful soap and store in variable soup
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('span', attrs={'class': 'name actor-name'})
print name_box

# name = name_box.text.strip() # strip() is used to remove starting and trailing
# print name
