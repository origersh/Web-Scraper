import requests
from bs4 import BeautifulSoup
import pandas

PAGES = 5
ROWS = 25

lst = []

Name = 'span', {'class':'sr-hotel__name'}
Rank = 'div', {'class':'bui-review-score__badge'}
Location = 'a', {'class':'bui-link'}
Description = 'div', {'class':'room_link'}
Cancellation = 'sup', {'class':'sr_room_reinforcement e2e-free-cancellation'}
Price = 'div', {'class':'bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper'}

for i in range(0, PAGES):
    offset = i * ROWS
    request = requests.get("https://www.booking.com/searchresults.html?aid=304142&label=gen173rf-1FCAEoggI46AdIM1gDaGqIAQGYATG4ARfIARXYAQHoAQH4AQuIAgGYAiKoAgO4AtXy2vUFwAIB&sid=f4d231386cbfbddb9cb9964028c9273b&tmpl=searchresults&ac_click_type=b&ac_position=1&checkin_month=5&checkin_monthday=30&checkin_year=2020&checkout_month=5&checkout_monthday=31&checkout_year=2020&class_interval=1&dest_id=224&dest_type=country&dtdisc=0&from_sf=1&group_adults=1&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=country&room1=A&sb_price_type=total&sb_travel_purpose=business&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=aed563942a2700eb&ss=United%20States&ss_all=0&ss_raw=usa&ssb=empty&sshis=0&top_ufis=1&rows=25&offset={}".format(offset), headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    content = request.content

    soup = BeautifulSoup(content, "html.parser")

    all = soup.find_all('div', {'class':'sr_item sr_item_new sr_item_default sr_property_block sr_flex_layout'})

    for item in all:
        d = {}
        try: d['Name'] = item.find_all(Name[0], Name[1])[0].text.strip()
        except: d['Name'] = 'None'
        try: d['Rank'] = item.find_all(Rank[0], Rank[1])[0].text.strip()
        except: d['Rank'] = 'None'
        try: d['Location'] = item.find_all(Location[0], Location[1])[0].text.strip().split('\n')[0]
        except: d['Location'] = 'None'
        try: d['Description'] = item.find_all(Description[0], Description[1])[0].text.strip().split('\n')[0]
        except: d['Description'] = 'None'
        try: d['Cancellation'] = item.find_all(Cancellation[0], Cancellation[1])[0].text.strip()
        except: d['Cancellation'] = 'None'
        try: d['Price'] = item.find_all(Price[0], Price[1])[0].text.strip()
        except: d['Price'] = 'None'

        lst.append(d)

df = pandas.DataFrame(lst)
df.to_csv("Hotels.csv")