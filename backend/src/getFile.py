import urllib.request
import json

# datafile documentation at
# https://forums.warframe.com/topic/1077490-riven-trading-toolbuilders-phase-1/
SOURCE_URL = r"https://www-static.warframe.com/repos/weeklyRivensPC.json"
LOCAL_DATAFILE = r"data/weeklyRivensPC.json"

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
	# Get latest datafile from the web endpoint (will overwrite)
	urllib.request.urlretrieve(SOURCE_URL, LOCAL_DATAFILE)

	# put datafile's data into string
	with open(LOCAL_DATAFILE, 'r') as datafile:
		dataString = datafile.read()

	# data formatting differs from json slightly, so let's fix that
	dataString = _convert_to_valid_json(dataString)

	# data becomes objects
	arrayOfDictionaries = json.loads(dataString)

	return arrayOfDictionaries
