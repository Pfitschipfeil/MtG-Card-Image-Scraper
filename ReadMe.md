# MtG Card Image Scraper (Python)

This script is supposed to download Magic the Gathering card images from scryfall.com.

1. Run the getMtGImages.py script with Python(3)
2. Enter the Magic the Gathering set name you want to download. Like `grn` for Guilds of Ravnica. [Full List](https://scryfall.com/sets)
3. Enter the image size to download. Values: `small`, `normal`, `large`, `png`, `art_crop`, `border_crop`
4. Enjoy!

> Please respect the guidelines from [Wizards of the Coast](http://gatherer.wizards.com/Pages/CodeOfConduct.aspx) and [scryfall.com](http://scryfall.com/docs/api/images)

FAQ:
- If you running macOS you may get an SSL Error while downloading. You need to execute `Install Certificates.command`.
- When you get an HTTP Error you may have chosen a card set or image size which is not available.