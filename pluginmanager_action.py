import pcbnew

class PluginManagerAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Plugin Manager"
        self.category = "Metaplugins"
        self.description = "A plugin manager for installing/removing plugins"
    
    def Run(self):
        # ATM the plugin runs the non-interactive command line interface
        from lord_of_the_plugins_cli import LordOfThePluginsCli
        cli = LordOfThePluginsCli(None)
        cli.Run()
