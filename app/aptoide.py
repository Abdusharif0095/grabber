from .spider import Spider
from bs4 import BeautifulSoup


class Aptoide:

    async def get_info(self, soup: BeautifulSoup) -> dict:
        div = soup.find('div', class_='app-view__AppDetailsContainer-sc-oiuh9w-4 gLnJns')
        spans = div.find_all('span')

        data = {
            "App's name": "",
            "Release date": "",
            "App's description": "",
            "Number of downloads": "",
            "App's size": "",
            "App's version": "",
        }

        name = div.find('div', class_='app-informations__LongNameContainer-sc-1wisk8p-13 fYZnxb').find('h1').text
        data["App's name"] = name
        data["Release date"] = spans[-2].text[1:-1]

        spans = div.find_all('span', class_="app-informations__AppSpan-sc-1wisk8p-6 app-informations__DetailsMainSpan-sc-1wisk8p-16 eBKTbc fNvkUS")
        data["Number of downloads"] = spans[0].text
        data["App's size"] = spans[1].text
        spans = div.find_all('span')
        data["App's version"] = spans[-3].text

        desc_div_p = soup.find('div', class_='details__DescriptionParagraphs-sc-rnz8ql-10 gJcZDT').find_all('p')

        for p in desc_div_p:
            data["App's description"] += p.get_text()

        return data

    async def get(self, url: str) -> tuple:
        result = {}
        spider = Spider()
        response, status = await spider.get_url(url, 'aptoide.com')
        if response:
            soup = BeautifulSoup(response, 'html.parser')
            result = await self.get_info(soup)

        return result, status
