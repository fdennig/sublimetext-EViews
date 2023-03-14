import sublime
import sublime_plugin
import re

class SelectVarsFromStringCommand(sublime_plugin.TextCommand):
    def run(self,edit, prefix, suffix):
        editedstr = ''
        editedlist = []
        tx = self.view.sel()[0]
        wrds = re.findall(r'\b[a-zA-z_]{5,}\b', self.view.substr(tx))
        for j, wx in enumerate(wrds):
            editedstr += prefix + wx + suffix + " "
            editedlist.append(prefix + wx + suffix)
        txa = ""
        txb = self.view.substr(tx)
        for k, qx in enumerate(wrds):
            a = txb.find(qx) + len(editedlist[k])
            txc = txb.replace(qx, editedlist[k], 1)
            txa = txa + txc[0:a]
            txb = txc[a:]
        txa = txa + txb
        sublime.set_clipboard(txa)

    def input(self, args):
        return PrefixInputHandler(self.view)

class PrefixInputHandler(sublime_plugin.TextInputHandler):
    def __init__(self,view):
        self.view = view
        self.prefixedList = []

    def name(self):
        return "prefix"

    def placeholder(self):
        return "Prefix"

    def preview(self, text):
        prefixedString = ''
        prefixedList = []
        for i, tx in enumerate(self.view.sel()):
            wrds = re.findall(r'\b[a-zA-z_]{5,}\b', self.view.substr(tx))
            for j, wx in enumerate(wrds):
                prefixedString += text + wx + " \n"
                prefixedList.append(text + wx)
        self.prefixedList = prefixedList
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
