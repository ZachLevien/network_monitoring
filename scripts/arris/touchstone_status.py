from bs4 import BeautifulSoup
from modem_status.base_modem import BaseModem


class TouchstoneStatus(BaseModem):
    def __init__(self, html) -> None:
        super()
        self.status = list()
        self.parameters = list()
        self.soup = BeautifulSoup(html)
    
    def parse_all_content(self):
        super().parse_all_content()

        main_body = self.soup.find("div", {"class": "main_body"}).p
        downstream = main_body.find("h4", string=" Downstream ").find_next("table")
        upstream = main_body.find("h4", string=" Upstream ").find_next("table")
        other = upstream.find_next_siblings("table")

        self.downstreams = self.parse_locks(self.parse_html_table(downstream))
        self.upstreams = self.parse_locks(self.parse_html_table(upstream))
