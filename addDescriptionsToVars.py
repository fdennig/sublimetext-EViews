import EViews.yaml as yaml
import os
import sublime
import sublime_plugin
from collections import OrderedDict

# class PromptJoinVarlistWithDatabaseCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         # sublime.set_clipboard('that')
#         self.window.show_input_panel("Type in country code", "", self.on_done, None, None)

#     def on_done(self, text):
#         try:
#             if self.window.active_view():
#                 self.window.active_view().run_command("add_descriptions_to_vars", {"strtoadd": text})
#         except ValueError:
#             pass

def CreateEntryFromGlossary(modelEntry, glossaryEntry):
    d = modelEntry
    d["description"] = glossaryEntry.get("description")
    d["unit"] = glossaryEntry.get("unit")
    return d

class PullDescriptionsForVarlistCommand(sublime_plugin.TextCommand):
    def run(self,edit,varListFile, glossaryFile):

        # print(prefix)
        prefix = "MF"
        # fileName = self.view.file_name()

        with open(varListFile, 'r') as modelFile:
            modelVars = yaml.full_load(modelFile)

        # with open(os.path.join(sublime.packages_path(),"EViews","MFMOD-notes","MFMODvariables.yml"), 'r') as glossaryFileTemp:
        with open(glossaryFile, 'r') as glossaryFileTemp:
            glossaryVars = yaml.full_load(glossaryFileTemp)

        modelVarsWithoutDescription = dict()

        for entry in modelVars:
            glossaryEntry = glossaryVars.get(entry)
            glossaryStrippedEntry = glossaryVars.get(entry[3:])
            newEntry = glossaryEntry or glossaryStrippedEntry

            if newEntry:
                d = CreateEntryFromGlossary(modelVars[entry],newEntry)
                modelVars[entry] = d
            elif modelVars[entry].get("description") is not None:
                pass
            else:
                modelVarsWithoutDescription[entry] = CreateEntryFromGlossary(modelVars[entry],modelVars[entry])

        varListFileName = os.path.basename(varListFile)
        varListFileNameNoExtension, varListFileNameExtension = os.path.splitext(varListFileName)

        outputFile = "{}.yml".format(varListFileNameNoExtension)
        with open(os.path.join(os.path.dirname(varListFile), outputFile), 'w+') as updatedVars:
            variables = yaml.dump(modelVars, updatedVars)

        missingDescriptionsOutput = "{}WithoutDescriptions.yml".format(varListFileNameNoExtension)
        with open(os.path.join(os.path.dirname(varListFile), missingDescriptionsOutput), "w+") as missingVars:
            missingVariables = yaml.dump(modelVarsWithoutDescription, missingVars)

    def input(self, args):
        return varListFileInputHandler(self.view)

class varListFileInputHandler(sublime_plugin.ListInputHandler):
    def __init__(self, view):
        self.view = view

    def name(self):
        return "varListFile"

    def placeholder(self):
        return "Mod Vars"

    def list_items(self):
        folderList = self.view.window().folders()
        fileList = []
        fileList.append(("Currently open file", self.view.file_name()))
        for folder in folderList:
            for (dirpath, dirnames, filenames) in os.walk(folder):
                for name in filenames:
                    if name.endswith('.yml' or '.yaml'):
                        filePair = (name, os.path.join(dirpath, name))
                        fileList.append(filePair)
        return fileList

    def next_input(self,args):
        return GlossaryFileInputHandler(self.view)
        # return PrefixInputHandler()

# class PrefixInputHandler(sublime_plugin.TextInputHandler):
#     def placeholder(self):
#         return "Country Code"

    # def next_input(self):
    #     return GlossaryFileInputHandler(self.view)

class GlossaryFileInputHandler(sublime_plugin.ListInputHandler):
    def __init__(self, view):
        self.view = view

    def name(self):
        return "glossaryFile"

    def placeholder(self):
        return "Glossary"

    def list_items(self):
        folderList = self.view.window().folders()
        fileList = []
        fileList.append(("MFMOD Glossary (default)", os.path.join(sublime.packages_path(),"EViews","MFMODresources","MFMODvariables.yml")))
        for folder in folderList:
            for (dirpath, dirnames, filenames) in os.walk(folder):
                for name in filenames:
                    if name.endswith('.yml' or '.yaml'):
                        filePair = (name, os.path.join(dirpath, name))
                        fileList.append(filePair)
        return fileList

    # def next_input(self, args):
    #     return PrefixInputHandler()
