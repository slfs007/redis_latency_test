import redis
import time
import matplotlib.pyplot as plt
r_mk = redis.StrictRedis(host='localhost',port=6379,db=0)

def latency_test(entry_size,entry_count,host_addr,port_num,db_num,workload_count):

    r = redis.StrictRedis(host=host_addr,porn=port_num,db=db_num)

    val = '{:< +' + str(entry_size) + '}'
    val = val.format(' ')
    print val

    latencyList = []
    timeList = []
    timeBase = time.time()
    for i in range(0,workload_count,1):
        timeStart = time.time()
        r.set(str(i%entry_count),val)
        timeEnd = time.time()
        timeList.append(timeStart - timeBase)
        latencyList.append(timeEnd - timeStart)

    return timeList,latencyList

if __name__ == '__main__':
    entrySize = 1000
    entryCount = 1000
    workloadCount = 10000

    timeList,latencyList = latency_test(entry_size=entrySize,entry_count=entryCount,workload_count=workloadCount,
                                        host_addr='localhost',port_num=6379,db_num=0)

    plt.plot(timeList,latencyList)
    plt.show()