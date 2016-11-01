
The *Original* Behchmark "**The Computer Language Benchmarks Game**" can download from http://benchmarksgame.alioth.debian.org/.

And also this benchmark follows BSD licence.

The different from original benchmark, is this benchmark use psutil from Python. Because original benchmakr uses python-gtop from Python, but this add-on doesn't provied nowdays. So, I *modified bin/planC.py* to use psutil for measures **CPU usage(%)**, **Memory Usage(MB)**. 

If you want to use this benchmark, these tools are required:
  - **GCC**(4.6.3)
  - **Python**(2.7.3)
  - **Python3**(3.2.3)
  - **python-gtop**
  - **Lua**(5.2.1)
  - **Java**(JDK 1.8.0, *not gnu*)
  - **psutil**


### Installation

pstuil can installed by follows.

Debian:

```sh
$ sudo apt-get install -y python-psutil python-pip python-dev
$ sudo pip install psutil
```

### Benchmark Set

For evaluation, I picked benchmark sets to executable in general environments.
* binarytrees
* n-body
* fannkuch-redux
* mandelbrot
* fasta
* spectral-norm


More detail descriptions can find here: http://benchmarksgame.alioth.debian.org/u64q/binarytrees-description.html. 

### Evaluation Environment

For this benchmark measure performance(CPU and Memory useage, execution time), I used Raspberry pi 1 Model B(ARM-v6 700MHz/512MB RAM) and raspbian OS. Also I used *Monsoon Power Monitor* for measure Energy for execution of each benchmark. And Source Line of Code was calculated by *CLOC*. 


### How to Run

This benchmark witten by Python and script files are located in **Benchmark/bin** directory. And I made *bin/run.sh* file can run benchmark easily. This shell code includes the job which remove existing result files.

```sh
$ sudo chmod 755 run.sh // change permission
$ ./run.sh              // benchmark will run
```

### Result of Measurement

 **1. binarytrees**
 
|Language|SLOC|CPU Usage(%)|Memory Usage(MB)|Execution Time(s)|Consumption Energy(mJ)|
|-------|----|----|----|----|----|
|Python|48|92.9|7.72|3598|7135.48| 
|C|118|93.9|0.00|124|239.86| 
|Java|51|93.9|13.61|2693|5341.49| 
|Lua|40|91.9|2.09|1234|2457.91|

 **2. fannkuch-redux**

|Language|SLOC|CPU Usage(%)|Memory Usage(MB)|Execution Time(s)|Consumption Energy(mJ)|
|-------|----|----|----|----|----|
|Python|85|93.0|7.61|7571|14611.38|
|C|86|92.9|0.00|87|158.93|
|Java|150|93.9|13.49|2660|5333.62|
|Lua|40|92.9|0.67|1133|2178.28| 

 **3.fata**
 
|Language|SLOC|CPU Usage(%)|Memory Usage(MB)|Execution Time(s)|Consumption Energy(mJ)|
|-------|----|----|----|----|----|
|Python|62|93.9|7.23|6696|12963.90| 
|C|103|91.8|0.00|107|203.92| 
|Java|125|93.0|13.47|2781|5478.14| 
|Lua|86|92.9|0.00|398|773.86|
 
 **4. mandelbrot**
 
|Language|SLOC|CPU Usage(%)|Memory Usage(MB)|Execution Time(s)|Consumption Energy(mJ)|
|-------|----|----|----|----|----|
|Python|87|91.8|525.82|87516|167746.29| 
|C|42|92.0|1.24|2370|4529.49| 
|Java|87|92.9|15.70|4509|8912.52| 
|Lua|61|92.9|16.00|8623|16821.32|

 **5. n-body**
 
|Language|SLOC|CPU Usage(%)|Memory Usage(MB)|Execution Time(s)|Consumption Energy(mJ)|
|-------|----|----|----|----|----|
|Python|89|93.9|6.83|2203|4370.32|
|C|124|92.9|0.00|69|131.11| 
|Java|140|92.0|14.78|3304|6518.05| 
|Lua|114|92.9|0.00|194|375.44|

**6. spectral-norm**

|Language|SLOC|CPU Usage(%)|Memory Usage(MB)|Execution Time(s)|Consumption Energy(mJ)|
|-------|----|----|----|----|----|
|Python|39|93.9|40.29|293766|569392.24| 
|C|40|92.1|0.93|3623|6878.66| 
|Java|117|91.0|15.67|5247|10250.18|
|Lua|33|93.8|1.40|30824|60390.60|