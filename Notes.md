12th Sep 2022
-----------------
Now trying to learn cassandra from here ![](https://github.com/rmoreira/cassandra-project)

Still unable to make it run. 
Docker using too much memory. 

I just wanted a simple solution. 

Adding db init scripts. 
change db code. 
updating docker-compose.yaml

11th Sep 2022
-------------

I am able to insert into the cassandra database but the insertion has increased the processing time and decreased the throughput. 
it's taking around 5 sec to process one request and this is causing issue. 

![](./images/jmeter_11_sept_1.png)

Now we should have fast insertion in the database and fast read also. 

I will mull over this problem later on how I can fast this up. 

Another problem I am noticing is my cassandra one of the servers is failing. 
Why is that ? 

Need to explore on that. 

Current problems : 
1. Cassandra taking long time to insert
2. One of nodes failing 
3. Attach redis.

Next issue is using redis cache. 



