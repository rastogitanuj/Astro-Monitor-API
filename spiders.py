__author__ = 'tanuj'

import sys
sys.path.append('beautifulsoup4-4.2.1')
from bs4 import BeautifulSoup
import urllib2
import items
import traceback


class SwiftSpider(object):

    def __init__(self):
        self.url = "http://swift.gsfc.nasa.gov/results/transients/BAT_current.html"

    def parse(self):
        try:

            page = urllib2.urlopen(self.url)
            soup = BeautifulSoup(page.read())

            tables = soup.find_all('table')
            rows = tables[0].find_all('tr')[1:] # first row is a header row

            item_list = []

            for row in rows:

                item = items.SwiftItem()

                values = row.find_all('td')
                item.sourcename = values[1].text.strip()

                val = values[2].text.strip()
                if val == '-':
                    item.RA = None
                else:
                    item.RA	= float(val)

                val = values[3].text.strip()
                if val == '-':
                    pass
                else:
                    item.Dec = None
                    item.Dec	= float(val)

                val = values[4].text.strip()
                if val == '-':
                    item.alternatename = None
                else:
                    item.alternatename	= val

                val = values[5].text.strip()
                if val == '-':
                    item.sourcetype = None
                else:
                    item.sourcetype	= val

                val = values[6].text.strip()
                if val == '-':
                    item.Today = None
                else:
                    item.Today = float(val.split()[0])

                val = values[7].text.strip()
                if val == '-':
                    item.Yesterday = None
                else:
                    item.Yesterday = float(val.split()[0])

                val = values[8].text.strip()
                if val == '-':
                    item.Tenday = None
                else:
                    item.Tenday = float(val.split()[0])

                val = values[9].text.strip()
                if val == '-':
                    item.Mean = None
                else:
                    item.Mean = float(val)

                val = values[10].text.strip()
                if val == '-':
                    item.Peak = None
                else:
                    item.Peak = float(val)

                val = values[11].text.strip()
                if val == '-':
                    item.Days = None
                else:
                    item.Days = float(val)

                val = values[12].text.strip()
                if val == '-':
                    item.Last_Day = None
                else:
                    item.Last_Day = float(val.split()[0])

                item_list.append(item)

            return item_list

        except Exception as e:
            error_message = "Exception thrown: " + str(e) +"\n"+traceback.format_exc()
            print error_message
            raise e