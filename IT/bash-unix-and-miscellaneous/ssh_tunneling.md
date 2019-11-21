Moba Xterm provides a GUI for establishing a tunneling ssh connection. However, the provided buttons do not work reliably. An alternative is to establish the tunnel from the command line. This can be achieved by:

(Add -f if you want it to run in the background)

Note, that this establishes a tunnel starting from the local port 9007. I chose to not use 8889 since this is Jupyter's standard port. This has as a consequence that if you open a Jupyter session locally, it gets confused. The same is true for 8890, etc since if you open a second session, it will start counting upwards.

https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers provides a list of standard port numbers and 9007 is not listed as standard port for any application and leaves enough room to both sides, so it seems like a reasonable choice. 

https://www.laurencegellert.com/2011/01/command-line-ssh-tunnel-port-forwarding/ gives a good introduction to port forwarding on the command line.

As an example it gives:
ssh -l youruser yourhost.com -p 22 -N -f -C -L 3306:yourdbserver.com:3306

With the argument summary:
-l 	login name
-p 	remote host port (It is best to connect to ssh on something other than the default port to shake off automated attacks. Change sshd.conf and/or the port mapping on your firewall. For example :2210 external maps to :22 internal for your ssh boxes that are allowed to accept outside connections.)
-N 	do not execute a remote command
-f 	requests SSH to go to background
-L port:host:hostport 	(port = local port, host and hostport are where you want the tunnel to point to. This does not have to be the box you are ssh-ing to!)
-C 	compression – optional

How to tell if the tunnel is working:

#check for ssh process with the parameters specified above
$ ps aux | grep ssh
#or, try to talk to it
$ telnet localhost 3306
When you are done with the tunnel and want to shut if off:

#find the tunnel that was setup on port 3306 and shut it down
#alter "3306:" to match the local port tunnel to shut off
ps -fU root -C ssh | grep "ssh -l" | grep "3306:" | awk '{print $2}' | xargs kill
