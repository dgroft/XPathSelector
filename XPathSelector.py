import sublime, sublime_plugin, re

class XPathSelectorCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# TODO: pop up a window where the user enters an xpath expression
		# evaluate the xpath expression
		# select all instances in the buffer according to the evaluated xpath
		# remember the last 10 xpath expressions, start with the last one

		sublime.status_message("call to x_path_selector command a success")
