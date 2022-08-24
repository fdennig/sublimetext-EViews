import sublime
import sublime_plugin

class AddStringToSelectionCommand(sublime_plugin.TextCommand):
    def run(self,edit, prefix, suffix):
        editedstr = ''
        for i, tx in enumerate(self.view.sel()):
            editedstr += prefix + self.view.substr(tx) + suffix + " "
        sublime.set_clipboard(editedstr)

    def input(self, args):
        return PrefixInputHandler(self.view)

class PrefixInputHandler(sublime_plugin.TextInputHandler):
    def __init__(self,view):
        self.view = view
        self.prefixedList = []
    # def name(self):
    #     return "prefix"

    def name(self):
        return "prefix"

    def placeholder(self):
        return "Prefix"

    def preview(self, text):
        prefixedString = ''
        prefixedList = []
        for i, tx in enumerate(self.view.sel()):
            prefixedString += text + self.view.substr(tx) + " \n"
            prefixedList.append(text + self.view.substr(tx))
        self.prefixedList = prefixedList
        print(self.prefixedList)
        return prefixedString

    def next_input(self,args):
        return SuffixInputHandler(self.view, self.prefixedList)

class SuffixInputHandler(sublime_plugin.TextInputHandler):
    def __init__(self,view, prefixedList):
        self.view = view
        self.prefixedList = prefixedList

    def name(self):
        return "suffix"

    def placeholder(self):
        return "Suffix"

    def preview(self, text):
        suffixedString = ''
        for i, tx in enumerate(self.prefixedList):
            suffixedString += tx + text + " \n"
        return suffixedString
