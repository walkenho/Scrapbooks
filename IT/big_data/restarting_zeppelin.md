`
1 stop zeppelin
               sudo
2              yarn application –list, 
followed by multiple 
	yarn application –kill <applicationid>
3 to list zeppelin processes, 
	ps –ef | grep zeppelin 
followed by multiple 
	kill <processid> 
to stop all orphan zeppelin processes (1, the id that holds 9995 open had to be killed by first sudoing to root (sudo su - root)
 
4 restart/start of zeppelin then worked
                /usr/hdp/current/zeppelin-server/bin/zeppelin-daemon.sh start
 
`
