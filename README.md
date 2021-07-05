# Forum-Snipe
Code repository for ForumSnipe.com

How It Works
---------------
1. `main.py` contains the script to pull all the information from the designated link
2. You must pass in an url to `ScrappingModule` to fulfil the `link` parameter when calling it.
3. `selling_check` will verify that it is a selling forum located on Net54's forum and then scrape all the needed information from it
4. All the information will then be exported.