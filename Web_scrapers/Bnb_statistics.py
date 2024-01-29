import requests
from bs4 import BeautifulSoup
import csv


class Scraper:
    def __init__(self, url='https://bnb.bg/Statistics/StInterbankForexMarket/index.htm'):
        self.url = url
        self.data_rows = []

    def scrape_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')

            table = soup.find_all('table')[1]

            if table:
                rows = table.find_all('tr')[2:-2]  # removed the unnecessary lines
                self.data_rows = sorted(rows, key=lambda row: float(row.find_all('td')[7].text.replace(' ', '')),
                                        reverse=True)
            else:
                print("Table not found on the webpage.")
        else:
            print(f"Failed to retrieve content. Status Code: {response.status_code}")

    def print_data_rows(self):
        for row in self.data_rows:
            row_text = ' | '.join(cell.text.strip() for cell in row.find_all(['th', 'td']))
            print(row_text)

    def save_sorted_to_csv(self):
        headers = [header.text.strip() for header in self.data_rows[0].find_all('th')]
        # Extracting the data from each row
        data = [[cell.text.strip() for cell in row.find_all(['th', 'td'])] for row in self.data_rows]
        # Writing to CSV
        with open('sorted_forex_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(headers)
            csv_writer.writerows(data)


scraper = Scraper()
scraper.scrape_data()
scraper.print_data_rows()
scraper.save_sorted_to_csv()
