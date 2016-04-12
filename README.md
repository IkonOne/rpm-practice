# rpm-practice
Simply a sandbox I am using to learn to develop rpm packages.

# RPM's

1 [Leafpad](#leafpad)

## Leafpad
Packaging a simple text editor was actually quite complicated.  Figuring out how all of the different files worked together, what environment they were executed in and keeping track of the 10+ naming conventions used in ~4 different files was a deep web of false/incorrect documentation.  I hope you remember how you set your PFX/PREFIX/_prefix/prefix/_PREFIX/_PREFIX_/Etc/_etc/etcetera.

Here are some highlights and mini-rants.

* If you think you are missing a build requirement despite what the docs say, you probably are.
* <3 Mock
* Reliable spec file(read FOSS) documentation is the holy grail.
* The %find_lang spec command is a juiced up version of the find-lang.sh script found in(/usr/lib/rpm/find-lang.sh).  It automagically fills in the first command line parameter for you.  Come on guys, it's not convenience if you don't document it.
* Originally I was writing a fancy shell script that would download the sources for you, clean the directory structure, execute build commands and paint your house.  It turns out I didn't need the paint your house bit...  Stop over-designing.  Dump the commands into a minimal shell script so that your steps are repeatable and only grow the script if it's needed.  You don't need to think about designing a good interface to your shell script when you are trying to track down why your package isn't building.
* I'm ready for more.
