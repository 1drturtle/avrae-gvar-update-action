
Automatic Avrae GVAR Updating
=============================

> This action automatically pushes GVARS to Avrae that have been pushed to the master branch (with a bit of setup).

Prerequisite
-----------
* Python 3.8.x
* https://avrae.io Account
* Basic File Management/Command Line Knowledge

How to Install
-----------------

For this you will need to do some changes to your repository, as well as acquire GVAR ID's for all the GVARs that you wish to automatically update.

> Important Note, this script will only recognize gvar files that end in `.gvar`

1. Get your Avrae Token. You can do this by going to [the Avrae Website](https://avrae.io) and opening up the developer console. Then, go to Storage, Local Storage, and copy the value of the avrae_token.
	* With your Avrae Token, go to your GitHub Repository and click settings. Then, near the bottom-left click Secrets. Click New Secret and call it `AVRAETOKEN`, and put your token into the value textbox.
2. Make a new folder in your repository called `.github/workflows`. In this folder make a document called `update_workflow.yml`. Paste the contents of the `example-workflow.yml` file (that exists in this repository) into your `update_workflow.yml`
3. In the base of your repository, make a file called `gvar-ids.json`.
    * In your new gvar-ids.json file, you will need to create a dictionary of file paths to GVAR ids. For example:
```json
{
    "gvars/test-gvar.gvar": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```
4. Add these new files to your git repository and push to the `master` branch. The workflow should automatically start running.


Contributing
------------
If you find a bug/issue with anything in this repository, open an issue! If you would like to make a change, open a PR

Further Questions
-----------------
If you have any other questions contact me at the [Avrae Discord](https://support.avrae.io). My username is Dr Turtle#1771.
