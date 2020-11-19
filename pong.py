import pyxel

TAMANHO_BOLA = 2
VELOCIDADE_BOLA = 2
LARGURA_TELA = 255
ALTURA_TELA = 120

class Game:
    def __init__(self):
        pyxel.init(LARGURA_TELA,ALTURA_TELA,caption="Pong")

        self.player1_x = 0
        self.player1_y = 40
        self.player2_x = 245
        self.player2_y = 40

        self.score = 0

        pyxel.run(self.update, self.draw)

    def processar_entrada(self):
        if pyxel.btn(pyxel.KEY_Q) :
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_W) :
            self.player1_y -= 5
            self.player2_y -= 5
        if pyxel.btn(pyxel.KEY_S) :
            self.player1_y += 5
            self.player2_y += 5
    
    def limite_bordas(self):
        self.player1_y = max(self.player1_y,5)
        self.player2_y = max(self.player2_y,5)
        self.player1_y = min(self.player1_y,75)
        self.player2_y = min(self.player2_y,75)


    def update(self):
        self.limite_bordas()
        self.processar_entrada()


    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.player1_x,self.player1_y,10,40,7)
        pyxel.rect(self.player2_x,self.player2_y,10,40,7)
        pyxel.rect(125,0,5,120,7)#barra central
        pyxel.text(135,2,f"SCORE = {self.score}",10)
        pyxel.circ(127.5, 60, 10, 7)#circulo central


Game()