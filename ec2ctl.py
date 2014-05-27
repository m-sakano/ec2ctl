import sys
import boto.ec2

# User variables---------

region = "ap-northeast-1"
instance_id = ["i-f2b5f1f4"]

# -----------------------

if (len(sys.argv) != 2):
    print 'Usage: # python %s {start|stop|status}' % sys.argvs[0]
    quit()

conn = boto.ec2.connect_to_region(region)

if sys.argv[1] == 'start':
	for a in conn.start_instances(instance_ids=instance_id):
		print '%s' % a
elif sys.argv[1] == 'stop':
	conn.stop_instances(instance_ids=instance_id)
elif sys.argv[1] == 'status':
	reservations = conn.get_all_instances()
	for res in reservations:
	    for inst in res.instances:
	    	if inst.id == instance_id[0]:
		        if 'Name' in inst.tags:
		            print "%s (%s) [%s]" % (inst.tags['Name'], inst.id, inst.state)
		        else:
		            print "%s [%s]" % (inst.id, inst.state)
else:
	print 'Usage: # python %s {start|stop|status}' % sys.argv[0]

