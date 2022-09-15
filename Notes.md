15th Sep 2022
----------------
Tried with execute_async but it's still taking time. 
Infact it's taking more. 

14th Sep 2022
-------------------
Cassandra is working now. 
Could not make it work with 2 or 4g of memory. 
Docker mahcines were crashing. 
Gave it free reign and it worked. 

Replication is working 

Throughput is back to 3-5 seconds. 
Now I need to think of how to put the database call in a new thread and return the response in flask. 
This will increase the throughput. 

For database calls the question is still how to save is persistenly. 
I can try to write to local file which is some append only file but how can many threads write to it. 
Need to read on how to do db calls to thread in flask. 

? Another thing is to make sure fake loadbalancer is working correctly with differnet ports 
check the github link from last entry

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



