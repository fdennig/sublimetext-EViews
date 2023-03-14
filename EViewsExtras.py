import os

import sublime
import sublime_plugin

# class TestCommand(sublime_plugin.WindowCommand):
class AddTutorialToProjectCommand(sublime_plugin.WindowCommand):
    def run(self):
        plugin_dir = os.path.dirname(os.path.realpath(__file__))
        tutorial_dir = os.path.join(plugin_dir, 'MFMODresources')
        pathobj = {"path": tutorial_dir}
        project_data = self.window.project_data()
        print(str(project_data))
        if ((project_data is None) or (len(project_data) == 0)):
            print("there exists no project data")
            project_data = {"folders": [pathobj]}
            self.window.set_project_data(project_data)
            # print(str(self.window.project_data()))
            html = """
                <body id="my-plugin-feature">
                    <style>
                        h1 {
                            font-size: 1.1rem;
                            font-weight: 500;
                            margin: 0 0 0.5em 0;
                            font-family: system;
                        }
                        p { margin-top: 0;}
                    </style>
                    <h1> Confirmation </h1>
                    <p>
                        You have created project including MFMODresources.
                    <br> Now add the folder with codebase and save project
                    </p>
                </body>
            """
            self.window.active_view().show_popup(html, flags = 24)

        elif "folders" in project_data.keys():
            if any(obj['path'] == tutorial_dir for obj in project_data["folders"]):
                html = """
                    <body id="my-plugin-feature">
                        <style>
                            h1 {
                                font-size: 1.1rem;
                                font-weight: 500;
                                margin: 0 0 0.5em 0;
                                font-family: system;
                            }
                            div.message {padding: 5px;}
                        </style>
                        <div class="message">
                            You have already added MFMODresources to this project
                        </div>
                    </body>
                """
                self.window.active_view().show_popup(html, flags = 24)

            else:
                print("tutorial was added")
                project_data["folders"].append(pathobj)
                self.window.set_project_data(project_data)
                html = """
                    <body id="my-plugin-feature">
                        <style>
                            h1 {
                                font-size: 1.1rem;
                                font-weight: 500;
                                margin: 0 0 0.5em 0;
                                font-family: system;
                            }
                            p { margin-top: 0;}
                        </style>
                        <h1> Confirmation </h1>
                        <p>
                            You have now added the MFMODresources to this project
                        </p>
                    </body>
                """
                self.window.active_view().show_popup(html, flags = 24)

def load_resource(name):
    """Return file contents for files within the package root folder."""
    try:
        return sublime.load_resource('Packages/{}/{}'.format(__package__, name))
    except Exception:
        log("Error while load_resource('%s')" % name)
        traceback.print_exc()
        return ''

def exists_resource(resource_file_path):
    """Check if resource exists."""
    filename = os.path.join(os.path.dirname(sublime.packages_path()), resource_file_path)
    return os.path.isfile(filename)

def new_view(window, text, scratch=False):
    """
    Create a new view and paste text content.

    Return the new view that can optionally can be set as scratch.
    """

    new_view = window.new_file()
    if scratch:
        new_view.set_scratch(True)
    new_view.run_command('append', {
        'characters': text,
    })
    return new_view

class EquationExtractorCommand(sublime_plugin.TextCommand):
    """Open the equation extractor prg"""

    def run(self, edit):
        """Execute command."""
        lines = '\n'.join(load_resource('MFMODresources/equationExtractor.prg').splitlines())
        view = new_view(self.view.window(), lines, scratch=True)
        view.set_name("Extraction subroutines")

        # Set syntax file
        syntax_files = [
            os.path.join(plugin_dir, "EViews.sublime-syntax")
        ]
        for file in syntax_files:
            if exists_resource(file):
                view.set_syntax_file(file)
                break  # Done if any syntax is set.

        sublime.status_message('Extraction subroutines opened')


class MfmodVarsCommand(sublime_plugin.TextCommand):
    """Open the equation extractor prg"""

    def run(self, edit):
        """Execute command."""
        lines = '\n'.join(load_resource('MFMODresources/MFMODvariables.yml').splitlines())
        view = new_view(self.view.window(), lines, scratch=True)
        view.set_name("MFMOD variables")

        # Set syntax file
        file = "Packages/YAML/YAML.sublime-syntax"
        if exists_resource(file):
            view.set_syntax_file(file)


        sublime.status_message('MFMOD dictionary opened')
