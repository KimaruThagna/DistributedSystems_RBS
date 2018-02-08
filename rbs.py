# p15/1691/2016
# CSC 315 Distributed systems
# RBS implementation
import random,datetime
def master(): # the main function...simulate sending empty packet
    process1() # call functions(processes to simulate sending packet
    process2()
    process3()
    process4()
    process5()
#emulating the processes
# The main logic engine....all processes work the same way thus no need to replicate code
def work(x=0,token=0):
    # x tells the process number token tells whether the process is reading or writing
    if token==0:#write
        # time_to_send is the current time plus a timedelta so as to create a large enough difference
        # visible to the reader instead of a difference of milliseconds
        time_to_send = datetime.datetime.time(datetime.datetime.now() + datetime.timedelta(minutes=random.randrange(0, 10)))
        myfile = open('time_deck.txt', 'a') #open file for writing in append mode
        time_to_file = str(time_to_send) + '\n'
        myfile.write(time_to_file) #write to file
    if token == 1: # reading
        rfile = open('time_deck.txt', 'r').read()
        times = str(rfile).split('\n') #get the 5 process times
        minute_dump = 0 # cummulative sum
        for process_time in times: #process each time stamp in a loop
            if process_time != "":
                time_array = process_time.split(':')
                minute_dump += float(time_array[1]) # obtain the minute value from the time
        avg_min = minute_dump / 5 # get average time in minutes
        hr = times[x].split(':')
        get_hr = hr[0]
        offset = avg_min - float(hr[1]) # get difference between reference time
        # and the process time(difference will be in the realm of minutes hence
        # no need to deal with hours( for demo purposes but a real world application
        # would differ in a matter of milliseconds)
        # print reference time
        print("Reference time is:" + str(get_hr) + ":" + str(round(avg_min)))
        # print the process time( the time it recorded after receiving the empty packet)
        print("Process time:" + str(times[x]))
        #print offset
        print("Offset value of process"+str(x+1)+" is:" + str(round(offset)))

#create processes
def process1(token=0):
   work(0,token)
def process2(token=0):
   work(1,token)
def process3(token=0):
   work(2,token)
def process4(token=0):
   work(3,token)
def process5(token=0):
   work(4,token)
# call master function...thus simulate the master sending the empty packet and initiating whole process
master()
# call functions....ie, initiate processes to read
print("///////////////////////////PROCESS 1//////////////////////////////////////////////////")
process1(token=1)
print("///////////////////////////PROCESS 2//////////////////////////////////////////////////")
process2(token=1)
print("///////////////////////////PROCESS 3//////////////////////////////////////////////////")
process3(token=1)
print("///////////////////////////PROCESS 4//////////////////////////////////////////////////")
process4(token=1)
print("///////////////////////////PROCESS 5//////////////////////////////////////////////////")
process5(token=1)
