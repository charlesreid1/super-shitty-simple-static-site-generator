import sys
import os
import shutil
import markdown
import glob

# Get all the .md files in here, except the fucking readme
mdfile = glob.glob('*.md')
mdfile.remove("Readme.md")

# If the user didn't give us exactly one fucking file,
# they're a complete nitwit who needs hand-holding.
if len(mdfile) != 1:
    print(mdfile)
    msg = f"""
    What the fuck is wrong with you, sport?
    You didn't read the fucking Readme, did you?
    ONE FUCKING FILE. How many do you have? Fucking {len(mdfile)}.
    Go back and read the fucking Readme.
    I'm fucking disappointed in you.
    """
    print(msg)
    sys.exit(1)
else:
    filename = mdfile[0]

# Now read the fucking markdown.
# (Assumes you didn't make a complete shitshow in there.)
with open(filename, 'r') as f:
    text = f.read()
    # This is the fucking money shot.
    html = markdown.markdown(text)
    # Tack it.

# Now take a big HTML dump into that HTML toilet you call a website.
htmlname = 'output/index.html'

try:
    os.remove('output/index.html')
except FileNotFoundError:
    pass
with open(htmlname, 'w') as f:
    f.write(html)

print("Way to go ace, you didn't fuck up counting to 1.")
