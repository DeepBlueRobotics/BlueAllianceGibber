print("importing...")
try:
	import tbapy
except:
	import os
	os.system("python3 -m pip install tbapy")
finally:
	import tbapy
print("\tdone")
		
#builtins
import json as js
import sys
import datetime
cmd_args = sys.argv[1:]

#key=input("Hey gimme ur key: ")
key = [
	"1Ju6nifJcZ9HKXAfTlYwFcZhXdhMpZHdoW1gAhFPWsrtge6HLJjPckbYYzaUse2N",
	"2023-10-05",
	"Team 199 access 1"
]
print("Connecting with key: "+key[0])
print(f"{key[1]} ||| {key[2]}")
tba = tbapy.TBA(key[0])
#tba = tbapy.TBA('key', 'ID', 'secret', 'event_key')


# code code code code code code code
team = tba.team(199)
districts, last_modified = tba.team_districts(199, last_modified=True)
years = [2020,2021,2022]
events = sum( [tba.team_events(199, y) for y in years], [])#don't worry about it - it just works
robots = tba.team_robots(199)

#print(dir(events[0]))

print(f'In years: {years}, team 199 was in %d events: \n%s.' % (len(events), ',\n'.join(f"\t{event.start_date} : {event.event_code} : {event.name}" for event in events)))
print(f'Team 199\'s districts: {districts}')
print(f'Team 199\'s robots: {robots}')
#examples stuff below


#import tbapy
#import datetime
#
## This key should ONLY be used for this example. If using this library in your own project,
## follow the steps in the README to generate your own key.
#tba = tbapy.TBA('TjUTfbPByPvqcFaMdEQVKPsd8R4m2TKIVHMoqf3Vya0kAdqx3DlwDQ5Sly4N2xJS')
#
#team = tba.team(254)
#districts, last_modified = tba.team_districts(1418, last_modified=True)
#match = tba.match(year=2017,
#                event='chcmp',
#                type='sf',
#                number=2,
#                round=1)
#events = tba.team_events(148, 2016)
#robots = tba.team_robots(4131)
#
#print('-' * 10 + ' Object Syntax' + '-' * 10)
#print('Team 254 is from %s in %s, %s.' % (team.city, team.state_prov, team.country))
#print('Team 1418 is/was in the %s district in the most recent year of competition.' % districts[-1].display_name)
#print('The second qual match at the 2017 CHS District Championship was predicted to start at Unix Time %s.' % match.predicted_time)
#print('In 2016, team 148 was in %d events: %s.' % (len(events), ', '.join(event.event_code for event in events)))
#print('Team 4131\'s robots: ' + ', '.join('%s (%d)' % (robot.robot_name, robot.year) for robot in robots))
#print('Robots have attribute name:', hasattr(robots[0], 'name'))
#print('Robots have attribute robot_name:', hasattr(robots[0], 'robot_name'))
#print()
#
#print('-' * 8 + ' Dictionary Syntax' + '-' * 8)
#print('Team 254 is from %s in %s, %s.' % (team['city'], team['state_prov'], team['country']))
#print('Team 1418 is/was in the %s district in the most recent year of competition.' % districts[-1]['display_name'])
#print('The second qual match at the 2017 CHS District Championship was predicted to start at Unix Time %s.' % match['predicted_time'])
#print('In 2016, team 148 was in %d events: %s.' % (len(events), ', '.join(event['event_code'] for event in events)))
#print('Team 4131\'s robots: ' + ', '.join('%s (%d)' % (robot['robot_name'], robot['year']) for robot in robots))
#print('Robots have attribute name:', 'name' in robots[0])
#print('Robots have attribute robot_name:', 'robot_name' in robots[0])
#print()
#
#print('-' * 5 + ' .raw() Dictionary Syntax' + '-' * 5)
#print('Team 254 is from %s in %s, %s.' % (team.raw()['city'], team.raw()['state_prov'], team.raw()['country']))
#print('Team 1418 is/was in the %s district in the most recent year of competition.' % districts[-1].raw()['display_name'])
#print('The second qual match at the 2017 CHS District Championship was predicted to start at Unix Time %s.' % match.raw()['predicted_time'])
#print('In 2016, team 148 was in %d events: %s.' % (len(events), ', '.join(event.raw()['event_code'] for event in events)))
#print('Team 4131\'s robots: ' + ', '.join('%s (%d)' % (robot.raw()['robot_name'], robot.raw()['year']) for robot in robots))
#print('Robots have attribute name:', 'name' in robots[0].raw())
#print('Robots have attribute robot_name:', 'robot_name' in robots[0].raw())
#print()
#
#print('-' * 8 + ' If-Modified-Since Header ' + '-' * 8)
#def fetch_cached_value():
#    return [tbapy.District({
#        'city': 'Falls Church',
#        'state_prov': 'Virginia',
#        'country': 'USA',
#        'cached': 'cached?'
#    })]
#
#date_last = last_modified.date
#date_old = datetime.datetime.utcnow().replace(year=2015)
#districts = tba.team_districts(1418, if_modified_since=date_last) or fetch_cached_value()
#print(f'Recent date -- Was the cached value used? {districts[0].get("cached") is not None}')
#districts = tba.team_districts(1418, if_modified_since=date_old) or fetch_cached_value()
#print(f'Old date -- Was the cached value used? {districts[0].get("cached") is not None}')