import datetime as dt
from mwrogue.esports_client import EsportsClient

Lolsite = EsportsClient('lol')



def getMatches(matches, date):
	date1 = (date + dt.timedelta(1))
	date2 = (date + dt.timedelta(2))

	response2 = Lolsite.cargo_client.query(tables="MatchSchedule",
										   fields="Team1, Team2, ShownName, DateTime_UTC",
										   limit="max",
										   where="DateTime_UTC >= '" + str(date) + "' AND DateTime_UTC <= '" + str(
											   date1) + "'")

	TODAY_MATCHES = list()
	for row in response2:
		if any(ext in row['ShownName'] for ext in matches):
			TODAY_MATCHES.insert(len(TODAY_MATCHES), row)
	matches = list()
	for r in TODAY_MATCHES:
		date = r['DateTime UTC']
		date = date.split(' ')
		matchString = r['Team1'] + ' VS. ' + r['Team2'] + ' at ' + date[1] + ' ' + r['ShownName']
		matches.append(matchString)

	return matches
