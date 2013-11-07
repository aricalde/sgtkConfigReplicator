import sys
from shotgun_api3 import Shotgun


def _get_projects_list():
	sg = Shotgun('http://yoursite.com', 'your_api', '123456')

	filters = [['sg_status', 'is', 'Active'], ['tank_name', 'is_not', '']]
	fields = ['name']
	order = [{'field_name': 'name', 'direction': 'asc'}]
	projectsDic = sg.find('Project', filters, fields, order)

	newProjectsDic = []

	for project in projectsDic:
		newProjectsDic.append(project['name'].replace(' ', ''))

	return newProjectsDic
