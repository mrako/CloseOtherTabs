import sublime, sublime_plugin

class CloseAllOtherTabsCommand(sublime_plugin.WindowCommand):
  def run(self, edit):
    active_group = window.activeGroup()
    curr_view_id = window.activeViewInGroup(active_group).id()

    for v in window.viewsInGroup(active_group):
        if v.id() == curr_view_id: continue
        window.focusView(v)
        window.runCommand("close")
