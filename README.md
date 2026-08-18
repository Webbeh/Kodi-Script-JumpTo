# Kodi-Script-JumpTo
A script that allows you to navigate directly to the selected letter in a library view.

When calling the script with any letter as an argument, the currently selected view will jump to that letter, if exists.
If you input a digit (or the `#` character), it will jump to the first element of the library including any digit.

## Installation
- Create the `~/.kodi/addons/script.jumpto` directory on your kodi box
- Drop the `addon.xml` and `default.py` files directly inside that newly created folder
- Restart kodi
- Go to your addons and enable the "Jump To Letter" addon.

## Usage
Call the script any way you want (json-rpc, other addon, ...) with whatever letter you want to jump to as argument. 
The navigation will jump to that letter if it exists.
Use `#` or any digit to jump to the titles starting with a number.
