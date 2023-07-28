# bumps

This generate bumps, little bits of information between video clips. These were
used in an amazing guerrilla drive-in project in 2006.

thanks brimstone for v1. v2 is garbage and we won't talk about it.
v3 is the one I am currently modifying for use in DragonConTV.

## How to use this (for people who do not know or care what Python is)
### Linux
1. Install Python3, pillow, and git if you don't have them. (Try `sudo apt install python3 python3-pil git`)
    * No harm in doing it even if you already have them installed.
2. In a terminal, type `git clone https://github.com/hfuller/bumps`
    * Now you are ready to use the app. You can start at step 3 next time.
3. Save your script as a .txt file in the `bumps/bump-gen3` folder in your home folder.
4. In a terminal, type `cd bumps/bump-gen3`
5. Now type `python3 frame.py script.txt` (assuming you called your script script.txt).
6. Observe that the image files have magically appeared in the `bumps/bump-gen3` folder.

### Windows
1. Open PowerShell as an administrator.
2. Type `python3 -m PIL` and hit return.
   * If the result is that the Microsoft Store opens to show you the Python app, install it, then start over at step 2.
   * If the result is "No module named PIL", then type `python3 -m pip install pillow` and hit return. Then start over at step 2.
   * If the result is a bunch of lines of text, some of which start with "Features", then type `exit` and hit return, and proceed to step 3.
3. Download this repository (either by using the Download ZIP feature on GitHub and unzipping it, or by `git clone`ing it if you're into that).
    * Now you are ready to use the app. You can start at step 4 next time.
4. Run PowerShell (*not* as an administrator).
5. Type `python3` then press the *space bar*.
6. Drag and drop the "frame.py" file from this GitHub repository into the PowerShell window, then press the *space bar*.
7. Save your script as a .txt file. Drag and drop that file into the PowerShell window, then hit return.
8. Observe that the image files have magically appeared. (They might appear in your home folder, i.e., `C:\Users\Hunter` or whatever).

### macOS
idk lol gl;hf

