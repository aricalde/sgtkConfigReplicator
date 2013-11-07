import yaml

def _build_path(project, jobpath, pathtype):
	
	config_file = open('modules/jobs_config.yml', 'r')
	config_dict = yaml.load(config_file.read())
	config_file.close()

	LocalServerPath = config_dict['Paths']['Original Projects Path']
	RemoteServerPath = config_dict['Paths']['Target Projects Path']

	if pathtype == 'origin':
		projectsPath = LocalServerPath
	elif pathtype == 'target':
		projectsPath = RemoteServerPath
	else:
		raise Exception('the specified pathtype: "' + pathtype + '" is not valid!!' + 
						'\n' + 'Expected values are: origin, target')

	sync_path = projectsPath + project + jobpath

	return sync_path