input.onButtonPressed(Button.A, function () {
    if (input.pinIsPressed(TouchPin.P2) || input.logoIsPressed()) {
        sprite.set(LedSpriteProperty.Direction, 270)
        sprite.move(1)
    } else {
        sprite.set(LedSpriteProperty.Direction, 90)
        sprite.move(1)
    }
})
input.onButtonPressed(Button.B, function () {
    if (input.pinIsPressed(TouchPin.P2) || input.logoIsPressed()) {
        sprite.set(LedSpriteProperty.Direction, 0)
        sprite.move(1)
    } else {
        sprite.set(LedSpriteProperty.Direction, 180)
        sprite.move(1)
    }
})
let sprite: game.LedSprite = null
sprite = game.createSprite(0, 0)
