import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url='https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population'):
        self.__url = url
        self.__data_rows = []
        self.countries = {}
        self.__fetch_data()
        self.__extract_countries_data()
        self.__calculate_population_percentage()

    def __fetch_data(self):
        response = requests.get(self.__url)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table', {'class': 'wikitable'})
        self.__data_rows = table.find_all('tr')[2:]  # Starting from 2 to skip the line about European Union

    def __extract_countries_data(self):
        for row in self.__data_rows:
            if not row.find('td'):
                continue

            row_text = ' | '.join(cell.text.strip() for cell in row.find_all(['th', 'td']))
            columns = row.find_all('td')
            # Extract country name
            country_name = columns[1].text.strip()
            # Extract population value
            population_text = columns[2].text.strip().replace(',', '')
            try:
                official_figure = int(population_text)
            except ValueError:
                print(f"Skipping row due to invalid population value: {row_text}")
                continue

            self.countries[country_name] = {
                'country_population': official_figure
            }

    def __calculate_population_percentage(self):
        total_country_population = sum(country_data['country_population'] for country_data in self.countries.values())
        for country_name, country_data in self.countries.items():
            country_population_percentage = (country_data['country_population'] / total_country_population) * 100
            country_data['country_population_percentage'] = round(country_population_percentage, 1)

    def print_countries_data(self):
        for country, info in self.countries.items():
            print(f"{country} -> {info}")


if __name__ == "__main__":
    eu_population = Scraper()
    eu_population.print_countries_data()