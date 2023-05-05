def on_button_pressed_a():
    if input.pin_is_pressed(TouchPin.P2) or input.logo_is_pressed():
        sprite.set(LedSpriteProperty.DIRECTION, 270)
        sprite.move(1)
    else:
        sprite.set(LedSpriteProperty.DIRECTION, 90)
        sprite.move(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if input.pin_is_pressed(TouchPin.P2) or input.logo_is_pressed():
        sprite.set(LedSpriteProperty.DIRECTION, 0)
        sprite.move(1)
    else:
        sprite.set(LedSpriteProperty.DIRECTION, 180)
        sprite.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

sprite: game.LedSprite = None
sprite = game.create_sprite(0, 0)