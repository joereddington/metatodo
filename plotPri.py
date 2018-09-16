#!/home/joereddington/env/bin/python
import numpy as np
import time
import matplotlib.pyplot as plt
import os
import argparse

#Todo


# Plan for adding the long term charting
# 1. Get working locally by adding a argparse that includes the source, and number of days
# 2. Include the compress function and add a switch to use it.
# 3. That means that all we need is the right commands and we're laughing. This
# is actually a reasonable

# Next action - argparse


DEST = "priority.png"
DAYS = 7
SMOOTHING=1


def get_content(infilename):                                                              
        with open(infilename) as f:                                                       
                content = f.readlines()                                                   
        return content      

class ProductivityPlotter():


	"Class designed to take a Jurgen-formatted file and turn it into a graph"
	def __init__(self,args,dest):
                self.args=args
		if args.f ==None:
		   raise Exception("No file name given!")
		self.source=args.f
		self.dest=dest
                if args.o:
                    self.dest=args.o
		self.days=int(args.d)
                self.ticklength=int(args.t)

	def smooth(self,y, box_pts=SMOOTHING):
	    box = np.ones(box_pts)/box_pts
	    y_smooth = np.convolve(y, box, mode='same')
	    return y_smooth#from stackexcahnge

	def array_to_lists(self,content):
                import calendar
                import time
                current_seconds=calendar.timegm(time.gmtime())
                seconds_at_start=current_seconds-(60*60*24*self.days)
		dayold, weekold,threedayold,seconds,now=([],[],[],[],[])
		count=0
                for rawline in content:
			     splitline=rawline.split(',')
                             if seconds_at_start < splitline[1]:
                             #   dayold.insert(0,int(splitline[4]))
                             #   threedayold.insert(0,int(splitline[5]))
                             #   weekold.insert(0,int(splitline[3]))
                                seconds.insert(0,int(splitline[1]))
                                now.insert(0,int(splitline[2]))
		return (seconds,now,dayold,threedayold,weekold)

	def graph(self,seconds,now, dayold, threedayold,weekold):
		x = np.array(seconds)
		ynow  = self.smooth(np.array(now))
		print now
		#yday  = self.smooth(np.array(dayold))
		#y3day = self.smooth(np.array(threedayold))
		#yweek = self.smooth(np.array(weekold))
		plt.plot(x,now, 'blue')
		#plt.plot(x,yday, 'green')
		#plt.plot(x,y3day,'purple')
		#plt.plot(x,yweek, 'red')
                import calendar
                import time
                current_seconds=calendar.timegm(time.gmtime())
                seconds_at_start=current_seconds-(60*60*24*self.days)
		plt.xlim(seconds_at_start, current_seconds-1000)
		plt.ylim(ymax=200)
		ticks=np.arange(seconds_at_start,current_seconds,(current_seconds-seconds_at_start)/self.ticklength)
		labels=[time.strftime("%a", time.gmtime(x)) for x in ticks]
		plt.xticks(ticks,labels)
		plt.grid()
		plt.savefig(self.dest)

	def get_graph(self):
                a=[]
                if self.args.c:
                    a=self.array_to_lists(compress(get_content(self.source)))
                else:
                    a=self.array_to_lists(get_content(self.source))
		self.graph(a[0],a[1],a[2],a[3],a[4])
		print "%s written with output from %s"%(self.dest, self.source)


def setup_argument_list():
    "creates and parses the argument list for Watson"
    parser = argparse.ArgumentParser( description="creates the priority chart")
    parser.add_argument('-f', nargs="?", help="File to use for data")
    parser.add_argument('-o', nargs="?" , help="outputfile")
    parser.add_argument( '-d', nargs="?", help="days", default=7)
    parser.add_argument( '-t', nargs="?", help="ticklength", default=7)
    parser.add_argument( '-c', action='store_true', help="should we compress")
    parser.set_defaults(verbatim=False)
    return parser.parse_args()



def compress(content):
        # the array we have is going to be horizonal when we need vertical. So
        # we have to deal with that.
        count = 0
        splitline = "hello world".split()
        outString = []
        for rawline in content:
                lastsplitline = splitline
                splitline = rawline.split()
                count = count+1
                if splitline[1] != lastsplitline[1]:
                        outString.append(rawline)
        return outString


if __name__ == "__main__":
        args=setup_argument_list()
	a=ProductivityPlotter(args,DEST)
	a.get_graph()

