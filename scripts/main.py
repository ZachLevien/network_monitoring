from urllib import request
from modem_status.arris import touchstone_status


url = "http://192.168.100.1/cgi-bin/status_cgi"
req = request.urlopen(url)
html = (req.read()).decode('utf8')

status = touchstone_status.TouchstoneStatus(html)
status.parse_all_content()

print('test')
