# MapReduce
1. Run   jobs   by
```hadoop jar /usr/lib/hadoop - mapreduce /hadoop - streaming.jar \ - files mapper.py,reducer.py -mapper mapper.py - reducer reducer.py \ - input /input - output /output```
2.   There   are   three   clusters   created:   one   master   and   two   workers    
      Master:    2   virtual   CPU,   7,75   GB Disk   size   100+400GB
      Worker:         2   virtual   CPU,   7,75   GB   (I   later   changed   the   machine   type) Disk   size   500GB

## Problem setting
### Design a MapReduce job flow to:
1. Read all the wikimedia entries for October 2017 from https://dumps.wikimedia.org/
other/pageviews/2017/2017-10/ (you will need to download the entries)
2. Filter out elements based on the rules discussed in previous assignment.
3. In addition to what you may have filtered, there are some malformed entries
which need to be filtered. Malformed entries are entries with missing article
name. Make sure that you filter these entries.
4. Aggregate the pageviews from hourly views to daily views.
5. Calculate the total pageviews for each article.
6. For every article that has page-views over 100,000, print the following line as
output (\t is the tab character):
```<total month views>\t<article name>\t<date1:page views for date1>\t<date2:page views for date2> ...```
7. Getting the input filename from within a Mapper: As the date/time information is encoded in the filename, Hadoop streaming makes the filename available to every map task through the environment variables mapreduce_map_input_file, map_input_file or map.input.file. For example, the filename can be accessed in python using the statement os.environ["mapreduce_map_input_file"], or in Java using the statement System.getenv("mapreduce_map_input_file")
2. Once you have designed and tested your MapReduce job flow on a small portion of the dataset, please run it on the entire dataset of February 2017 using MapReduce.
3. Please note the cluster configuration and runtime in minutes of your solution.
4. In addition, put top 10 lines from your MapReduce results in the report
