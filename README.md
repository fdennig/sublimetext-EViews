# *EViews* Package for Sublime Text

## How to set up the package
- Save the `EViews` folder into the subfolder of the Sublime Text application called `Data\\Packages\\User`
- If you are using the *Mariana* color scheme, then you are good to go
- If you choose a different color scheme, the following steps will ensure that the color coding treats %variables and !variables correctly
	- If you don't follow these substeps, things will still work, but some concepts might not be colored at all or colored consistently
	- From within Sublime Text, having selected the desired Color Scheme (the `scheme` is important, not the `theme`), hit `ctrl`+`shift`+`P` and type "customize color scheme" and hit enter. 
	- Two files will open side by side, on the left the settings of your color scheme (which you can't edit) and on the right the skeleton for the settings you will override
	- Copy the contents of `Mariana.sublime-color-scheme` into the file on the right
	- The color codes in lines 26, 33, 40, and 46 need to be changed to the colors that are used in the color scheme (file on the left) for the corresponding "scopes". E.g. for the "constant.numeric" scope, simply search that term in the file on the left, identify the color code associated with that scope, and copy that into line 40 on the right.


## Features of the package
- Hitting `ctrl` + `B` from within a .prg file will open EViews and run the program provided EViews is installed at `C:\\Program Files\\EViews 12\\EViews12_x64.exe`
	- If EViews is installed elsewhere, you have to replace the path in the file `EViews.sublime-build`
- Always open the whole folder containing the model (`File` -> `Open Folder`)
- Hitting `ctrl` + `shift` + `R` opens a list of all defined equations (both stochastic and identities) and subroutines in the entire group of files making up the model. You can search this list by typing components of the name you are looking for
	- e.g. if you are looking for the identity `UGANYGDPMKTPKN` I can type "gdpkn" and the list is reduce to a few items, and by choosing `UGANYGDPMKTPKN` among the list you will be taken to the point in the code where the identity corresponding to that variable is defined
	- if there are several instances in which such an identity is defined, you will be presented with a list of such positions amongst which you can choose
	- Incidentally, the identity for `UGANYGDPMKTPKN` is defined twice in the Uganda model, for example. In the 03_equations.prg and 03d_damages.prg. Could someone explain to me how I know which is the definition that gets picked up by the model solver?
	- This works for subroutines, equations and identities. I have not implemented this of the definitions of `series` objects, because given my current understanding of things, those relationships are not the relevant ones to understand the model. But I might be wrong about that, and one can easily add this functionality for `series` or other objects

