import sublime, sublime_plugin, os
from os.path import dirname, realpath

class SampBuildCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.save()
        self.myplugin(edit)

    def save(self):
        self.view.run_command("save")

    def myplugin(self, edit):
        branch, leaf = os.path.split(self.view.file_name())
        filePath = self.view.file_name()
        commandLine = "pawno\pawncc.exe "

        branch = branch.replace("filterscripts", commandLine)
        branch = branch.replace("gamemodes", commandLine) 

        print("DEBUG: " + branch)
        self.view.window().run_command('exec', { 'cmd': [branch, filePath], 'quiet': False })  
