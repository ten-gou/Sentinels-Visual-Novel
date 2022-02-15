# The script of the game goes in this file.

# set ATLs and inits using the init block? here
# flip an image
init:
    transform flip:
        linear 0.1 alpha 0.0
        xzoom -1.0
        linear 0.1 alpha 1.0

# Declare transitions below this line, using the define statement

define enterleft = ComposeTransition(dissolve, after=easeinleft)
define enterright = ComposeTransition(dissolve, after=easeinright)
define entertop = ComposeTransition(dissolve, after=easeintop)
define enterbot = ComposeTransition(dissolve, after=easeinbottom)

# Declare backgrounds below this line, using the image statement.

image bgWhite = "#ffffff"
image bgBlack = "#000000"
image bgRoom = "images/Backgrounds/ROOM.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ros = Character("Ross") # Self
define shi = Character("Shigure") # Fox girl, partner
define tat = Character("Tatsu") # Friend

# Declare character art below this line, using the image statement.

image Ross Casual = "images/Characters/Ross/RossCasual.png"
image Ross Casual Sigh = "images/Characters/Ross/RossCasualSigh.png"
image Ross Formal
image Shigure Casual = "images/Characters/Shigure/ShigureCasual.png"
image Shigure Formal = "images/Characters/Shigure/ShigureFormal.png"

# The game starts here.

label start:

scene bgBlack

centered "......"
centered "...{w=.2} I awoke to the sound of rain."

scene bgRoom with dissolve
play music "audio/Rain Drops.mp3" fadeout 3

"???" "Wake up, you."

show Shigure Casual at left with enterleft


ros "Good morning, Shigure."
shi "It's already past noon, child. More{w=.2} im{w=.2}por{w=.2}tantly,{w=.2}"
"She leans in to stare into my eyes."

# Cutout - Middle - Lean In

shi "Another full moon is upon us. Are we going out tonight?"
ros "Ngh..."

# Exit cutout

"I pull myself off of the bed.{nw}"

show Ross Casual at right with enterright

"You can't see the sky outside, because of the rain, but I can tell that it is already evening."
shi "Well? It has already been a fortnite since we last prowled."

pause 2.0
show Ross Casual Sigh with dissolve

ros "I suppose so. It has been a while, after all."
ros "Just let me get dressed."
shi "Ya- I mean, a most excellent choice."
"Despite her attempts to hide it, a smile crept up on her face. I sigh once more."

show Ross Casual with dissolve

stop music fadeout 3
scene bgBlack with dissolve

centered "It's going to be another long night."

# scene Night Park

show Shigure Formal at left with enterright

shi "Ah, the night air is so relaxing~"

show Shigure Formal at flip

shi "You can even see the stars from here~"
shi "Wouldn't you agree, Ross?"

# show Ross Jacket at right with easeinright 3

"I had to agree; it was nice out tonight."
"Illuminated by the flickering street lamps, the area looked normal- just like everywhere else in the city."
"But something was abrew, beneath the thin veneer of normalcy. You just had to focus your eyes, and then{w=.1}"

# scene Night Park - Spirits in Air

extend " they came into view."

return
