__author__ = 'Robson_Marinho && Isabela Oliveira'


    ### CRIA TELA / CORES / TAMANHO / POSIÇÃO / VELOCIDADE ###

SCREEN_HEIGHT = 768  #Altura da tela
SCREEN_WIDTH = 1024  #largura da tela

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) #Variável de largura e altura

TITLE = "Super Mário Bros"  #Título da página

    #### DEFININDO AS CORES RGB ###

WHITE        = (255, 255, 255)
RED          = (255, 0, 0)
GRAY         = (100, 100, 100)
NAVYBLUE     = (60, 60, 100)
GREEN        = ( 0, 255, 0)
FOREST_GREEN = (31, 162, 35)
BLUE         = (0, 0, 255)
SKY_BLUE     = (0, 0, 255)
YELLOW       = (255, 255, 0)
ORANGE       = (255, 255, 0)
PURPLE       = (255, 0, 255)
CYAN         = (0, 255, 255)
BLACK        = (0, 0, 0)
NEAR__BLACK  = (19, 15, 48)
COMBLUE      = (233, 232, 255)
GOLD         = (255, 215, 0)

BGCOLOR = WHITE #Variável de background

SIZE_MULTIPLAYER = 2.5  #Tamanho do multiplayer
BRICK_SIZE_MULTIPLAYER = 2.69
BACKGROUND_MULTIPLAYER = 2.679
GROUND_HEIGHT = SCREEN_HEIGHT - 62

### MARIO FORÇAS ###

WALK_ACCEL = .15
RUN_ACCEL = 20
SMALL_TURNAROUND = .35

GRAVITY = 1.01  #define a gravidade
JUMP_GRAVITY = .31
JUMP_VEL = -10  #Velocidade do pulo
FAST_JUMP_VEL = -12.5   #velocidade do pulo na corrida
MAX_Y_VEL = 11

MAX_RUN_SPEED = 800 #Máximo de velocidade
MAX_WALK_SPEED = 6

    ### MARIO ESTADOS ###

STAND = 'standing'  #De pé
WALK = 'walk'   #andando
JUMP = 'jump'   #pulando
FALL = 'fall'
SMALL_TO_BIG = 'small to big'           #De pequeno para grande
BIG_TO_FIRE = 'big to fire'             #De grande para fogo
BIG_TO_SMALL = 'big to small'           #De grande para pequeno
FLAGPOLE = 'flag pole'                  #bandeira
WALKING_TO_CASTLE = 'walking to castle' #Andando ao castelo
END_OF_LEVEL_FALL = 'end of level fall' #Final do level

#ESTADOS DE POSIÇÃO

LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'


SHELL_SLIDE = 'shell slide'

#ESTADO DOS TIJOLOS

RESTING = 'resting'
BUMPED = 'bumped'

#MOEDAS
OPENED = 'opened'

#ESTADOS DE COGUMELOS

REVEAL = 'reveal'
SLIDE = 'slide'

#ESTADOS DE MOEDAS

SPIN = 'spin'

#ESTADO ESTRELAS

BOUNCE = 'bounce'

#ESTADOS DE FOGO E EXPLOSÃO

FLYING = 'flying'
BOUNCING = 'bouncing'
EXPLODING = 'exploding'

#CONTEUDO DAS CAIXAS E MOEDAS

MUSHROOM = 'mushroom'
STAR = 'star'
FIREFLOWER = 'fireflower'
SIXCOINS = '6coins'
COIN = 'coin'
LIFE_MUSHROOM = '1up_mushroom'

FIREBALL = 'fireball'

#LISTA DE INIMIGOS

GOOMBA = 'goomba'
KOOPA = 'koopa'

#ESTADOS DOS NIVEIS

FROZEN = 'frozen'
NOT_FROZEN = 'not frozen'
IN_CASTLE = 'in castle'
FLAG_AND_FIREWORKS = 'flag and fireworks'

#ESTADO DA BANDEIRA
TOP_OF_POLE = 'top of pole'
SLIDE_DOWN = 'slide down'
BOTTOM_OF_POLE = 'bottom of pole'

#1UP PONTOS
ONEUP = '379'

#MAIN MENU ESTADOS DO CURSOR
PLAYER1 = '1 player'
PLAYER2 = '2 player'

#ESTADOS DE CARREGAMENTO DE INFORMAÇÕES
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'loading screen'
LEVEL = 'level'
GAME_OVER = 'game over'
FAST_COUNT_DOWN = 'fast count down'
END_OF_LEVEL = 'end of level'


#INFORMAÇÕES DE TEXTOS DO JOGO
COIN_TOTAL = 'coin total'
SCORE = 'score'
TOP_SCORE = 'top score'
LIVES = 'lives'
CURRENT_TIME = 'current time'
LEVEL_STATE = 'level state'
CAMERA_START_X = 'camera start x'
MARIO_DEAD = 'mario dead'

#ESTADOS DA ENGINE DO JOGO
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
TIME_OUT = 'time out'
GAME_OVER = 'game over'
LEVEL1 = 'level1'

#ESTADOS DOS SONS
NORMAL = 'normal'
STAGE_CLEAR = 'stage clear'
WORLD_CLEAR = 'world clear'
TIME_WARNING = 'time warning'
SPED_UP_NORMAL = 'sped up normal'
MARIO_INVINCIBLE = 'mario invincible'