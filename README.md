# *EViews* Package for Sublime Text

EViews language support for [Sublime Text](http://www.sublimetext.com/)

- Syntax highlighting
- Build system
- Snippets
- Specific support for World Bank developers of MFMOD

# Installation
Install [Package Control](https://packagecontrol.io/installation), and select `EViews` from `Package Control: Install Package` list in the Command Palette.

## Features of the package
- Hitting `ctrl` + `B` from within a .prg file will open EViews and run the program provided EViews is installed at `C:\\Program Files\\EViews 12\\EViews12_x64.exe`
	- If EViews is installed elsewhere, you have to replace the path in the file `EViews.sublime-build`
- Always open the whole folder containing the model (`File` -> `Open Folder`)
- Hitting `ctrl` + `shift` + `R` opens a list of all defined equations (both stochastic and identities) and subroutines in the entire group of files making up the model. You can search this list by typing components of the name you are looking for
	- e.g. if you are looking for the identity `UGANYGDPMKTPKN` I can type "gdpkn" and the list is reduce to a few items, and by choosing `UGANYGDPMKTPKN` among the list you will be taken to the point in the code where the identity corresponding to that variable is defined
	- if there are several instances in which such an identity is defined, you will be presented with a list of such positions amongst which you can choose
	- Incidentally, the identity for `UGANYGDPMKTPKN` is defined twice in the Uganda model, for example. In the 03_equations.prg and 03d_damages.prg. Could someone explain to me how I know which is the definition that gets picked up by the model solver?
	- This works for subroutines, equations and identities. I have not implemented this of the definitions of `series` objects, because given my current understanding of things, those relationships are not the relevant ones to understand the model. But I might be wrong about that, and one can easily add this functionality for `series` or other objects

