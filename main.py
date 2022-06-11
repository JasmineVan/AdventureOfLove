@namespace
class SpriteKind:
    Collectable = SpriteKind.create()
    Flowers = SpriteKind.create()
    Bushes = SpriteKind.create()
    Clouds = SpriteKind.create()
    Trees = SpriteKind.create()
    Bounds = SpriteKind.create()
    gates = SpriteKind.create()
    lavas = SpriteKind.create()
    bubs = SpriteKind.create()
def aboutPlay2():
    MyPlayer.say_text("Right/Left + B to blink...and I hate lava...")

def on_b_pressed():
    if currentLevel == 1:
        MyPlayer.say_text("\"Meow\"", 200, False)
    elif currentLevel == 2:
        MyPlayer.say_text("\"Nyan\"", 200, False)
    else:
        catBurst()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap(sprite, otherSprite):
    MyPlayer.say_text("\"U w U\"", 100, False)
sprites.on_overlap(SpriteKind.player, SpriteKind.Bushes, on_on_overlap)

def on_a_pressed():
    if MyPlayer.vy == 0:
        MyPlayer.vy = -90
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite2, location):
    game.over(False, effects.melt)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile)

def startLevel1():
    global Coins, Flowers2, Cloud, gate
    scene.set_background_color(13)
    scene.set_background_image(img("""
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddd33dddddddddddddddddddddddddddddddddddddd33dddddddddddddddddddddddddddddddddddddd33dddddddddddddddddddddddddddddddddddddd33dddddddddddddddd
                ddddddddddddddddddddddd3ddddddddddddddddddddddddddddddddddddddd3ddddddddddddddddddddddddddddddddddddddd3ddddddddddddddddddddddddddddddddddddddd3dddddddddddddddd
                ddddddddddddddddddddd3333dddddddddddddddddddddddddddddddddddd3333dddddddddddddddddddddddddddddddddddd3333dddddddddddddddddddddddddddddddddddd3333ddddddddddddddd
                dddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddd
                ddddddddddddddddddd3333333ddddddddddddddddddddddddddddddddd3333333ddddddddddddddddddddddddddddddddd3333333ddddddddddddddddddddddddddddddddd3333333dddddddddddddd
                ddddddddddddddddddd33333d3ddddddddddddddddddddddddddddddddd33333d3ddddddddddddddddddddddddddddddddd33333d3ddddddddddddddddddddddddddddddddd33333d3dddddddddddddd
                ddddddddddddbddddddd3333ddddddddddddddddddddddddddddbddddddd3333ddddddddddddddddddddddddddddbddddddd3333ddddddddddddddddddddddddddddbddddddd3333dddddddddddddddd
                ddddddddddddbdddddd3333333ddddddddddddddddddddddddddbdddddd3333333ddddddddddddddddddddddddddbdddddd3333333ddddddddddddddddddddddddddbdddddd3333333dddddddddddddd
                ddddddddddddbddddd33333333ddddddddddddddddddddddddddbddddd33333333ddddddddddddddddddddddddddbddddd33333333ddddddddddddddddddddddddddbddddd33333333dddddddddddddd
                ddddddddddddbdddd33333333333ddddddddddddddddddddddddbdddd33333333333ddddddddddddddddddddddddbdddd33333333333ddddddddddddddddddddddddbdddd33333333333dddddddddddd
                dd33ddddddddbdd3d3333333333333ddddbddddddd33ddddddddbdd3d3333333333333ddddbddddddd33ddddddddbdd3d3333333333333ddddbddddddd33ddddddddbdd3d3333333333333ddddbddddd
                d33333ddddddbdd333333333333333ddddbdddddd33333ddddddbdd333333333333333ddddbdddddd33333ddddddbdd333333333333333ddddbdddddd33333ddddddbdd333333333333333ddddbddddd
                33333333ddddbddd33333333333333ddddbddddd33333333ddddbddd33333333333333ddddbddddd33333333ddddbddd33333333333333ddddbddddd33333333ddddbddd33333333333333ddddbddddd
                333333333ddddbdddd333333333333ddddbddddd333333333ddddbdddd333333333333ddddbddddd333333333ddddbdddd333333333333ddddbddddd333333333ddddbdddd333333333333ddddbddddd
                d33333333dddddbdddd3333333444444dbbdddd3d33333333dddddbdddd3333333444444dbbdddd3d33333333dddddbdddd3333333444444dbbdddd3d33333333dddddbdddd3333333444444dbbdddd3
                d333333333dddddbb3333333444444444bdddd3dd333333333dddddbb3333333444444444bdddd3dd333333333dddddbb3333333444444444bdddd3dd333333333dddddbb3333333444444444bdddd3d
                33333333ddddddddbb33333333443443bbdddddd33333333ddddddddbb33333333443443bbdddddd33333333ddddddddbb33333333443443bbdddddd33333333ddddddddbb33333333443443bbdddddd
                333333333dddddd333b333333343334bb3ddddd3333333333dddddd333b333333343334bb3ddddd3333333333dddddd333b333333343334bb3ddddd3333333333dddddd333b333333343334bb3ddddd3
                3333b33dddddd33333333333333333bbdddddd333333b33dddddd33333333333333333bbdddddd333333b33dddddd33333333333333333bbdddddd333333b33dddddd33333333333333333bbdddddd33
                3333b3333ddddd333333333333333bbddddddd333333b3333ddddd333333333333333bbddddddd333333b3333ddddd333333333333333bbddddddd333333b3333ddddd333333333333333bbddddddd33
                3333b33b33dddddd333344444333333ddddddd333333b33b33dddddd333344444333333ddddddd333333b33b33dddddd333344444333333ddddddd333333b33b33dddddd333344444333333ddddddd33
                3333b33b33ddddd34444444444333333333ddd333333b33b33ddddd34444444444333333333ddd333333b33b33ddddd34444444444333333333ddd333333b33b33ddddd34444444444333333333ddd33
                3333b3b333dddd444444444443344433333ddd333333b3b333dddd444444444443344433333ddd333333b3b333dddd444444444443344433333ddd333333b3b333dddd444444444443344433333ddd33
                3333bbb3443d3334444444444443444333ddddd33333bbb3443d3334444444444443444333ddddd33333bbb3443d3334444444444443444333ddddd33333bbb3443d3334444444444443444333ddddd3
                3333bb3443334444444444444444344433dddd333333bb3443334444444444444444344433dddd333333bb3443334444444444444444344433dddd333333bb3443334444444444444444344433dddd33
                333bb33333444444444444444444433333333333333bb33333444444444444444444433333333333333bb33333444444444444444444433333333333333bb33333444444444444444444433333333333
                33bb333344444444444444443bb333333333b33333bb333344444444444444443bb333333333b33333bb333344444444444444443bb333333333b33333bb333344444444444444443bb333333333b333
                33b3333433334443443443443bb333443333b33333b3333433334443443443443bb333443333b33333b3333433334443443443443bb333443333b33333b3333433334443443443443bb333443333b333
                33b3b33333344434433444333bb333b44333b33333b3b33333344434433444333bb333b44333b33333b3b33333344434433444333bb333b44333b33333b3b33333344434433444333bb333b44333b333
                3bb3b33333343334333334333bb333b33333b3333bb3b33333343334333334333bb333b33333b3333bb3b33333343334333334333bb333b33333b3333bb3b33333343334333334333bb333b33333b333
                3bbbb33333333433344333333bb333b333333b333bbbb33333333433344333333bb333b333333b333bbbb33333333433344333333bb333b333333b333bbbb33333333433344333333bb333b333333b33
                3bbb333333334433443333333bb333b333333b333bbb333333334433443333333bb333b333333b333bbb333333334433443333333bb333b333333b333bbb333333334433443333333bb333b333333b33
                3b333333333343333333b3333bb33b3333333bbb3b333333333343333333b3333bb33b3333333bbb3b333333333343333333b3333bb33b3333333bbb3b333333333343333333b3333bb33b3333333bbb
                bb333333333333333333b3333bbb3b333333333bbb333333333333333333b3333bbb3b333333333bbb333333333333333333b3333bbb3b333333333bbb333333333333333333b3333bbb3b333333333b
                3b333333333333333333b3333bbbb333333333333b333333333333333333b3333bbbb333333333333b333333333333333333b3333bbbb333333333333b333333333333333333b3333bbbb33333333333
                3b333333333333333333b3333bbbb333444333333b333333333333333333b3333bbbb333444333333b333333333333333333b3333bbbb333444333333b333333333333333333b3333bbbb33344433333
                3b444334443333333333b3333bbb3334443333333b444334443333333333b3333bbb3334443333333b444334443333333333b3333bbb3334443333333b444334443333333333b3333bbb333444333333
                44444433444333333333b3333bbb33444334444444444433444333333333b3333bbb33444334444444444433444333333333b3333bbb33444334444444444433444333333333b3333bbb334443344444
                44443333b44433333333b3333bbb33333444444444443333b44433333333b3333bbb33333444444444443333b44433333333b3333bbb33333444444444443333b44433333333b3333bbb333334444444
                44444443b33333333b33b3333bbb33334444444444444443b33333333b33b3333bbb33334444444444444443b33333333b33b3333bbb33334444444444444443b33333333b33b3333bbb333344444444
                44444444443333333b33b3333bbbb3444434444444444444443333333b33b3333bbbb3444434444444444444443333333b33b3333bbbb3444434444444444444443333333b33b3333bbbb34444344444
                44444344443333333b33b3333bbb4444b433443444444344443333333b33b3333bbb4444b433443444444344443333333b33b3333bbb4444b433443444444344443333333b33b3333bbb4444b4334434
                3444333bb3bb33333b33b3333bbbb444b33443333444333bb3bb33333b33b3333bbbb444b33443333444333bb3bb33333b33b3333bbbb444b33443333444333bb3bb33333b33b3333bbbb444b3344333
                33b4333bb3b333333bb3bb333bbbb333bb33333333b4333bb3b333333bb3bb333bbbb333bb33333333b4333bb3b333333bb3bb333bbbb333bb33333333b4333bb3b333333bb3bb333bbbb333bb333333
                33b3333bbbb3333333bbbb333bbbb333bb33333333b3333bbbb3333333bbbb333bbbb333bb33333333b3333bbbb3333333bbbb333bbbb333bb33333333b3333bbbb3333333bbbb333bbbb333bb333333
                33b3333bb3333333333bbb333bbbb333bb33333333b3333bb3333333333bbb333bbbb333bb33333333b3333bb3333333333bbb333bbbb333bb33333333b3333bb3333333333bbb333bbbb333bb333333
                33b3333bb33333333333bbb33bbbb333bb33333333b3333bb33333333333bbb33bbbb333bb33333333b3333bb33333333333bbb33bbbb333bb33333333b3333bb33333333333bbb33bbbb333bb333333
                333b333bb33333333333bbb33bbbb333bb333333333b333bb33333333333bbb33bbbb333bb333333333b333bb33333333333bbb33bbbb333bb333333333b333bb33333333333bbb33bbbb333bb333333
                333bb3bbb3333443444334b33bbbb333bb33b333333bb3bbb3333443444334b33bbbb333bb33b333333bb3bbb3333443444334b33bbbb333bb33b333333bb3bbb3333443444334b33bbbb333bb33b333
                333bbbbbb3334444444444443bbbbb33bb33b333333bbbbbb3334444444444443bbbbb33bb33b333333bbbbbb3334444444444443bbbbb33bb33b333333bbbbbb3334444444444443bbbbb33bb33b333
                3333bbbbb334444444444444bbbbbb3bb33bb3333333bbbbb334444444444444bbbbbb3bb33bb3333333bbbbb334444444444444bbbbbb3bb33bb3333333bbbbb334444444444444bbbbbb3bb33bb333
                33333bbbb333443444444434bbbbbb3bb33b333333333bbbb333443444444434bbbbbb3bb33b333333333bbbb333443444444434bbbbbb3bb33b333333333bbbb333443444444434bbbbbb3bb33b3333
                33333bbb3344334444443433bbbbbb3bb3b3333333333bbb3344334444443433bbbbbb3bb3b3333333333bbb3344334444443433bbbbbb3bb3b3333333333bbb3344334444443433bbbbbb3bb3b33333
                33333bbb3333344334433433bbbbbb3bbb33333333333bbb3333344334433433bbbbbb3bbb33333333333bbb3333344334433433bbbbbb3bbb33333333333bbb3333344334433433bbbbbb3bbb333333
                33333bbb333b3433333333333bbbbbbb3333333333333bbb333b3433333333333bbbbbbb3333333333333bbb333b3433333333333bbbbbbb3333333333333bbb333b3433333333333bbbbbbb33333333
                33333bbb333b3333333333333bbbbbbb3333333333333bbb333b3333333333333bbbbbbb3333333333333bbb333b3333333333333bbbbbbb3333333333333bbb333b3333333333333bbbbbbb33333333
                33333bbb333b3b33333333333bbbbbbb3333333333333bbb333b3b33333333333bbbbbbb3333333333333bbb333b3b33333333333bbbbbbb3333333333333bbb333b3b33333333333bbbbbbb33333333
                33333bbb333b3b33333333333bbbbbb33333333333333bbb333b3b33333333333bbbbbb33333333333333bbb333b3b33333333333bbbbbb33333333333333bbb333b3b33333333333bbbbbb333333333
                33333bbb333b3b33333333333bbbbb333333333333333bbb333b3b33333333333bbbbb333333333333333bbb333b3b33333333333bbbbb333333333333333bbb333b3b33333333333bbbbb3333333333
                33333bb3333bbb33333333333bbbbb333333333333333bb3333bbb33333333333bbbbb333333333333333bb3333bbb33333333333bbbbb333333333333333bb3333bbb33333333333bbbbb3333333333
                33333bb333bbb333333333333bbbbb333333333333333bb333bbb333333333333bbbbb333333333333333bb333bbb333333333333bbbbb333333333333333bb333bbb333333333333bbbbb3333333333
                3333bbb333b333333333dd333bbbbb3d333333333333bbb333b333333333dd333bbbbb3d333333333333bbb333b333333333dd333bbbbb3d333333333333bbb333b333333333dd333bbbbb3d33333333
                3333bbb333b3333333333dd3bbbbbb33dd3333d33333bbb333b3333333333dd3bbbbbb33dd3333d33333bbb333b3333333333dd3bbbbbb33dd3333d33333bbb333b3333333333dd3bbbbbb33dd3333d3
                3333bbb3bbb3333333333333bbbbbbb33d333dd33333bbb3bbb3333333333333bbbbbbb33d333dd33333bbb3bbb3333333333333bbbbbbb33d333dd33333bbb3bbb3333333333333bbbbbbb33d333dd3
                dd33bbbbbb33333333d33333bbbbbbb333333d33dd33bbbbbb33333333d33333bbbbbbb333333d33dd33bbbbbb33333333d33333bbbbbbb333333d33dd33bbbbbb33333333d33333bbbbbbb333333d33
                3dd3bbbbb33dd3333dd3333dbbbbbbbd333333333dd3bbbbb33dd3333dd3333dbbbbbbbd333333333dd3bbbbb33dd3333dd3333dbbbbbbbd333333333dd3bbbbb33dd3333dd3333dbbbbbbbd33333333
                3dddbbbbb333dd33dd33d3ddbbbbbbbd333d33333dddbbbbb333dd33dd33d3ddbbbbbbbd333d33333dddbbbbb333dd33dd33d3ddbbbbbbbd333d33333dddbbbbb333dd33dd33d3ddbbbbbbbd333d3333
                3dddbbb333333333d33dddddbbbbbbbdd3dd33d33dddbbb333333333d33dddddbbbbbbbdd3dd33d33dddbbb333333333d33dddddbbbbbbbdd3dd33d33dddbbb333333333d33dddddbbbbbbbdd3dd33d3
                ddddbbbd33333333333dddddbbbbbbbdddd33dddddddbbbd33333333333dddddbbbbbbbdddd33dddddddbbbd33333333333dddddbbbbbbbdddd33dddddddbbbd33333333333dddddbbbbbbbdddd33ddd
                ddddbbbd333d33ddd33dddddbbbbbbbdddddddddddddbbbd333d33ddd33dddddbbbbbbbdddddddddddddbbbd333d33ddd33dddddbbbbbbbdddddddddddddbbbd333d33ddd33dddddbbbbbbbddddddddd
                ddddbbbd33ddd3dddd3dddddbbbbbbbdddddddddddddbbbd33ddd3dddd3dddddbbbbbbbdddddddddddddbbbd33ddd3dddd3dddddbbbbbbbdddddddddddddbbbd33ddd3dddd3dddddbbbbbbbddddddddd
                ddddbbbdddddddddddddddddbbbbbbbdddddddddddddbbbdddddddddddddddddbbbbbbbdddddddddddddbbbdddddddddddddddddbbbbbbbdddddddddddddbbbdddddddddddddddddbbbbbbbddddddddd
                ddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbddddddddd
                ddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbdddddddddddddbbb3ddddddddddddddddbbbbbbbddddddddd
                ddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbddddddddd
                ddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbddddddddd
                ddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbdddddddddddddbbbbddddddddddddddddbbbbbbbddddddddd
                ddddbbbb3dddddddddddddddbbbbbbbdddddddddddddbbbb3dddddddddddddddbbbbbbbdddddddddddddbbbb3dddddddddddddddbbbbbbbdddddddddddddbbbb3dddddddddddddddbbbbbbbddddddddd
                ddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbddddddddd
                ddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbdddddddddddddbbbbbdddddddddddddddbbbbbbbddddddddd
                ddddbbbbb3ddddddddddddd3bbbbbbb3ddddddddddddbbbbb3ddddddddddddd3bbbbbbb3ddddddddddddbbbbb3ddddddddddddd3bbbbbbb3ddddddddddddbbbbb3ddddddddddddd3bbbbbbb3dddddddd
                ddddbbbbb3dddddddddddddbbbbbbbb3ddddddddddddbbbbb3dddddddddddddbbbbbbbb3ddddddddddddbbbbb3dddddddddddddbbbbbbbb3ddddddddddddbbbbb3dddddddddddddbbbbbbbb3dddddddd
                ddd3bbbbbbdddddddddddddbbbbbbbbbddddddddddd3bbbbbbdddddddddddddbbbbbbbbbddddddddddd3bbbbbbdddddddddddddbbbbbbbbbddddddddddd3bbbbbbdddddddddddddbbbbbbbbbdddddddd
                ddd3bbbbbbdddddddddddd3bbbbbbbbbddddddddddd3bbbbbbdddddddddddd3bbbbbbbbbddddddddddd3bbbbbbdddddddddddd3bbbbbbbbbddddddddddd3bbbbbbdddddddddddd3bbbbbbbbbdddddddd
                443bbbbbbb3dddddddddddbbbbbbbb4444444444443bbbbbbb3dddddddddddbbbbbbbb4444444444443bbbbbbb3dddddddddddbbbbbbbb4444444444443bbbbbbb3dddddddddddbbbbbbbb4444444444
                44444444bbbddddddddd33bbb44444444444444444444444bbbddddddddd33bbb44444444444444444444444bbbddddddddd33bbb44444444444444444444444bbbddddddddd33bbb444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
    """))
    tiles.set_current_tilemap(tilemap("""
        level1
    """))
    MyPlayer.ay = 100
    tiles.place_on_random_tile(MyPlayer, assets.tile("""
        myTile3
    """))
    for value in tiles.get_tiles_by_type(assets.tile("""
        myTile3
    """)):
        tiles.set_tile_at(value, assets.tile("""
            transparency16
        """))
    scene.camera_follow_sprite(MyPlayer)
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        CoinSpawn
    """)):
        Coins = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . f f f f f f f . . . . 
                            . . . . f 5 5 5 5 5 5 5 f . . . 
                            . . . f 5 4 4 4 4 4 5 5 5 f . . 
                            . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 4 f . 
                            . . . f 5 5 4 5 5 5 5 5 4 f . . 
                            . . . . f 5 5 5 5 5 5 4 f . . . 
                            . . . . . f f f f f f f . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Collectable)
        animation.run_image_animation(Coins,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . f 5 4 4 4 4 5 5 5 5 f . . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 4 5 5 5 5 5 5 4 f . . 
                                . . f 5 5 5 5 5 5 5 5 4 f . . . 
                                . . . f 5 5 5 5 5 5 4 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f . . . . . . 
                                . . . . f 5 5 5 5 5 f . . . . . 
                                . . . f 5 4 4 4 5 5 5 f . . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 4 f . . . 
                                . . . f 5 5 5 5 5 5 4 f . . . . 
                                . . . . f 5 5 5 5 4 f . . . . . 
                                . . . . . f f f f f . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . f 5 5 5 f . . . . . . 
                                . . . . f 5 4 4 5 5 f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 4 f . . . . 
                                . . . . f 5 5 5 5 4 f . . . . . 
                                . . . . . f 5 5 4 f . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . f 5 4 5 f . . . . . . 
                                . . . . f 5 5 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 4 f . . . . . 
                                . . . . . f 5 5 4 f . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 4 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . f 5 4 5 f . . . . . . 
                                . . . . f 5 5 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 4 f . . . . . 
                                . . . . . f 5 5 4 f . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . f 5 5 5 f . . . . . . 
                                . . . . f 5 4 4 5 5 f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 4 f . . . . 
                                . . . . f 5 5 5 5 4 f . . . . . 
                                . . . . . f 5 5 4 f . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f . . . . . . 
                                . . . . f 5 5 5 5 5 f . . . . . 
                                . . . f 5 4 4 4 5 5 5 f . . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 4 f . . . 
                                . . . f 5 5 5 5 5 5 4 f . . . . 
                                . . . . f 5 5 5 5 4 f . . . . . 
                                . . . . . f f f f f . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . f 5 4 4 4 4 5 5 5 5 f . . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 4 5 5 5 5 5 5 4 f . . 
                                . . f 5 5 5 5 5 5 5 5 4 f . . . 
                                . . . f 5 5 5 5 5 5 4 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            500,
            True)
        tiles.place_on_tile(Coins, value2)
        tiles.set_tile_at(value2, assets.tile("""
            transparency16
        """))
    for value3 in tiles.get_tiles_by_type(sprites.swamp.swamp_tile0):
        Flowers2 = sprites.create(img("""
                ....................
                            ....................
                            ....................
                            ....................
                            ....................
                            ....................
                            ....................
                            ...........444......
                            ..........4eee4.....
                            ..........44444.....
                            ...........444......
                            .....444....7.......
                            ....4eee4...7.......
                            ....44444..77.7.....
                            .....444...7766.....
                            ......7....766......
                            .......7...76.......
                            .....7777..7........
                            ......6667.6........
                            .........666........
            """),
            SpriteKind.Flowers)
        animation.run_image_animation(Flowers2,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . 4 4 4 . . 
                                . . . . . . . . . . 4 e e e 4 . 
                                . . . . . . . . . . 4 4 4 4 4 . 
                                . . . . . . . . . . . 4 4 4 . . 
                                . . . . . 4 4 4 . . . . 7 . . . 
                                . . . . 4 e e e 4 . . . 7 . . . 
                                . . . . 4 4 4 4 4 . . 7 7 . 7 . 
                                . . . . . 4 4 4 . . . 7 7 6 6 . 
                                . . . . . . 7 . . . . 7 6 6 . . 
                                . . . . . . . 7 . . . 7 6 . . . 
                                . . . . . 7 7 7 7 . . 7 . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . 4 4 4 . 
                                . . . . . . . . . . . 4 e e e 4 
                                . . . . . . . . . . . 4 4 4 4 4 
                                . . . . 4 4 4 . . . . . 4 4 4 . 
                                . . . 4 e e e 4 . . . . . 7 . . 
                                . . . 4 4 4 4 4 . . . . . 7 . . 
                                . . . . 4 4 4 . . . . . 7 7 . 7 
                                . . . . . 7 . . . . . . 7 7 6 6 
                                . . . . . . 7 . . . . . 7 6 6 . 
                                . . . . . . . 7 . . . . 7 6 . . 
                                . . . . . 7 7 7 7 . . 7 . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . 4 4 4 . . 
                                . . . . . . . . . . 4 e e e 4 . 
                                . . . . . . . . . . 4 4 4 4 4 . 
                                . . . . . . 4 4 4 . . 4 4 4 . . 
                                . . . . . 4 e e e 4 . . 7 . . . 
                                . . . . . 4 4 4 4 4 . . 7 . . . 
                                . . . . . . 4 4 4 . . . 7 7 . 7 
                                . . . . . . . 7 . . . . 7 7 6 6 
                                . . . . . . 7 . . . . . 7 6 6 . 
                                . . . . . . . 7 . . . . 7 6 . . 
                                . . . . . 7 7 7 7 . . 7 . . . .
                """)],
            500,
            True)
        tiles.place_on_tile(Flowers2, value3)
    for value4 in tiles.get_tiles_by_type(assets.tile("""
        FlowerPlaceHolder
    """)):
        Cloud = sprites.create(img("""
                ....................
                            ....................
                            ....................
                            ....................
                            ....................
                            .........1..........
                            ......661d1.........
                            .....177717766......
                            ....1d177777677.....
                            ..6.717777c77177....
                            ...7c77767771d17....
                            ...77677766771777...
                            ..1777766677777767..
                            .1d1776717676777c7..
                            .7177661d176777777..
                            .77767771777777176..
                            .677c77777c7671d17..
                            .77777777777767176..
                            .667776776777777767.
                            ...76776766676766...
            """),
            SpriteKind.Bushes)
        tiles.place_on_tile(Cloud, value4)
        tiles.set_tile_at(value4, assets.tile("""
            transparency16
        """))
    for value5 in tiles.get_tiles_by_type(assets.tile("""
        CloudPlaceHolder
    """)):
        Cloud = sprites.create(assets.image("""
            cloud
        """), SpriteKind.Clouds)
        animation.run_image_animation(Cloud,
            [img("""
                    .........bbbb...........
                                .......bb1111bb.........
                                ......bb111111bbbbb.....
                                ......b1111111ddd11b....
                                ......b11111111d1111b...
                                ...bbbd11111111d1111b...
                                ..b11111111111111111bb..
                                .b11111111111111111d11b.
                                .b111d11111111111111111b
                                cdd1d111111111111111111c
                                cdddd11111111111111111dc
                                cddbd11111d11111dd111dc.
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bb.........
                                ......b1111111bbbbb.....
                                ......b1111111ddd11b....
                                ...bbbd11111111d1111b...
                                ..b111111111111d1111b...
                                .b111111111111111111bb..
                                .b111d1111111111111d11b.
                                cdd1d111111111111111111b
                                cdddd111111111111111111b
                                cddbd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ...bb.b1111111dd1111b...
                                ..b11bd11111111d1111b...
                                .b111111111111111111bb..
                                .b111d1111111111111d11b.
                                cdd1d111111111111111111b
                                cdddd111111111111111111b
                                cddbd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ......b1111111dd1111b...
                                ...bb.d11111111d1111b...
                                ..b11b11111111111111bb..
                                .b11111111111111111d11b.
                                .b111d11111111111111111b
                                cdd1d111111111111111111b
                                cdddd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ......b1111111dd1111b...
                                ...bb.d11111111d1111b...
                                ..b11b11111111111111bb..
                                .b11111111111111111d11b.
                                .b111d11111111111111111b
                                cdd1d111111111111111111b
                                ccbbdd111dddd11ddbdddccb
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                                ........................
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ......b1111111dd1111b...
                                ...bb.d11111111d1111b...
                                ..b11b11111111111111bb..
                                .b11111111111111111d11b.
                                .b111d11111111111111111b
                                cdd1d111111111111111111b
                                cdddd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ...bb.b1111111dd1111b...
                                ..b11bd11111111d1111b...
                                .b111111111111111111bb..
                                .b111d1111111111111d11b.
                                cdd1d111111111111111111b
                                cdddd111111111111111111b
                                cddbd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """)],
            500,
            True)
        tiles.place_on_tile(Cloud, value5)
        tiles.set_tile_at(value5, assets.tile("""
            transparency16
        """))
    for value6 in tiles.get_tiles_by_type(sprites.dungeon.collectible_insignia):
        gate = sprites.create(assets.image("""
            Cloud1
        """), SpriteKind.gates)
        animation.run_image_animation(gate, assets.animation("""
            gateMovement
        """), 500, True)
        tiles.place_on_tile(gate, value6)
    aboutPlay()
