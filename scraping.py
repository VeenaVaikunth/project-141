from bs4 import BeautifulSoup

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

star_data = []

def scrape():
    headers = ['name', 'distance', 'mass', 'radius']
    star_data = []

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...')

    for i in range(0, 490):
        soup = BeautifulSoup()
        for ul_tag in soup.find_all('ul', attrs={'class', 'exoplanet'}):
            li_tags = ul_tag.find_all('li')
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append('')
            star_data.append(temp_list)
    print(star_data[1])

headers = ['name', 'distance', 'mass', 'radius']