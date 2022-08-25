# *EViews* Package for Sublime Text

EViews language support for [Sublime Text](http://www.sublimetext.com/)

## Features

- Syntax highlighting
- Build system
- Snippets
- Specific support for World Bank developers of MFMOD
	+ MFMOD specific snippets
	+ YAML file based variable glossary generator (based on MFMOD glossary or manually update YAML file)
	+ Mnemonic based symbol indexing (for project wide cross-referencing of model variables)
	+ Climate specific modelling resource repository

## Installation
Currently only manual installation possible.

1. Download `.zip` file of this folder (`clone`)
2. Unzip to a folder named `EViews`
3. Move this folder to the `Packages` directory, which can be opened through the Sublime menu `Preferences --> Browse Packages...`


## Usage

The most powerful feature in Sublime Text is the fuzzy search among different object categories. For example, the shortcut

| `Goto Anything` | `Ctrl` + `P` |
| --- | --- |

displays the *Goto Anything* search bar, providing quick access to any file in the project via a drop-down list that tightens around the target as letters in its name are typed - even if the name is typed incorrectly. The [documentation](https://sublime-text-unofficial-documentation.readthedocs.io/en/latest/file_management/file_navigation.html#goto-anything) elaborates on the various uses of this feature. Navigating to words/variables/lines within a file and across files is massively simplified by this.


### Projects
For greatest coverage of features I recommend working with [Projects](https://sublime-text-unofficial-documentation.readthedocs.io/en/latest/file_management/projects.html) within Sublime. A Sublime *project* is a collection of folders that contain all the resources of a circumscribed project, such as an EViews model. You can open a folder in Sublime using the `Project` menu, or by dragging a folder into an empty Sublime window. This establishes an anonymous project, to which multiple folders can be added.

To save an anonymous project use the menu `Project --> Save Project As...`

To switch between such saved projects use the menu `Project --> Quick Switch Project` or use the shortcut 

| `Quick Switch Project` | `Ctrl` + `Alt` + `P` |
| --- | --- |

### EViews build
The shortcut

| `Build File` | `ctrl` + `B` |
| --- | --- |

from within a .prg file will open EViews and run the program.

This works out of the box provided EViews is installed at `C:\\Program Files\\EViews 12\\EViews12_x64.exe`. If it is not, one has to replace this path with the correct one in the in the file `EViews.sublime-build` inside the EViews package folder.

### Symbols

The package identifies the names of equations, identities, series, !variables, %variables, and other important EViews objects in the source code. Sublime calls them **Symbols**, and keeps track of where they are defined in the code.

Searching for the instance(s) where they are defined is as simple as the shortcut

| `Goto Symbol In Project` | `Ctrl` + `Shift` + `R` |
| --- | --- |

As with *Goto Anything*, this displays a fuzzy search bar, and typing just a few (not necessarily consecutive) letters of the object name quickly displays the desired object, and hitting `Enter` opens the file at the location.

### Command Palette
The shortcut

| `Command Palette` | `Ctrl` + `Shift` + `P` |
| --- | --- |

displays a fuzzy search bar exposing a variety of useful Sublime Text commands, including some specific commands in this package for EViews and MFMOD work.

For example, typing `sptevw` into the *Command Palette* (from within a .prg file) will bring up a list of EViews specific *Snippets*. 

Typing `arthcm` into the *Command Palette* exposes the *Arithmetic* command. It will evaluate simple arithmetic expressions that are subsequently typed into the search bar. Expressions such as `17*7/3`.

### Snippets

Snippets are code fragments that are inserted at the current position of the cursor when the corresponding snippet command is called. 

One way to access snippets is through the *Command Palette* (`ctrl`+`shift`+`p`), by typing `snippet` along with some other letters contained in the description of the snippet. For example, the code snippet used to create a new scenario initiated to the baseline, and solving it (with the user's choice of overrides and excludes) is saved in the package with the description "Snippet: EViews: solve scenario initiated to baseline". So typing any sequence of letters from that description will very soon display exactly that snippet's command at the top of the dropdown list. In my case the input `evscb` was sufficient. Hitting `Enter` will then insert, at the cursor, the code

	{%cty}.scenario(n,a=!i,i="baseline",c) name
	{%cty}.scenario name
	{%cty}.exclude  {%excludelist}
	{%cty}.OVERRIDE {%overridelist}
	smpl %solve_start %fcst_end
	{%cty}.addassign(i,c) @stochastic
	{%cty}.addinit(v=n) @stochastic
	{%cty}.solve(s=d,d=d,o=b,i=a,c=1e-10,v=t,g=n)

The two instances of `name` will be highlighted, so that the programmer can change them by directly typing a better name. Subsequently hitting `tab` will highlight `%solve_start`, and a further `tab` highlights `%solve_end`, in case the programmer uses other phrases for the sample limits and wants to change them quickly.

When a snippet command description is displayed in the dropdown list, the *tab-trigger* is also displayed at the right edge of the dropdown menu. The *tab-trigger* is a short string inserted in the program that gets replaced with the entire code snippet if the programmer hits `tab` right after typing said string. For the snippet above the tab-trigger is the word `scenario`. Type it in the code and hit `tab`, and the snippet created a new scenario will be inserted in its position.

I have had to type `{%cty}` so many times, that the tab-trigger `ct` + `tab` now does the same job. Try it.

Some snippets are merely for convenience (like the one for `{%cty}`). Many other snippets in the package are there for reference. I find that I have to go back to old models to find the exact code needed to do things like creating a new scenario, or solving the model in the historical period, or defining the list of quasi-identities `c_spec_qi`. The package contains a number of such "reference" snippets. This slightly speeds up the process when writing those bits of code. But it also establishes a reference library for those bits of code so that we are all using the same code for the same things. Familiarize yourselves with the snippets called by "Snippet: Eviews: xxx" and "Snippet: MFMOD: yyy". If you solve something in a different way (as I have seen in multiple different variants), lets have a brief discussion on what is better, and we can update this reference. 

There are probably still some mistakes in these, so if you find those, please let me know.

### MFMOD

The package contains some MFMOD specific features. 


