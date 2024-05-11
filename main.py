import arcade

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN_TITLE="Динозаврик"
SCREEN_D=450
SCREEN_D2=250


class Animechen(arcade.Sprite):
    frame_index=0
    time=0

    def update_animation(self,delta_time):
        self.time+=delta_time
        if self.time>0.1:
            self.time=0
            if self.frame_index==len(self.textures)-1:
                self.frame_index=0
            else:
                self.frame_index += 1
            self.set_texture(self.frame_index)

class Kaktus(Animechen):
    def __init__(self,filename,scale):
        super().__init__(filename, scale)
        self.center_x = SCREEN_WIDTH
        self.center_y = SCREEN_HEIGHT / 3.25

    def update(self):
        self.center_x -=4
        if self.center_x == 0:
            self.center_x = SCREEN_WIDTH
            window.score+=1


class Dino(Animechen):
    def __init__(self,filename,scale):
        super().__init__(filename,scale)
        self.center_x = SCREEN_WIDTH/4
        self.center_y = SCREEN_HEIGHT / 3

    def update(self):
        self.center_y+=self.change_y
        if self.top>SCREEN_D:
            self.change_y -=1
        if self.top<=SCREEN_D2:
            self.change_y=0
            window.isJump=False

class Game(arcade.Window):
    def __init__(self, width,height,title):
        super().__init__(width,height,title)
        self.bg=arcade.load_texture("images/bg.png")
        self.dino=Dino("images/dino1.png",1)
        self.kaktus=Kaktus("images/cactus1.png",1)
        for i in range(1,4):
            self.dino.append_texture(arcade.load_texture(f"images/dino{i}.png"))
        for i in range(1,3):
            self.kaktus.append_texture(arcade.load_texture(f"images/cactus{i}.png"))
        self.score=0
        self.isJump=False
        self.game = True

        self.over=arcade.load_texture("images/game_over.png")

        self.win = arcade.load_texture("images/win.png")



    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.dino.draw()
        self.kaktus.draw()
        arcade.draw_text(f"Счет:{self.score}", 20, 600 - 30, (0, 0, 0), 20)
        if self.game == False:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.over)
            # arcade.draw_text(f"Вы проиграли", 250, SCREEN_HEIGHT / 2, (0, 0, 0), 40)

        if self.score==5:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.win)


    def update(self, delta_time):
        if self.game:
            self.dino.update()
            self.kaktus.update()
            self.kaktus.update_animation(delta_time)
            if self.isJump!=True:
                self.dino.update_animation(delta_time)
            if arcade.check_for_collision(self.dino, self.kaktus):
                self.game = False


    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.isJump!=True:
            self.dino.change_y = 5
            self.isJump = True

    def on_key_release(self, key, modifiers):
        pass




window=Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
arcade.run()