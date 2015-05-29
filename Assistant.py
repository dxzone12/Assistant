import sublime, sublime_plugin

'''
header files will be to the right
source files will be to the left
'''

class AssistantListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        file_name = view.file_name()
        # custome layout name
        layout_pref = "2cols"

        if file_name != None:

            # source file, move header to right, source to left
            if file_name.endswith(".cpp"):
                header = view.window().find_open_file(file_name.replace('.cpp', '.h'))
                if header != None:
                    layout_panes(layout_pref)
                    view.window().set_view_index(header, 1, 0)
                    view.window().set_view_index(view, 0, view.window().get_view_index(view)[1])

            # header file, move header to right, source to left
            if file_name.endswith(".h"):
                source = view.window().find_open_file(file_name.replace('.h', '.cpp'))
                if source != None:
                    layout_panes(layout_pref)
                    view.window().set_view_index(source, 0, 0)
                    view.window().set_view_index(view, 1, view.window().get_view_index(view)[1])

    def layout_panes(layout)
    # add custom layouts here.
        if layout = "2cols":
            view.window().set_layout({"cols": [0, 0.5, 1], "rows": [0, 1], "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]})
        elif layout = "2rows":
            view.window().set_layout({"cols": [0, 1], "rows": [0, 0.5, 1], "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]})
        else:
            # default to 'rows' layout
            view.window().set_layout({"cols": [0, 0.5, 1], "rows": [0, 1], "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]})