def aboutPlay():
    MyPlayer.say_text("press A to jump, B to use skill, meow")
def lv1Talk():
    story.print_character_text("Hello Stranger!", "")
    story.print_character_text("My name is Luv, meow...", "")
    story.print_character_text("Can you help me find my way home...", "")

def on_overlap_tile2(sprite3, location2):
    game.over(True, effects.hearts)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile2)

def playerSetup():
    global MyPlayer
    MyPlayer = sprites.create(assets.image("""
        KingCat
    """), SpriteKind.player)
    controller.move_sprite(MyPlayer, 100, 0)
def aboutMushroom():
    MyPlayer.say_text("Jumping on those mushroom to avoid the acid, stranger!")
def catBurst():
    if characterAnimations.matches_rule(MyPlayer, characterAnimations.rule(Predicate.MOVING_RIGHT)):
        MyPlayer.say_text("Cat's Burst!!", 200, False)
        music.magic_wand.play()
        MyPlayer.start_effect(effects.halo, 500)
        MyPlayer.x += 50
    elif characterAnimations.matches_rule(MyPlayer, characterAnimations.rule(Predicate.MOVING_LEFT)):
        MyPlayer.say_text("Cat's Burst!!", 200, False)
        music.magic_wand.play()
        MyPlayer.start_effect(effects.halo, 500)
        MyPlayer.x += -50
    else:
        MyPlayer.say_text("\"Grr\"", 200, False)
