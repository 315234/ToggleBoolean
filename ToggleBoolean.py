'''Plugin which will change the value under the cursor between true/false'''
import sublime
import sublime_plugin

class ToggleBoolean(sublime_plugin.TextCommand):
    replacements = {
        "True": "False",
        "true": "false",
        "TRUE": "FALSE",
        "on": "off",
        "yes": "no",
        "1": "0",
    }
    # automatically add the reverse of the above items to replacements
    replacements.update([
        reversed(item) for item in replacements.items()
    ])

    def __init__(self, view = None):
        # Called whenever a new instance of this class is required
        self.view = view


    def run(self, edit):
        # Called whenever the command toggle_boolean is run
        current_selections = self.view.sel()
        for selection in current_selections:
            wordreg = self.view.word(selection)
            oldword = self.view.substr(wordreg)
            if oldword in self.replacements:
                newword = self.replacements[oldword]
                self.view.replace(edit, wordreg, newword)
            else:
                sublime.status_message(
                    "ToggleBoolean: Word not recognised: '%s'" % oldword
                )

    def description(self):
        # Used in menus etc
        return "Toggle between boolean values"

