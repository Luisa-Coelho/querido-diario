from datetime import date

from gazette.spiders.base.doem import DoemGazetteSpider


class BaCaetiteSpider(DoemGazetteSpider):
    TERRITORY_ID = "2905206"
    name = "ba_caetite"
    start_date = date(2021, 4, 27)
    state_city_url_part = "ba/caetite"
