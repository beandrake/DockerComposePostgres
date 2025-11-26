import requests
import json
import datetime

# datafile documentation at
# https://forums.warframe.com/topic/1077490-riven-trading-toolbuilders-phase-1/
SOURCE_URL = r"https://www-static.warframe.com/repos/weeklyRivensPC.json"
LOCAL_DATAFILE = r"data/weeklyRivensPC.json"

# Format of timestamp: Mon, 24 Nov 2025 01:00:03 GMT
# See: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
TIMESTAMP_FORMAT = '%a, %d %b %Y %X %Z' 


# This function is specific to the exact formatting the file uses;
# will not work on all pseudo-json files.
def _convert_to_valid_json(pseudoJSON):
	# replace single quotes with double quotes
	pseudoJSON = pseudoJSON.replace("'", '"')

	# replace each line's leading 4 spaces with 4 spaces AND a front quote
	pseudoJSON = pseudoJSON.replace('    ', '    "')

	# replace each line's colon with a colon preceded by a back quote
	return pseudoJSON.replace(':', '":')


def get_and_parse_data():
	payload = requests.get(SOURCE_URL)

	# data formatting differs from json slightly, so let's fix that
	dataString = _convert_to_valid_json(payload.text)

	# convert string into objects
	arrayOfDictionaries = json.loads(dataString)

	# get timestamp from header
	timestampString = payload.headers["last-modified"]
	timestamp = datetime.datetime.strptime(timestampString, TIMESTAMP_FORMAT)

	return {"timestamp": timestamp, "records": arrayOfDictionaries}



def _main():
	data = get_and_parse_data()
	print(data)

if __name__ == '__main__':
	_main()