#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.
import time
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

### Protocol Implementation

# This is just about the simplest possible protocol
class Echo(Protocol):
	def dataReceived(self, data):
		"""
		As soon as any data is received, write it back.
		"""
		print type(data)
		print data
		print "processing"
		time.sleep(10)
		print "finish"
		self.transport.write(data)

def main():
	f = Factory()
	f.protocol = Echo
	reactor.listenTCP(50000, f)
	reactor.run()

if __name__ == '__main__':
	main()