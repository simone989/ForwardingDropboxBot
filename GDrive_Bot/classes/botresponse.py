#!/usr/bin/env python

class Response(object):
	def __init__(self):
		self.responseFile = open("bot.txt","r")

	def textResponse(self, message):
		self.responseFile.read()
		self.textLines = self.responseFile.splitlines()
		print (self.textLines)
	def prova(self):
		print("prova")