def startLevel2():
    global Coins, Tree, Cloud, Bound, gate, bub
    sprites.destroy_all_sprites_of_kind(SpriteKind.Collectable)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Flowers)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Bushes)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Clouds)
    sprites.destroy_all_sprites_of_kind(SpriteKind.gates)
    scene.set_background_color(9)
    scene.set_background_image(img("""
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7776677777777767777777777777777777777777777667777777776777777777777777777777777777766777777777677777777777777777777777777776677777777767777777777777777777777777
                7666777777777667777777777777777777777767766677777777766777777777777777777777776776667777777776677777777777777777777777677666777777777667777777777777777777777767
                7767766777667766777766777777777777777766776776677766776677776677777777777777776677677667776677667777667777777777777777667767766777667766777766777777777777777766
                6666667767766766776766777777777777776676666666776776676677676677777777777777667666666677677667667767667777777777777766766666667767766766776766777777777777776676
                6666677766766666766667777777777777666677666667776676666676666777777777777766667766666777667666667666677777777777776666776666677766766666766667777777777777666677
                6666676666666676666677767777776667776667666667666666667666667776777777666777666766666766666666766666777677777766677766676666676666666676666677767777776667776667
                6666666666666776677666667766677766777666666666666666677667766666776667776677766666666666666667766776666677666777667776666666666666666776677666667766677766777666
                6666666666666766667766677677667766666666666666666666676666776667767766776666666666666666666667666677666776776677666666666666666666666766667766677677667766666666
                66b666666666666666666667667776676666666666b666666666666666666667667776676666666666b666666666666666666667667776676666666666b6666666666666666666676677766766666666
                66b6666666666666666666666b6776666666666666b6666666666666666666666b6776666666666666b6666666666666666666666b6776666666666666b6666666666666666666666b67766666666666
                66b6666666666666666666666bb676666666666666b6666666666666666666666bb676666666666666b6666666666666666666666bb676666666666666b6666666666666666666666bb6766666666666
                66b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb666666666666
                66b66666699dbb666666dd9666bb66666666666666b666666999bb666666999666bb66666666666666b666666999bb666666999666bb66666666666666b666666999bb666666999666bb666666666666
                6bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb6666666666666bb6669669966bbb69666d9966bb666666666666
                6bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb666666666666bb666d96696d9bbb9966d9966bbb66666666666
                6bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb666666666666bb66dd9999d996bb99ddd96666bb66666666666
                bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666bbb666d9999d996bb99dd99669dbbb6696666666
                bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666bbbdd6d9999d999bbb9dd999996bbb6699966666
                bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666bbb6ddd9999d9999bb9dd9999d6bbb9699666666
                bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966bbb6ddd999d99999bbbdd9999d9bbb9999669966
                bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996bbbdddd999d999999bbdd9999d9bbbb9999d9996
                bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999bb9dddd99dd9999999bb9999dd9bbbb9999d9999
                bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999bb99ddddd999999999bbb999d999bbb9999d9999
                bb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999bbb99dddd9999999999dbbbbdd999bbb9999d999b
                bb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999bbb99ddd99999999999ddbbbb9999bbbb999d999b
                bb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999bbb99ddd99999999999ddbbbbbb99bbbb999d999b
                b9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99bb9999dd9999999999ddddbbbbbbbbbbbb999d99b
                b9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99bb9999ddd999999999dd99999bbbbbbbbb999d99b
                b9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bbb9999dddd99999999dd999999bbbbbbbb999d9bb
                b9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbbb9999ddddd999999ddd9999999bbbbbbb999dbbb
                dd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbbdd99999ddddd9999ddd999999999bbbbb999bbbb
                9d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb99d99999ddddddd9ddd9999999999bbbbb99bbbb9
                9d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb999d999999dddddddddd9999999999bbbbb99bbb99
                9d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb9999d999999ddddddddd99999999999bbbbb99bb999
                9dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd999dd99999ddddddd9999999999999bbbbb99bbd99
                99dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd9999dd9999dddddd99999999999999bbbbb99bbd99
                99ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd999ddd999dddddd99999999999999bbbbb9bbbdd9
                9999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d99999dddddddddd9999999999999bbbbbb9bbb9d9
                9999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d99999dddddddddd9999999999999bbbbbbbbb99d9
                999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd999999dddddddd9999999999999bbbbbbbbb99dd
                d9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999dd9999999dddddd999999999999bbbbbbbbb9999d
                dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999dd9999999ddddd999999999999bbbbbbbbb99999
                dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999dd9999999ddddd999999999999bbbbbbbb999999
                9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
                9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
                9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
                9d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb9999999d9999999ddddd99999999999bbbbbbbbb999999
                9dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb9999999
                9dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb99999999dd999999ddddd99999999999bbbbbbbb9999999
                ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999ddd999999ddddd99999999999bbbbbbbb9999999
                dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999dd9999999ddddd99999999999bbbbbbbb9999999
                dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999
                dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999dd9999999dddddd9999999999bbbbbbbb9999999
                dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999dd9999999dddddd9999999999bbbbbbb99999999
                d99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999dd99999999dddddd9999999999bbbbbbb9999999d
                d99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999dd
                d99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999ddd99999999dddddd9999999999bbbbbbb999999dd
                999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
                999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
                999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd999999999ddddddd999999999bbbbbbb99999ddd
                999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd
                999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd999999999dddddddd99999999bbbbbbb9999dddd
                999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9999999999dddddddd99999999bbbbbbb9999ddd9
                9999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd99999999999dddddddd999999bbbbbbbb9999ddd9
                d999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbddddddddd999999999dddddddd999999bbbbbbbbdddddddd
                ddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbdddddddddddd99999dddddddd999999bbbbbbbbbddddddd
                dddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddddddddddd99ddddddddd999ddbbbbbbbbbddddddd
                ddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbdddddddddddddddddddddddddd9ddddbbbbbbbbbddddddd
                ddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbdddddd
                ddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbdddddd
                dddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbdddddd
                dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
                dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
                dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
                dddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddddddddddddddddddddddddddbbbbbbbbbbbbddddd
                ddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbdddddddddddddddddddddddd7777777777bbbbbbddddd
                dddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddddddddddddddddd77777777777777777777bddddd
                ddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777ddddddddddddddd7777777777777777777777777dddd
                dddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dddddddddd777777777777777777777777777777dd
                ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777ddddd77777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    """))
    tiles.set_current_tilemap(tilemap("""
        level0
    """))
    MyPlayer.ay = 100
    tiles.place_on_random_tile(MyPlayer, assets.tile("""
        myTile3
    """))
    for value7 in tiles.get_tiles_by_type(assets.tile("""
        myTile3
    """)):
        tiles.set_tile_at(value7, assets.tile("""
            transparency16
        """))
    scene.camera_follow_sprite(MyPlayer)
    for value8 in tiles.get_tiles_by_type(assets.tile("""
        CoinSpawn
    """)):
        Coins = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . f f f f f f f . . . . 
                            . . . . f 5 5 5 5 5 5 5 f . . . 
                            . . . f 5 4 4 4 4 4 5 5 5 f . . 
                            . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 4 f . 
                            . . . f 5 5 4 5 5 5 5 5 4 f . . 
                            . . . . f 5 5 5 5 5 5 4 f . . . 
                            . . . . . f f f f f f f . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Collectable)
        animation.run_image_animation(Coins,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . f 5 4 4 4 4 5 5 5 5 f . . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 4 5 5 5 5 5 5 4 f . . 
                                . . f 5 5 5 5 5 5 5 5 4 f . . . 
                                . . . f 5 5 5 5 5 5 4 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f . . . . . . 
                                . . . . f 5 5 5 5 5 f . . . . . 
                                . . . f 5 4 4 4 5 5 5 f . . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 4 f . . . 
                                . . . f 5 5 5 5 5 5 4 f . . . . 
                                . . . . f 5 5 5 5 4 f . . . . . 
                                . . . . . f f f f f . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . f 5 5 5 f . . . . . . 
                                . . . . f 5 4 4 5 5 f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 4 f . . . . 
                                . . . . f 5 5 5 5 4 f . . . . . 
                                . . . . . f 5 5 4 f . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . f 5 4 5 f . . . . . . 
                                . . . . f 5 5 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 4 f . . . . . 
                                . . . . . f 5 5 4 f . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 4 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . f 5 4 5 f . . . . . . 
                                . . . . f 5 5 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 4 f . . . . . 
                                . . . . . f 5 5 4 f . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . f 5 5 5 f . . . . . . 
                                . . . . f 5 4 4 5 5 f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 4 f . . . . 
                                . . . . f 5 5 5 5 4 f . . . . . 
                                . . . . . f 5 5 4 f . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f . . . . . . 
                                . . . . f 5 5 5 5 5 f . . . . . 
                                . . . f 5 4 4 4 5 5 5 f . . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 4 f . . . 
                                . . . f 5 5 5 5 5 5 4 f . . . . 
                                . . . . f 5 5 5 5 4 f . . . . . 
                                . . . . . f f f f f . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . f 5 4 4 4 4 5 5 5 5 f . . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 4 5 5 5 5 5 5 4 f . . 
                                . . f 5 5 5 5 5 5 5 5 4 f . . . 
                                . . . f 5 5 5 5 5 5 4 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            500,
            True)
        tiles.place_on_tile(Coins, value8)
        tiles.set_tile_at(value8, assets.tile("""
            transparency16
        """))
    for value9 in tiles.get_tiles_by_type(assets.tile("""
        myTile4
    """)):
        Tree = sprites.create(img("""
                ........................
                            ...........66...........
                            ..........6776..........
                            ..........6776..........
                            .........877778.........
                            ........86777768........
                            .......6777777776.......
                            ......677677776776......
                            ......866777777668......
                            .....86677677677668.....
                            ....8668866766888668....
                            ....8888668886686888....
                            .....86868868868668.....
                            ....866888668888868.....
                            ....8688886888888888....
                            ....8886688888866888....
                            ....8676888868886768....
                            ...87778868678688776....
                            ..8777767767787767778...
                            .877767777777677776778..
                            .8866777777777777776778.
                            .8667776776767776777688.
                            ..887766768668776667668.
                            ..8688668886688686688668
                            .86688688686866888688888
                            8668868866888866888868..
                            88886686688888868688668.
                            .8688888888888888668868.
                            .8878888868868878868788.
                            .87768776788778777667788
                            877677767787776767776778
                            88877787766777777877788.
                            ..88886786777667768888..
                            .....86887786668868.....
                            ......8886888668888.....
                            .........88ee88.........
                            .........feeeef.........
                            .........feeeef.........
                            ........feeefeef........
                            ........fefeffef........
            """),
            SpriteKind.Trees)
        animation.run_image_animation(Tree, assets.animation("""
            treeDingding
        """), 500, True)
        tiles.place_on_tile(Tree, value9)
        tiles.set_tile_at(value9, assets.tile("""
            transparency16
        """))
    for value10 in tiles.get_tiles_by_type(assets.tile("""
        FlowerPlaceHolder
    """)):
        Cloud = sprites.create(img("""
                ....................
                            ....................
                            ....................
                            ....................
                            ....................
                            .........1..........
                            ......661d1.........
                            .....177717766......
                            ....1d177777677.....
                            ..6.717777c77177....
                            ...7c77767771d17....
                            ...77677766771777...
                            ..1777766677777767..
                            .1d1776717676777c7..
                            .7177661d176777777..
                            .77767771777777176..
                            .677c77777c7671d17..
                            .77777777777767176..
                            .667776776777777767.
                            ...76776766676766...
            """),
            SpriteKind.Bushes)
        tiles.place_on_tile(Cloud, value10)
        tiles.set_tile_at(value10, assets.tile("""
            transparency16
        """))
    for value11 in tiles.get_tiles_by_type(assets.tile("""
        myTile2
    """)):
        Bound = sprites.create(img("""
                . . . . . . b b b b . . . . . . 
                            . . . . b b 3 3 3 3 b b . . . . 
                            . . . c b 3 3 3 3 1 1 b c . . . 
                            . . c b 3 3 3 3 3 1 1 1 b c . . 
                            . c c 1 1 1 3 3 3 3 1 1 3 c c . 
                            c c d 1 1 1 3 3 3 3 3 3 3 b c c 
                            c b d d 1 3 3 3 3 3 1 1 1 b b c 
                            c b b b 3 3 1 1 3 3 1 1 d d b c 
                            c b b b b d d 1 1 3 b d d d b c 
                            . c b b b b d d b b b b b b c . 
                            . . c c b b b b b b b b c c . . 
                            . . . . c c c c c c c c . . . . 
                            . . . . . . b 1 1 b . . . . . . 
                            . . . . . . b 1 1 b b . . . . . 
                            . . . . . b b d 1 1 b . . . . . 
                            . . . . . b d d 1 1 b . . . . .
            """),
            SpriteKind.Bounds)
        tiles.place_on_tile(Bound, value11)
        animation.run_image_animation(Bound,
            [img("""
                    ......bbbb......................
                                ....bb3333bb....................
                                ...cb333311bc...................
                                ..cb33333111bc..................
                                .cc1113333113cc.................
                                ccd1113333333bcc................
                                cbdd133333111bbc................
                                cbbb33113311ddbc................
                                cbbbbdd113bdddbc................
                                .cbbbbddbbbbbbc.................
                                ..ccbbbbbbbbcc..................
                                ....cccccccc....................
                                ......b11b......................
                                ......b11bb.....................
                                .....bbd11b.....................
                                .....bdd11b.....................
                """),
                img("""
                    ................................
                                ................................
                                ................................
                                ......bbbb......................
                                ....bb3333bb....................
                                ...cb333311bc...................
                                ..cb33333111bc..................
                                .cb1113333113cc.................
                                cbd1113333333bbc................
                                cbbd133333111bbc................
                                cbbb33113311ddbc................
                                .cbbbdd113bdddc.................
                                ..ccbbddbbbbcc..................
                                ....cccccccc....................
                                .....bbd11b.....................
                                .....bdd11b.....................
                """),
                img("""
                    ................................
                                ................................
                                ................................
                                ......bbbb......................
                                ....bb3333bb....................
                                ...cb333311bc...................
                                ..cb33333111bc..................
                                .cb1113333113cc.................
                                cbd1113333333bbc................
                                cbbd133333111bbc................
                                cbbb33113311ddbc................
                                .cbbbdd113bdddc.................
                                ..ccbbddbbbbcc..................
                                ....cccccccc....................
                                .....bbd11b.....................
                                .....bdd11b.....................
                """),
                img("""
                    ......bbbb......................
                                ....bb3333bb....................
                                ...cb333311bc...................
                                ..cb33333111bc..................
                                .cc1113333113cc.................
                                ccd1113333333bcc................
                                cbdd133333111bbc................
                                cbbb33113311ddbc................
                                cbbbbdd113bdddbc................
                                .cbbbbddbbbbbbc.................
                                ..ccbbbbbbbbcc..................
                                ....cccccccc....................
                                ......b11b......................
                                ......b11bb.....................
                                .....bbd11b.....................
                                .....bdd11b.....................
                """)],
            500,
            True)
    for value12 in tiles.get_tiles_by_type(assets.tile("""
        CloudPlaceHolder
    """)):
        Cloud = sprites.create(assets.image("""
            cloud
        """), SpriteKind.Clouds)
        animation.run_image_animation(Cloud,
            [img("""
                    .........bbbb...........
                                .......bb1111bb.........
                                ......bb111111bbbbb.....
                                ......b1111111ddd11b....
                                ......b11111111d1111b...
                                ...bbbd11111111d1111b...
                                ..b11111111111111111bb..
                                .b11111111111111111d11b.
                                .b111d11111111111111111b
                                cdd1d111111111111111111c
                                cdddd11111111111111111dc
                                cddbd11111d11111dd111dc.
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bb.........
                                ......b1111111bbbbb.....
                                ......b1111111ddd11b....
                                ...bbbd11111111d1111b...
                                ..b111111111111d1111b...
                                .b111111111111111111bb..
                                .b111d1111111111111d11b.
                                cdd1d111111111111111111b
                                cdddd111111111111111111b
                                cddbd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ...bb.b1111111dd1111b...
                                ..b11bd11111111d1111b...
                                .b111111111111111111bb..
                                .b111d1111111111111d11b.
                                cdd1d111111111111111111b
                                cdddd111111111111111111b
                                cddbd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ......b1111111dd1111b...
                                ...bb.d11111111d1111b...
                                ..b11b11111111111111bb..
                                .b11111111111111111d11b.
                                .b111d11111111111111111b
                                cdd1d111111111111111111b
                                cdddd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ......b1111111dd1111b...
                                ...bb.d11111111d1111b...
                                ..b11b11111111111111bb..
                                .b11111111111111111d11b.
                                .b111d11111111111111111b
                                cdd1d111111111111111111b
                                ccbbdd111dddd11ddbdddccb
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                                ........................
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ......b1111111dd1111b...
                                ...bb.d11111111d1111b...
                                ..b11b11111111111111bb..
                                .b11111111111111111d11b.
                                .b111d11111111111111111b
                                cdd1d111111111111111111b
                                cdddd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ...bb.b1111111dd1111b...
                                ..b11bd11111111d1111b...
                                .b111111111111111111bb..
                                .b111d1111111111111d11b.
                                cdd1d111111111111111111b
                                cdddd111111111111111111b
                                cddbd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """)],
            500,
            True)
        tiles.place_on_tile(Cloud, value12)
        tiles.set_tile_at(value12, assets.tile("""
            transparency16
        """))
    for value13 in tiles.get_tiles_by_type(sprites.dungeon.collectible_insignia):
        gate = sprites.create(assets.image("""
            Cloud1
        """), SpriteKind.gates)
        animation.run_image_animation(gate, assets.animation("""
            gateMovement
        """), 500, True)
        tiles.place_on_tile(gate, value13)
    for value14 in tiles.get_tiles_by_type(sprites.swamp.swamp_tile6):
        bub = sprites.create(assets.image("""
            bubble
        """), SpriteKind.bubs)
        animation.run_image_animation(bub, assets.animation("""
            bubbleMovement
        """), 500, True)
        tiles.place_on_tile(bub, value14)
        tiles.set_tile_at(value14, assets.tile("""
            transparency16
        """))
    aboutMushroom()

