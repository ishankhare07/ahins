import subprocess
import sys

print('creating git archive')
result = subprocess.Popen(['git', 'archive', 'master', '-o', 'deployment.tar.gz'])
result.wait()
print('archive successfully created')

print('transfering tarball to the server')
scp = subprocess.Popen(['gcloud compute scp ' + 'deployment.tar.gz post_ssh.sh' + ' ishan@blog:~/'], shell=True)
scp.wait()
print('tarbal transfer complete')

print('ssh-ing into the server', 'running post_ssh.sh on the server', sep='\n')
post_ssh = subprocess.Popen(['gcloud', 'compute', 'ssh', 'ishan@blog', '--', './post_ssh.sh'])
post_ssh.wait()
print('post_ssh execution complete', 'try going at https://ishankhare.com to see the changes live', sep='\n')

