class BaseModem():
    def __init__(self) -> None:
        self.url = str()
        self.upstreams = list()
        self.downstreams = list()

    def parse_all_content(self):
        pass

    def parse_locks(self, lock_data):
        '''
        parse_lock_data reads ISP CMTS upstream and downstream lock data at time of status page refresh.
        return json
        '''
        json_data = list()

        if len(lock_data) > 0:
            # get columns from first row
            columns = lock_data[0]

            for lock in lock_data[1:]:
                new_line = dict()

                for ci, column in enumerate(columns[1:]):
                    #  no column name exists for the first item
                    if ci == 0:
                        new_line["Connection"] = lock[0]
                    else:
                        # match column names with the remaining data
                        new_line[column] = lock[ci]

                json_data.append(new_line)

        return json_data
    
    def parse_html_table(self, html):
        '''
        parse_html_table takes a raw html string containing a <table>, and parses the cell data in a python list
        Returns list()
        '''
        data = list()

        # https://stackoverflow.com/a/18544794
        data = [[cell.text for cell in row("td")]
                            for row in html("tr")]