def on_on_overlap2(sprite4, otherSprite2):
    music.ba_ding.play()
    info.change_score_by(1)
    otherSprite2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Collectable, on_on_overlap2)

def on_overlap_tile3(sprite5, location3):
    MyPlayer.say_text("XDD")
    MyPlayer.vy += -150
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite6, location4):
    game.over(False, effects.confetti)
scene.on_overlap_tile(SpriteKind.player,
    sprites.swamp.swamp_tile7,
    on_overlap_tile4)

def startLevel3():
    global Coins, Tree, Cloud, gate, lava, lava2, lava3
    sprites.destroy_all_sprites_of_kind(SpriteKind.Trees)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Bounds)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Collectable)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Flowers)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Bushes)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Clouds)
    sprites.destroy_all_sprites_of_kind(SpriteKind.gates)
    sprites.destroy_all_sprites_of_kind(SpriteKind.bubs)
    scene.set_background_color(9)
    scene.set_background_image(img("""
        5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
                5555555555555555522225555555555555555555555555555555555552222555555555555555555555555555555555555222255555555555555555555555555555555555522225555555555555555555
                5555555555522222222222555555555555555555555555555552222222222255555555555555555555555555555222222222225555555555555555555555555555522222222222555555555555555555
                5555555522222222222222555555555555555555555555552222222222222255555555555555555555555555222222222222225555555555555555555555555522222222222222555555555555555555
                5555552222222222222222555555555555555555555555222222222222222255555555555555555555555522222222222222225555555555555555555555552222222222222222555555555555555555
                5555522222222222222222555555555555555555555552222222222222222255555555555555555555555222222222222222225555555555555555555555522222222222222222555555555555555555
                5555522222222222222222555555555555555555555552222222222222222255555555555555555555555222222222222222225555555555555555555555522222222222222222555555555555555555
                5555222222222222222222255555555555555555555522222222222222222225555555555555555555552222222222222222222555555555555555555555222222222222222222255555555555555555
                5555222222222222222222255555555555555555555522222222222222222225555555555555555555552222222222222222222555555555555555555555222222222222222222255555555555555555
                5552222222222222222222255555522255555555555222222222222222222225555552225555555555522222222222222222222555555222555555555552222222222222222222255555522255555555
                5552222222222222222222255555222225555555555222222222222222222225555522222555555555522222222222222222222555552222255555555552222222222222222222255555222225555555
                5522222222222222222222255555222225555555552222222222222222222225555522222555555555222222222222222222222555552222255555555522222222222222222222255555222225555555
                5522222222222222222222255555222225555555552222222222222222222225555522222555555555222222222222222222222555552222255555555522222222222222222222255555222225555555
                5522222222222222222222255555222222555555552222222222222222222225555522222255555555222222222222222222222555552222225555555522222222222222222222255555222222555555
                5222222222222222222222255555222222555555522222222222222222222225555522222255555552222222222222222222222555552222225555555222222222222222222222255555222222555555
                5222222222222222222222255555222222555555522222222222222222222225555522222255555552222222222222222222222555552222225555555222222222222222222222255555222222555555
                5222222222222222222222255552222222555555522222222222222222222225555222222255555552222222222222222222222555522222225555555222222222222222222222255552222222555555
                2222222222222224222222255552222222555522222222222222222422222225555222222255552222222222222222242222222555522222225555222222222222222224222222255552222222555522
                2222222222222244222222255552222222552222222222222222224422222225555222222255222222222222222222442222222555522222225522222222222222222244222222255552222222552222
                2222222222222244222222255552222222252222222222222222224422222225555222222225222222222222222222442222222555522222222522222222222222222244222222255552222222252222
                2222222222222444422222255552222222222222222222222222244442222225555222222222222222222222222224444222222555522222222222222222222222222444422222255552222222222222
                2222222222244444222222222222222222222222222222222224444422222222222222222222222222222222222444442222222222222222222222222222222222244444222222222222222222222222
                2222222222222444222222222222222eeeeeee222222222222222444222222222222222eeeeeee222222222222222444222222222222222eeeeeee222222222222222444222222222222222eeeeeee22
                22222222222244444222222222222eeeeeeeeeee22222222222244444222222222222eeeeeeeeeee22222222222244444222222222222eeeeeeeeeee22222222222244444222222222222eeeeeeeeeee
                e222222222224444444222222222eeeeeeeeeeeee222222222224444444222222222eeeeeeeeeeeee222222222224444444222222222eeeeeeeeeeeee222222222224444444222222222eeeeeeeeeeee
                eee22222222444444222222222eeeeeeeeeeeeeeeee22222222444444222222222eeeeeeeeeeeeeeeee22222222444444222222222eeeeeeeeeeeeeeeee22222222444444222222222eeeeeeeeeeeeee
                eeee222224444444442222222eeeeeeeeeeeeeeeeeee222224444444442222222eeeeeeeeeeeeeeeeeee222224444444442222222eeeeeeeeeeeeeeeeeee222224444444442222222eeeeeeeeeeeeeee
                eeeee2222224444444422222eeeeeeeeeeeeeeeeeeeee2222224444444422222eeeeeeeeeeeeeeeeeeeee2222224444444422222eeeeeeeeeeeeeeeeeeeee2222224444444422222eeeeeeeeeeeeeeee
                eeeeee22ee4444444222222eeeeeeeeeeeeeeeeeeeeeee22ee4444444222222eeeeeeeeeeeeeeeeeeeeeee22ee4444444222222eeeeeeeeeeeeeeeeeeeeeee22ee4444444222222eeeeeeeeeeeeeeeee
                eeeeeeeeeeee4444442222ee4eeeeeeeeeeeeeeeeeeeeeeeeeee4444442222ee4eeeeeeeeeeeeeeeeeeeeeeeeeee4444442222ee4eeeeeeeeeeeeeeeeeeeeeeeeeee4444442222ee4eeeeeeeeeeeeeee
                eeeeeeeeee44444444422eee4eeeeeeeeeeeeeeeeeeeeeeeee44444444422eee4eeeeeeeeeeeeeeeeeeeeeeeee44444444422eee4eeeeeeeeeeeeeeeeeeeeeeeee44444444422eee4eeeeeeeeeeeeeee
                eeeeeeeee44444444444eee44eeeeeeeeeeeeeeeeeeeeeeee44444444444eee44eeeeeeeeeeeeeeeeeeeeeeee44444444444eee44eeeeeeeeeeeeeeeeeeeeeeee44444444444eee44eeeeeeeeeeeeeee
                eeeeeee44444444444eeeeee44eeeeeeeeeeeeeeeeeeeee44444444444eeeeee44eeeeeeeeeeeeeeeeeeeee44444444444eeeeee44eeeeeeeeeeeeeeeeeeeee44444444444eeeeee44eeeeeeeeeeeeee
                eeeeeeeee444444444eeeee44eeeeeeeeeeeeeeeeeeeeeeee444444444eeeee44eeeeeeeeeeeeeeeeeeeeeeee444444444eeeee44eeeeeeeeeeeeeeeeeeeeeeee444444444eeeee44eeeeeeeeeeeeeee
                eeeeeeeee4444444eeeeee4444eeeeeeeeeeeeeeeeeeeeeee4444444eeeeee4444eeeeeeeeeeeeeeeeeeeeeee4444444eeeeee4444eeeeeeeeeeeeeeeeeeeeeee4444444eeeeee4444eeeeeeeeeeeeee
                eeeeeeee44944444444ee444444eeeeeeeeeeeeeeeeeeeee44944444444ee444444eeeeeeeeeeeeeeeeeeeee44944444444ee444444eeeeeeeeeeeeeeeeeeeee44944444444ee444444eeeeeeeeeeeee
                eeeeeeeeee4444444444eee44eeeeeeeeeee4eeeeeeeeeeeee4444444444eee44eeeeeeeeeee4eeeeeeeeeeeee4444444444eee44eeeeeeeeeee4eeeeeeeeeeeee4444444444eee44eeeeeeeeeee4eee
                eeeeeeee44444444444ee444444eeeeeeeee4eeeeeeeeeee44444444444ee444444eeeeeeeee4eeeeeeeeeee44444444444ee444444eeeeeeeee4eeeeeeeeeee44444444444ee444444eeeeeeeee4eee
                eee4eee444444444444e44444444eeeeeee444eeeee4eee444444444444e44444444eeeeeee444eeeee4eee444444444444e44444444eeeeeee444eeeee4eee444444444444e44444444eeeeeee444ee
                eee44eeeee4444444444444444eeeeeeeeee44eeeee44eeeee4444444444444444eeeeeeeeee44eeeee44eeeee4444444444444444eeeeeeeeee44eeeee44eeeee4444444444444444eeeeeeeeee44ee
                ee44eeee44444444444444444444eeeeeee44eeeee44eeee44444444444444444444eeeeeee44eeeee44eeee44444444444444444444eeeeeee44eeeee44eeee44444444444444444444eeeeeee44eee
                eee44ee4444444444444444444444eeeee4444eeeee44ee4444444444444444444444eeeee4444eeeee44ee4444444444444444444444eeeee4444eeeee44ee4444444444444444444444eeeee4444ee
                ee4444444444444444444444444eeeeeeee4444eee4444444444444444444444444eeeeeeee4444eee4444444444444444444444444eeeeeeee4444eee4444444444444444444444444eeeeeeee4444e
                eee44444444444444444444444444eeeee4444eeeee44444444444444444444444444eeeee4444eeeee44444444444444444444444444eeeee4444eeeee44444444444444444444444444eeeee4444ee
                eee444444444444444444444444444eee444444eeee444444444444444444444444444eee444444eeee444444444444444444444444444eee444444eeee444444444444444444444444444eee444444e
                ee44444444444444444444444444eeeeee4444eeee44444444444444444444444444eeeeee4444eeee44444444444444444444444444eeeeee4444eeee44444444444444444444444444eeeeee4444ee
                e44444444444444444444444444444ee4444444ee44444444444444444444444444444ee4444444ee44444444444444444444444444444ee4444444ee44444444444444444444444444444ee4444444e
                ee44444444444444444444444444444ee4444444ee44444444444444444444444444444ee4444444ee44444444444444444444444444444ee4444444ee44444444444444444444444444444ee4444444
                ee4444444444444444444444444444ee44444444ee4444444444444444444444444444ee44444444ee4444444444444444444444444444ee44444444ee4444444444444444444444444444ee44444444
                4444444444444444444444444444444e444444444444444444444444444444444444444e444444444444444444444444444444444444444e444444444444444444444444444444444444444e44444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
                4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
    """))
    tiles.set_current_tilemap(tilemap("""
        level12
    """))
    MyPlayer.ay = 100
    tiles.place_on_random_tile(MyPlayer, assets.tile("""
        myTile3
    """))
    for value15 in tiles.get_tiles_by_type(assets.tile("""
        myTile3
    """)):
        tiles.set_tile_at(value15, assets.tile("""
            transparency16
        """))
    scene.camera_follow_sprite(MyPlayer)
    for value16 in tiles.get_tiles_by_type(assets.tile("""
        CoinSpawn
    """)):
        Coins = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . f f f f f f f . . . . 
                            . . . . f 5 5 5 5 5 5 5 f . . . 
                            . . . f 5 4 4 4 4 4 5 5 5 f . . 
                            . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 4 f . 
                            . . . f 5 5 4 5 5 5 5 5 4 f . . 
                            . . . . f 5 5 5 5 5 5 4 f . . . 
                            . . . . . f f f f f f f . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Collectable)
        animation.run_image_animation(Coins,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . f 5 4 4 4 4 5 5 5 5 f . . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 4 5 5 5 5 5 5 4 f . . 
                                . . f 5 5 5 5 5 5 5 5 4 f . . . 
                                . . . f 5 5 5 5 5 5 4 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f . . . . . . 
                                . . . . f 5 5 5 5 5 f . . . . . 
                                . . . f 5 4 4 4 5 5 5 f . . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 4 f . . . 
                                . . . f 5 5 5 5 5 5 4 f . . . . 
                                . . . . f 5 5 5 5 4 f . . . . . 
                                . . . . . f f f f f . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . f 5 5 5 f . . . . . . 
                                . . . . f 5 4 4 5 5 f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 4 f . . . . 
                                . . . . f 5 5 5 5 4 f . . . . . 
                                . . . . . f 5 5 4 f . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . f 5 4 5 f . . . . . . 
                                . . . . f 5 5 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 4 f . . . . . 
                                . . . . . f 5 5 4 f . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 4 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . f 5 4 5 f . . . . . . 
                                . . . . f 5 5 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 5 f . . . . . 
                                . . . . f 5 4 5 5 4 f . . . . . 
                                . . . . . f 5 5 4 f . . . . . . 
                                . . . . . . f 5 f . . . . . . . 
                                . . . . . . . f . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . f 5 5 5 f . . . . . . 
                                . . . . f 5 4 4 5 5 f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 5 f . . . . 
                                . . . f 5 4 5 5 5 5 4 f . . . . 
                                . . . . f 5 5 5 5 4 f . . . . . 
                                . . . . . f 5 5 4 f . . . . . . 
                                . . . . . . f f f . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f . . . . . . 
                                . . . . f 5 5 5 5 5 f . . . . . 
                                . . . f 5 4 4 4 5 5 5 f . . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 5 f . . . 
                                . . f 5 4 5 5 5 5 5 5 4 f . . . 
                                . . . f 5 5 5 5 5 5 4 f . . . . 
                                . . . . f 5 5 5 5 4 f . . . . . 
                                . . . . . f f f f f . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . f 5 4 4 4 4 5 5 5 5 f . . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 5 5 5 5 5 5 5 5 f . . 
                                . f 5 4 5 4 5 5 5 5 5 5 4 f . . 
                                . . f 5 5 5 5 5 5 5 5 4 f . . . 
                                . . . f 5 5 5 5 5 5 4 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            500,
            True)
        tiles.place_on_tile(Coins, value16)
        tiles.set_tile_at(value16, assets.tile("""
            transparency16
        """))
    for value17 in tiles.get_tiles_by_type(assets.tile("""
        myTile4
    """)):
        Tree = sprites.create(img("""
                ........................
                            ...........66...........
                            ..........6776..........
                            ..........6776..........
                            .........877778.........
                            ........86777768........
                            .......6777777776.......
                            ......677677776776......
                            ......866777777668......
                            .....86677677677668.....
                            ....8668866766888668....
                            ....8888668886686888....
                            .....86868868868668.....
                            ....866888668888868.....
                            ....8688886888888888....
                            ....8886688888866888....
                            ....8676888868886768....
                            ...87778868678688776....
                            ..8777767767787767778...
                            .877767777777677776778..
                            .8866777777777777776778.
                            .8667776776767776777688.
                            ..887766768668776667668.
                            ..8688668886688686688668
                            .86688688686866888688888
                            8668868866888866888868..
                            88886686688888868688668.
                            .8688888888888888668868.
                            .8878888868868878868788.
                            .87768776788778777667788
                            877677767787776767776778
                            88877787766777777877788.
                            ..88886786777667768888..
                            .....86887786668868.....
                            ......8886888668888.....
                            .........88ee88.........
                            .........feeeef.........
                            .........feeeef.........
                            ........feeefeef........
                            ........fefeffef........
            """),
            SpriteKind.Trees)
        animation.run_image_animation(Tree, assets.animation("""
            treeDingding
        """), 500, True)
        tiles.place_on_tile(Tree, value17)
        tiles.set_tile_at(value17, assets.tile("""
            transparency16
        """))
    for value18 in tiles.get_tiles_by_type(assets.tile("""
        CloudPlaceHolder
    """)):
        Cloud = sprites.create(assets.image("""
            cloud
        """), SpriteKind.Clouds)
        animation.run_image_animation(Cloud,
            [img("""
                    .........bbbb...........
                                .......bb1111bb.........
                                ......bb111111bbbbb.....
                                ......b1111111ddd11b....
                                ......b11111111d1111b...
                                ...bbbd11111111d1111b...
                                ..b11111111111111111bb..
                                .b11111111111111111d11b.
                                .b111d11111111111111111b
                                cdd1d111111111111111111c
                                cdddd11111111111111111dc
                                cddbd11111d11111dd111dc.
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bb.........
                                ......b1111111bbbbb.....
                                ......b1111111ddd11b....
                                ...bbbd11111111d1111b...
                                ..b111111111111d1111b...
                                .b111111111111111111bb..
                                .b111d1111111111111d11b.
                                cdd1d111111111111111111b
                                cdddd111111111111111111b
                                cddbd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ...bb.b1111111dd1111b...
                                ..b11bd11111111d1111b...
                                .b111111111111111111bb..
                                .b111d1111111111111d11b.
                                cdd1d111111111111111111b
                                cdddd111111111111111111b
                                cddbd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ......b1111111dd1111b...
                                ...bb.d11111111d1111b...
                                ..b11b11111111111111bb..
                                .b11111111111111111d11b.
                                .b111d11111111111111111b
                                cdd1d111111111111111111b
                                cdddd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ......b1111111dd1111b...
                                ...bb.d11111111d1111b...
                                ..b11b11111111111111bb..
                                .b11111111111111111d11b.
                                .b111d11111111111111111b
                                cdd1d111111111111111111b
                                ccbbdd111dddd11ddbdddccb
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                                ........................
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ......b1111111dd1111b...
                                ...bb.d11111111d1111b...
                                ..b11b11111111111111bb..
                                .b11111111111111111d11b.
                                .b111d11111111111111111b
                                cdd1d111111111111111111b
                                cdddd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """),
                img("""
                    ........................
                                .........bbbb...........
                                .......bb1111b..........
                                ......bb11111bbbbbb.....
                                ......b1111111bdd11b....
                                ...bb.b1111111dd1111b...
                                ..b11bd11111111d1111b...
                                .b111111111111111111bb..
                                .b111d1111111111111d11b.
                                cdd1d111111111111111111b
                                cdddd111111111111111111b
                                cddbd11111d11111111111db
                                .cbbdd111dddd11ddbdddcc.
                                .ccbbdddddbdddddddbcc...
                                ...cccdddbbbdddddcc.....
                                ......ccccccccccc.......
                """)],
            500,
            True)
        tiles.place_on_tile(Cloud, value18)
        tiles.set_tile_at(value18, assets.tile("""
            transparency16
        """))
    for value19 in tiles.get_tiles_by_type(sprites.dungeon.collectible_insignia):
        gate = sprites.create(assets.image("""
            Cloud1
        """), SpriteKind.gates)
        animation.run_image_animation(gate, assets.animation("""
            gateMovement
        """), 500, True)
        tiles.place_on_tile(gate, value19)
    for value20 in tiles.get_tiles_by_type(sprites.dungeon.hazard_lava1):
        lava = sprites.create(assets.image("""
            lavaMovement
        """), SpriteKind.lavas)
        animation.run_image_animation(lava,
            [img("""
                    5 4 4 5 5 4 4 4 4 2 2 2 4 4 4 4 
                                4 4 4 4 4 5 5 4 2 2 2 2 4 4 4 5 
                                4 2 2 2 4 4 5 4 2 2 4 4 5 5 5 5 
                                2 2 4 2 4 4 5 4 2 2 4 5 5 5 5 4 
                                2 2 2 2 4 4 5 4 2 2 4 4 5 5 4 4 
                                4 2 2 2 4 5 5 4 4 4 4 4 4 4 4 2 
                                2 2 2 4 4 5 5 5 4 4 2 2 2 2 2 2 
                                4 2 2 4 5 5 5 5 4 2 2 4 2 2 2 4 
                                5 4 4 4 4 4 4 5 5 4 2 2 2 4 4 4 
                                4 4 4 2 2 2 4 4 5 5 4 4 4 4 5 5 
                                4 2 2 2 2 2 2 2 4 5 5 5 5 5 5 5 
                                5 4 4 2 4 2 2 4 4 5 5 5 4 4 4 5 
                                5 5 4 2 2 2 4 4 4 5 5 4 2 2 2 4 
                                4 5 4 4 4 4 5 5 5 5 4 2 4 2 2 4 
                                4 5 5 5 5 5 5 4 4 4 2 4 2 4 2 4 
                                4 5 5 5 4 4 4 4 2 2 2 2 4 2 4 4
                """),
                img("""
                    4 5 5 5 4 4 4 4 2 2 2 2 4 2 4 4 
                                4 5 5 5 5 5 5 4 4 4 2 4 2 4 2 4 
                                4 5 4 4 4 4 5 5 5 5 4 2 4 2 2 4 
                                5 5 4 2 2 2 4 4 4 5 5 4 2 2 2 4 
                                5 4 4 2 4 2 2 4 4 5 5 5 4 4 4 5 
                                4 2 2 2 2 2 2 2 4 5 5 5 5 5 5 5 
                                4 4 4 2 2 2 4 4 5 5 4 4 4 4 5 5 
                                5 4 4 4 4 4 4 5 5 4 2 2 2 4 4 4 
                                4 2 2 4 5 5 5 5 4 2 2 4 2 2 2 4 
                                2 2 2 4 4 5 5 5 4 4 2 2 2 2 2 2 
                                4 2 2 2 4 5 5 4 4 4 4 4 4 4 4 2 
                                2 2 2 2 4 4 5 4 2 2 4 4 5 5 4 4 
                                2 2 4 2 4 4 5 4 2 2 4 5 5 5 5 4 
                                4 2 2 2 4 4 5 4 2 2 4 4 5 5 5 5 
                                4 4 4 4 4 5 5 4 2 2 2 2 4 4 4 5 
                                5 4 4 5 5 4 4 4 4 2 2 2 4 4 4 4
                """),
                img("""
                    4 4 4 4 2 2 2 4 4 4 4 5 5 4 4 5 
                                5 4 4 4 2 2 2 2 4 5 5 4 4 4 4 4 
                                5 5 5 5 4 4 2 2 4 5 4 4 2 2 2 4 
                                4 5 5 5 5 4 2 2 4 5 4 4 2 4 2 2 
                                4 4 5 5 4 4 2 2 4 5 4 4 2 2 2 2 
                                2 4 4 4 4 4 4 4 4 5 5 4 2 2 2 4 
                                2 2 2 2 2 2 4 4 5 5 5 4 4 2 2 2 
                                4 2 2 2 4 2 2 4 5 5 5 5 4 2 2 4 
                                4 4 4 2 2 2 4 5 5 4 4 4 4 4 4 5 
                                5 5 4 4 4 4 5 5 4 4 2 2 2 4 4 4 
                                5 5 5 5 5 5 5 4 2 2 2 2 2 2 2 4 
                                5 4 4 4 5 5 5 4 4 2 2 4 2 4 4 5 
                                4 2 2 2 4 5 5 4 4 4 2 2 2 4 5 5 
                                4 2 2 4 2 4 5 5 5 5 4 4 4 4 5 4 
                                4 2 4 2 4 2 4 4 4 5 5 5 5 5 5 4 
                                4 4 2 4 2 2 2 2 4 4 4 4 5 5 5 4
                """),
                img("""
                    4 4 2 4 2 2 2 2 4 4 4 4 5 5 5 4 
                                4 2 4 2 4 2 4 4 4 5 5 5 5 5 5 4 
                                4 2 2 4 2 4 5 5 5 5 4 4 4 4 5 4 
                                4 2 2 2 4 5 5 4 4 4 2 2 2 4 5 5 
                                5 4 4 4 5 5 5 4 4 2 2 4 2 4 4 5 
                                5 5 5 5 5 5 5 4 2 2 2 2 2 2 2 4 
                                5 5 4 4 4 4 5 5 4 4 2 2 2 4 4 4 
                                4 4 4 2 2 2 4 5 5 4 4 4 4 4 4 5 
                                4 2 2 2 4 2 2 4 5 5 5 5 4 2 2 4 
                                2 2 2 2 2 2 4 4 5 5 5 4 4 2 2 2 
                                2 4 4 4 4 4 4 4 4 5 5 4 2 2 2 4 
                                4 4 5 5 4 4 2 2 4 5 4 4 2 2 2 2 
                                4 5 5 5 5 4 2 2 4 5 4 4 2 4 2 2 
                                5 5 5 5 4 4 2 2 4 5 4 4 2 2 2 4 
                                5 4 4 4 2 2 2 2 4 5 5 4 4 4 4 4 
                                4 4 4 4 2 2 2 4 4 4 4 5 5 4 4 5
                """)],
            500,
            True)
        tiles.place_on_tile(lava, value20)
        tiles.set_tile_at(value20, assets.tile("""
            transparency16
        """))
    for value21 in tiles.get_tiles_by_type(assets.tile("""
        tilewlava3
    """)):
        lava2 = sprites.create(img("""
                f f f f 5 5 4 5 2 2 2 2 4 4 4 4 
                            f e e e f 5 2 5 2 2 2 2 4 4 4 5 
                            f f e f f 4 5 4 2 2 4 4 5 5 5 5 
                            f f f e f f 5 4 2 2 4 5 5 5 5 4 
                            e f f f f 4 5 4 2 2 4 4 5 5 4 4 
                            f e f e f e f 4 4 4 4 4 4 4 4 2 
                            f e e e 4 5 5 5 4 4 2 2 2 2 2 2 
                            f e e f e 4 5 5 4 2 2 4 2 2 2 4 
                            f f f f f 4 f 5 5 4 2 2 2 4 4 4 
                            f e f f e 2 4 4 5 5 4 4 4 4 5 5 
                            f e e f f 4 f 2 4 5 5 5 5 5 5 5 
                            f f e f f f 5 4 4 5 5 5 4 4 4 5 
                            f e e f e 2 4 4 4 5 5 4 2 2 2 4 
                            f f f e f 5 5 4 5 5 4 2 4 2 2 4 
                            f e e e 2 e 2 4 4 4 2 4 2 4 2 4 
                            f f e f f 4 4 4 2 2 2 2 4 2 4 5
            """),
            SpriteKind.lavas)
        animation.run_image_animation(lava2,
            assets.animation("""
                lava2movement
            """),
            500,
            True)
        tiles.place_on_tile(lava2, value21)
        tiles.set_tile_at(value21, assets.tile("""
            transparency16
        """))
    for value22 in tiles.get_tiles_by_type(assets.tile("""
        tilewlava4
    """)):
        lava3 = sprites.create(img("""
                4 4 4 4 2 2 2 2 5 4 5 5 f f f f 
                            5 4 4 4 2 2 2 2 5 2 5 f e e e f 
                            5 5 5 5 4 4 2 2 4 5 4 f f e f f 
                            4 5 5 5 5 4 2 2 4 5 f f e f f f 
                            4 4 5 5 4 4 2 2 4 5 4 f f f f e 
                            2 4 4 4 4 4 4 4 4 f e f e f e f 
                            2 2 2 2 2 2 4 4 5 5 5 4 e e e f 
                            4 2 2 2 4 2 2 4 5 5 4 e f e e f 
                            4 4 4 2 2 2 4 5 5 f 4 f f f f f 
                            5 5 4 4 4 4 5 5 4 4 2 e f f e f 
                            5 5 5 5 5 5 5 4 2 f 4 f f e e f 
                            5 4 4 4 5 5 5 4 4 5 f f f e f f 
                            4 2 2 2 4 5 5 4 4 4 2 e f e e f 
                            4 2 2 4 2 4 5 5 4 5 5 f e f f f 
                            4 2 4 2 4 2 4 4 4 2 e 2 e e e f 
                            5 4 2 4 2 2 2 2 4 4 4 f f e f f
            """),
            SpriteKind.lavas)
        animation.run_image_animation(lava3,
            assets.animation("""
                lava3movement
            """),
            500,
            True)
        tiles.place_on_tile(lava3, value22)
        tiles.set_tile_at(value22, assets.tile("""
            transparency16
        """))
    aboutPlay2()

