import re

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class BaCamacariSpider(BaseGazetteSpider):
    name = "ba_camacari"
    TERRITORY_ID = "2905206"
    start_date = datetime.date(2014, 11, 28)
    allowed_domains = ["camacari.ba.gov.br"]
    start_urls = ["https://www.camacari.ba.gov.br/arquivos/diario-oficial/"]

    def parse(self, response):
        editions = response.xpath("/html/body/section/div[2]/div[1]/div/div")

        for edition in editions:
            document_href = edition.xpath(
                "//div[@class='col-sm 12 col-md-10']//p[div[@class='h5 mb-40']/@href"
            ).get()
            title = edition.xpath(
                "//div[@class='col-sm 12 col-md-10']//p[div[@class='h5 mb-40']/text()"
            )
            gazette_date = re.search(r"\d{2}/\d{2}/\d{4}", title)
            edition_number = re.search(r"(?<=DIÁRIO OFICIAL N° )\S+", title)
            is_extra_edition = "extra" in title

            yield Gazette(
                date=gazette_date,
                edition_number=edition_number,
                file_urls=[response.urljoin(document_href)],
                is_extra_edition=is_extra_edition,
                power="executive",
            )
