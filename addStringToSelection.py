import sublime
import sublime_plugin

class PromptAddStringToSelectionCommand(sublime_plugin.WindowCommand):
    def run(self):
        # sublime.set_clipboard('that')
        self.window.show_input_panel("Add string to selection", "", self.on_done, None, None)

    def on_done(self, text):
        try:
            if self.window.active_view():
                self.window.active_view().run_command("add_string_to_selection", {"strtoadd": text})
        except ValueError:
            pass

class AddStringToSelectionCommand(sublime_plugin.TextCommand):
    def run(self,edit,strtoadd):
        editedstr = ''
        for i, tx in enumerate(self.view.sel()):
            editedstr += strtoadd + self.view.substr(tx) + " "
        sublime.set_clipboard(editedstr)

