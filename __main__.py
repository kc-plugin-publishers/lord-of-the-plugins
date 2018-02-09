# Can be run from command line from the parent directory:
# python -m lord-of-the-plugins #or
# python2 -m lord-of-the-plugins
import os
import sys
currd = os.path.dirname(os.path.abspath(__file__))
configFileName = currd + "/lord_of_the_plugins.ini"
if len(sys.argv) >1:
    configFileName = sys.argv[1]

from lord_of_the_plugins_cli import LordOfThePluginsCli
cli = LordOfThePluginsCli(configFileName)
cli.Run()
