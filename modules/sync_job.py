import subprocess

def _sync_job(job):

	excludedFiles = job['exclusions']

	NewExcludedFiles = []
	if excludedFiles != None:
		for fileName in excludedFiles:
			NewExcludedFiles.append('--exclude=' + fileName)

	command = ['rsync', '-av', job['from'], job['to']]

	for exclusion in NewExcludedFiles:
		command.insert(2, exclusion)

	rsync = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = rsync.communicate()
	if rsync.returncode != 0:
	    raise Exception(stderr)