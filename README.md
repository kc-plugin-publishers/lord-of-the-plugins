# lord-of-the-plugins

Download as zip or clone this repo.

Change the .ini file if you want to. Even if you don't want to change it, check there which plugin will be installed and where.

In command line go to the project's directory. Run lord_of_the_plugins_action.py with python 2.

Check the result - the plugin given in the .ini file should now be installed to the given directory.

The script can install itself (and ATM is configured to do so).

The script can update itself. It must of course first be installed manually somewhere and run there. After it has installed itself go to the plugins directory given in the .ini file. Go to this script's directory and run the script. The current working directory is deleted before the files are re-installed and you have to "cd .." and cd there again to see the changes.

See also https://github.com/kc-plugin-publishers/kc-plugins-master-list. There are .plugininfo files which describe installable plugins.
