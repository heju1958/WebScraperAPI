from requests_html import HTMLSession
from operator import itemgetter


class Scraper:
    def web_scraper_data(self, tag):
        url = f"https://webscraper.io/test-sites/e-commerce/allinone/computers/{tag}"
        session = HTMLSession()
        request = session.get(url)

        data_list = []

        item = request.html.find("div.col-sm-4.col-lg-4.col-md-4")

        for i in item:
            product = {
                "img": i.find("img.img-responsive", first=True).text.strip(),
                "title": i.find("a.title", first=True).text.strip(),
                "price": i.find("h4.pull-right.price", first=True).text.strip(),
                "description": i.find("p.description", first=True).text.strip(),
                "reviews": i.find("p.pull-right", first=True).text.strip(),
            }

            data_list.append(product)

            data_filter = [
                laptops
                for laptops in data_list
                if laptops["title"].__contains__("Lenovo")
                and sorted(laptops, key=itemgetter(0))
            ]

        return data_filter