def on_overlap_tile5(sprite7, location5):
    global currentLevel
    currentLevel += 1
    if currentLevel == 1:
        startLevel1()
    elif currentLevel == 2:
        startLevel2()
    else:
        startLevel3()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile5)

lava3: Sprite = None
lava2: Sprite = None
lava: Sprite = None
bub: Sprite = None
Bound: Sprite = None
Tree: Sprite = None
gate: Sprite = None
Cloud: Sprite = None
Flowers2: Sprite = None
Coins: Sprite = None
MyPlayer: Sprite = None
currentLevel = 0
info.set_life(1)
currentLevel = 1
playerSetup()
lv1Talk()
startLevel1()

def on_forever():
    characterAnimations.loop_frames(MyPlayer,
        [img("""
                . 1 . . . f f f f f . . . . . . 
                        . . . . f 5 1 5 1 5 f . 1 . . . 
                        1 . f f 1 1 5 5 5 1 1 f f . 1 . 
                        . f 3 3 1 1 5 5 5 1 1 3 3 f . . 
                        f 1 3 d f f 1 1 d f f 1 3 1 f . 
                        . f 1 f 1 f f 1 f 1 f f 1 f . . 
                        . f 1 f f 1 f 1 f f 1 f 1 f . 1 
                        . f 1 1 f f 1 1 1 f f 1 1 f . . 
                        . . f 1 3 3 d f d 3 3 1 f . . . 
                        . . f 1 1 1 d d d 1 1 1 f . 1 . 
                        1 . . f f f f f f f f f . . f . 
                        . . 1 . . f 1 1 1 f 1 f . . . f 
                        . . . . f 1 1 1 1 1 f 1 f . . f 
                        . . . . f 1 1 f 1 1 f 1 1 f . f 
                        . . . . . f 1 f 1 f 1 1 1 f f . 
                        . . . . . f d f d f d d f . . .
            """),
            img("""
                . . 1 . . f f f f f . . . . . 1 
                        . . . . f 5 1 5 1 5 f . 1 . . . 
                        f f f f 1 1 5 5 5 1 1 f f f f . 
                        f 3 3 3 1 1 5 5 5 1 1 3 3 3 f . 
                        f 1 3 d f f 1 1 d f f 1 3 1 f . 
                        . f 1 f f 1 f 1 f f 1 f 1 f . . 
                        . f 1 f 1 f f 1 f 1 f f 1 f . . 
                        . f 1 1 f f 1 1 1 f f 1 1 f . . 
                        . . f 1 3 3 d f d 3 3 1 f . 1 . 
                        1 . f 1 1 1 d d d 1 1 1 f . . 1 
                        . . . f f f f f f f f f . f . . 
                        . . . . . f 1 1 1 f 1 f . f . . 
                        . . . . f 1 1 1 1 1 f 1 f . f . 
                        . . . . f 1 1 f 1 1 f 1 1 f . f 
                        . . . . . f 1 f 1 f 1 1 1 f f . 
                        . . . . . f d f d f d d f . . .
            """)],
        500,
        characterAnimations.rule(Predicate.NOT_MOVING))
    characterAnimations.loop_frames(MyPlayer,
        [img("""
                . . . . . . f f f f f . . . . . 
                        . . . . . f 5 1 5 1 5 f . . . . 
                        . f f f f 1 1 5 5 5 1 1 f f f f 
                        . f 3 3 3 1 1 5 5 5 1 1 3 3 3 f 
                        . f 1 3 1 f f d 1 1 f f d 3 1 f 
                        . . f 1 f f 1 f 1 f f 1 f 1 f . 
                        . . f 1 f f f f 1 f f f f 1 f . 
                        . . f 1 1 f f 1 1 1 f f 1 1 f . 
                        . . . f 1 3 3 d f d 3 3 1 f . . 
                        . . . f 1 1 1 d d d 1 1 1 f . . 
                        . . f . f f f f f f f f f . . . 
                        . . . f . f 1 1 1 1 1 f . . . . 
                        . . f . f 1 f 1 1 1 1 1 f . . . 
                        . f . f 1 1 f 1 1 f 1 1 f . . . 
                        . . f f 1 1 1 f 1 f 1 f . . . . 
                        . . . . f d d f d f d f . . . .
            """),
            img("""
                . . . . . . f f f f f . . . . . 
                        . . . . . f 5 1 5 1 5 f . . . . 
                        . f f f f 1 1 5 5 5 1 1 f f f f 
                        . f 3 3 3 1 1 5 5 5 1 1 3 3 3 f 
                        . f 1 3 1 f f d 1 1 f f d 3 1 f 
                        . . f 1 f f 1 f 1 f f 1 f 1 f . 
                        . . f 1 f f f f 1 f f f f 1 f . 
                        . . f 1 1 f f 1 1 1 f f 1 1 f . 
                        . . . f 1 3 3 d f d 3 3 1 f . . 
                        . . . f 1 1 1 d d d 1 1 1 f . . 
                        . f . . f f f f f f f f f . . . 
                        f . . . . f 1 1 1 1 1 f . . . . 
                        f . . . f 1 f 1 1 1 1 1 f . . . 
                        . f . f 1 1 f 1 1 f 1 1 f . . . 
                        . f f f 1 1 1 f 1 f 1 f . . . . 
                        . . . . f d d f d f d f . . . .
            """)],
        500,
        characterAnimations.rule(Predicate.MOVING_RIGHT))
    characterAnimations.loop_frames(MyPlayer,
        [img("""
                . . . . . f f f f f . . . . . . 
                        . . . . f 5 1 5 1 5 f . . . . . 
                        f f f f 1 1 5 5 5 1 1 f f f f . 
                        f 3 3 3 1 1 5 5 5 1 1 3 3 3 f . 
                        f 1 3 d f f 1 1 d f f 1 3 1 f . 
                        . f 1 f 1 f f 1 f 1 f f 1 f . . 
                        . f 1 f f f f 1 f f f f 1 f . . 
                        . f 1 1 f f 1 1 1 f f 1 1 f . . 
                        . . f 1 3 3 d f d 3 3 1 f . . . 
                        . . f 1 1 1 d d d 1 1 1 f . . . 
                        . . . f f f f f f f f f . f . . 
                        . . . . f 1 1 1 1 1 f . f . . . 
                        . . . f 1 1 1 1 1 f 1 f . f . . 
                        . . . f 1 1 f 1 1 f 1 1 f . f . 
                        . . . . f 1 f 1 f 1 1 1 f f . . 
                        . . . . f d f d f d d f . . . .
            """),
            img("""
                . . . . . f f f f f . . . . . . 
                        . . . . f 5 1 5 1 5 f . . . . . 
                        f f f f 1 1 5 5 5 1 1 f f f f . 
                        f 3 3 3 1 1 5 5 5 1 1 3 3 3 f . 
                        f 1 3 d f f 1 1 d f f 1 3 1 f . 
                        . f 1 f 1 f f 1 f 1 f f 1 f . . 
                        . f 1 f f f f 1 f f f f 1 f . . 
                        . f 1 1 f f 1 1 1 f f 1 1 f . . 
                        . . f 1 3 3 d f d 3 3 1 f . . . 
                        . . f 1 1 1 d d d 1 1 1 f . . . 
                        . . . f f f f f f f f f . . f . 
                        . . . . f 1 1 1 1 1 f . . . . f 
                        . . . f 1 1 1 1 1 f 1 f . . . f 
                        . . . f 1 1 f 1 1 f 1 1 f . f . 
                        . . . . f 1 f 1 f 1 1 1 f f f . 
                        . . . . f d f d f d d f . . . .
            """)],
        500,
        characterAnimations.rule(Predicate.MOVING_LEFT))
    characterAnimations.loop_frames(MyPlayer,
        [img("""
                . . . . . f f f f f . . . . . . 
                        . . . . f 5 1 5 1 5 f . . . . . 
                        f f f f 1 1 5 5 5 1 1 f f f f . 
                        f 3 3 3 1 1 5 5 5 1 1 3 3 3 f . 
                        f 1 3 d f f 1 1 d f f 1 3 1 f . 
                        . f 1 f 1 f f 1 f 1 f f 1 f . . 
                        . f 1 f f f f 1 f f f f 1 f . . 
                        . f 1 1 f f 1 1 1 f f 1 1 f . . 
                        . . f 1 3 3 d f d 3 3 1 f . . . 
                        . . f 1 1 1 d d d 1 1 1 f . . . 
                        . . . f f f f f f f f f . . f . 
                        . . . . f 1 1 1 1 1 f . . . . f 
                        . . . f 1 1 1 1 1 f 1 f . . . f 
                        . . . f 1 1 f 1 1 f 1 1 f . f . 
                        . . . . f 1 f 1 f 1 1 1 f f f . 
                        . . . . f d f d f d d f . . . .
            """),
            img("""
                . . . . . f f f f f . . . . . . 
                        . . . . f 5 1 5 1 5 f . . . . . 
                        f f f f 1 1 5 5 5 1 1 f f f f . 
                        f 3 3 3 1 1 5 5 5 1 1 3 3 3 f . 
                        f 1 3 d f f 1 1 d f f 1 3 1 f . 
                        . f 1 f 1 f f 1 f 1 f f 1 f . . 
                        . f 1 f f f f 1 f f f f 1 f . . 
                        . f 1 1 f f 1 1 1 f f 1 1 f f . 
                        . . f 1 3 3 d f d 3 3 1 f . . f 
                        . . f 1 1 1 d d d 1 1 1 f . . f 
                        . . . f f f f f f f f f . . f . 
                        . f f 1 1 1 1 1 1 1 1 1 f f . . 
                        f 1 1 1 1 1 1 f 1 1 1 1 1 1 d f 
                        d 1 f f 1 1 f 1 1 1 1 1 1 f f . 
                        f f . f 1 f . f f f f 1 1 1 d f 
                        . . f d 1 f . . . . . f f f f .
            """)],
        500,
        characterAnimations.rule(Predicate.MOVING_UP, Predicate.MOVING_LEFT))
    characterAnimations.loop_frames(MyPlayer,
        [img("""
                . . . . . f f f f f . . . . . . 
                        . . . . f 5 1 5 1 5 f . . . . . 
                        f f f f 1 1 5 5 5 1 1 f f f f . 
                        f 3 3 3 1 1 5 5 5 1 1 3 3 3 f . 
                        f 1 3 d f f 1 1 d f f 1 3 1 f . 
                        . f 1 f 1 f f 1 f 1 f f 1 f . . 
                        . f 1 f f f f 1 f f f f 1 f . . 
                        . f 1 1 f f 1 1 1 f f 1 1 f . . 
                        . . f 1 3 3 d f d 3 3 1 f . . . 
                        . . f 1 1 1 d d d 1 1 1 f . . . 
                        . . . f f f f f f f f f . . f . 
                        . . . . f 1 1 1 1 1 f . . . . f 
                        . . . f 1 1 1 1 1 f 1 f . . . f 
                        . . . f 1 1 f 1 1 f 1 1 f . f . 
                        . . . . f 1 f 1 f 1 1 1 f f f . 
                        . . . . f d f d f d d f . . . .
            """),
            img("""
                . . . . . f f f f f . . . . . . 
                        . . . . f 5 1 5 1 5 f . . . . . 
                        f f f f 1 1 5 5 5 1 1 f f f f . 
                        f 3 3 3 1 1 5 5 5 1 1 3 3 3 f . 
                        f 1 3 d f f 1 1 d f f 1 3 1 f . 
                        . f 1 f 1 f f 1 f 1 f f 1 f . . 
                        . f 1 f f f f 1 f f f f 1 f . . 
                        . f 1 1 f f 1 1 1 f f 1 1 f f . 
                        . . f 1 3 3 d f d 3 3 1 f . . f 
                        . . f 1 1 1 d d d 1 1 1 f . . f 
                        . . . f f f f f f f f f . . f . 
                        . f f 1 1 1 1 1 1 1 1 1 f f . . 
                        f 1 1 1 1 1 1 f 1 1 1 1 1 1 d f 
                        d 1 f f 1 1 f 1 1 1 1 1 1 f f . 
                        f f . f 1 f . f f f f 1 1 1 d f 
                        . . f d 1 f . . . . . f f f f .
            """)],
        500,
        characterAnimations.rule(Predicate.MOVING_DOWN, Predicate.MOVING_LEFT))
    characterAnimations.loop_frames(MyPlayer,
        [img("""
                . . . . . . f f f f f . . . . . 
                        . . . . . f 5 1 5 1 5 f . . . . 
                        . f f f f 1 1 5 5 5 1 1 f f f f 
                        . f 3 3 3 1 1 5 5 5 1 1 3 3 3 f 
                        . f 1 3 1 f f d 1 1 f f d 3 1 f 
                        . . f 1 f f 1 f 1 f f 1 f 1 f . 
                        . . f 1 f f f f 1 f f f f 1 f . 
                        . . f 1 1 f f 1 1 1 f f 1 1 f . 
                        . . . f 1 3 3 d f d 3 3 1 f . . 
                        . . . f 1 1 1 d d d 1 1 1 f . . 
                        . f . . f f f f f f f f f . . . 
                        f . . . . f 1 1 1 1 1 f . . . . 
                        f . . . f 1 f 1 1 1 1 1 f . . . 
                        . f . f 1 1 f 1 1 f 1 1 f . . . 
                        . f f f 1 1 1 f 1 f 1 f . . . . 
                        . . . . f d d f d f d f . . . .
            """),
            img("""
                . . . . . . f f f f f . . . . . 
                        . . . . . f 5 1 5 1 5 f . . . . 
                        . f f f f 1 1 5 5 5 1 1 f f f f 
                        . f 3 3 3 1 1 5 5 5 1 1 3 3 3 f 
                        . f 1 3 1 f f d 1 1 f f d 3 1 f 
                        . . f 1 f f 1 f 1 f f 1 f 1 f . 
                        . . f 1 f f f f 1 f f f f 1 f . 
                        . f f 1 1 f f 1 1 1 f f 1 1 f . 
                        f . . f 1 3 3 d f d 3 3 1 f . . 
                        f . . f 1 1 1 d d d 1 1 1 f . . 
                        . f . . f f f f f f f f f . . . 
                        . . f f 1 1 1 1 1 1 1 1 1 f f . 
                        f d 1 1 1 1 1 1 f 1 1 1 1 1 1 f 
                        . f f 1 1 1 1 1 1 f 1 1 f f 1 d 
                        f d 1 1 1 f f f f . f 1 f . f f 
                        . f f f f . . . . . f 1 d f . .
            """)],
        500,
        characterAnimations.rule(Predicate.MOVING_UP, Predicate.MOVING_RIGHT))
    characterAnimations.loop_frames(MyPlayer,
        [img("""
                . . . . . . f f f f f . . . . . 
                        . . . . . f 5 1 5 1 5 f . . . . 
                        . f f f f 1 1 5 5 5 1 1 f f f f 
                        . f 3 3 3 1 1 5 5 5 1 1 3 3 3 f 
                        . f 1 3 1 f f d 1 1 f f d 3 1 f 
                        . . f 1 f f 1 f 1 f f 1 f 1 f . 
                        . . f 1 f f f f 1 f f f f 1 f . 
                        . . f 1 1 f f 1 1 1 f f 1 1 f . 
                        . . . f 1 3 3 d f d 3 3 1 f . . 
                        . . . f 1 1 1 d d d 1 1 1 f . . 
                        . f . . f f f f f f f f f . . . 
                        f . . . . f 1 1 1 1 1 f . . . . 
                        f . . . f 1 f 1 1 1 1 1 f . . . 
                        . f . f 1 1 f 1 1 f 1 1 f . . . 
                        . f f f 1 1 1 f 1 f 1 f . . . . 
                        . . . . f d d f d f d f . . . .
            """),
            img("""
                . . . . . . f f f f f . . . . . 
                        . . . . . f 5 1 5 1 5 f . . . . 
                        . f f f f 1 1 5 5 5 1 1 f f f f 
                        . f 3 3 3 1 1 5 5 5 1 1 3 3 3 f 
                        . f 1 3 1 f f d 1 1 f f d 3 1 f 
                        . . f 1 f f 1 f 1 f f 1 f 1 f . 
                        . . f 1 f f f f 1 f f f f 1 f . 
                        . f f 1 1 f f 1 1 1 f f 1 1 f . 
                        f . . f 1 3 3 d f d 3 3 1 f . . 
                        f . . f 1 1 1 d d d 1 1 1 f . . 
                        . f . . f f f f f f f f f . . . 
                        . . f f 1 1 1 1 1 1 1 1 1 f f . 
                        f d 1 1 1 1 1 1 f 1 1 1 1 1 1 f 
                        . f f 1 1 1 1 1 1 f 1 1 f f 1 d 
                        f d 1 1 1 f f f f . f 1 f . f f 
                        . f f f f . . . . . f 1 d f . .
            """)],
        500,
        characterAnimations.rule(Predicate.MOVING_DOWN, Predicate.MOVING_RIGHT))
forever(on_forever)

def on_forever2():
    if MyPlayer.vx != 0:
        music.footstep.play()
forever(on_forever2)

def on_forever3():
    if currentLevel == 1:
        music.set_volume(15)
        music.play_melody("B C5 B G F E E G ", 120)
    elif currentLevel == 2:
        music.set_volume(15)
        music.play_melody("A G E E D E C C ", 120)
    elif currentLevel == 3:
        music.set_volume(15)
        music.play_melody("C B C A C G C F ", 120)
    else:
        pass
forever(on_forever3)

def on_forever4():
    if currentLevel == 1:
        music.set_volume(10)
        music.play_melody("G - E - C - C E ", 120)
    elif currentLevel == 2:
        music.set_volume(10)
        music.play_melody("D - C - C - D - ", 120)
    elif currentLevel == 3:
        music.set_volume(10)
        music.play_melody("G C F C E C D C ", 120)
    else:
        pass
forever(on_forever4)
