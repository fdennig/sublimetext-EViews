import os

import sublime
import sublime_plugin

# class TestCommand(sublime_plugin.WindowCommand):
class AddTutorialToProjectCommand(sublime_plugin.WindowCommand):
    def run(self):
        plugin_dir = os.path.dirname(os.path.realpath(__file__))
        tutorial_dir = os.path.join(plugin_dir, 'MFMOD-notes')
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
                        You have created project including MFMOD-notes.
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
                            You have already added MFMOD-notes to this project
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
                            You have now added the MFMOD-notes to this project
                        </p>
                    </body>
                """
                self.window.active_view().show_popup(html, flags = 24)
