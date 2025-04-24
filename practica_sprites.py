import pygame

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ancho = 500
alto = 500
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Animación de Sprite")

# Cargar las imágenes de los sprites
sprite1 = pygame.image.load("1618037802244.png").convert_alpha()
sprite2 = pygame.image.load("1618037802244.png").convert_alpha()
sprite3 = pygame.image.load("1618037802244.png").convert_alpha()
sprite4 = pygame.image.load("1618037802244.png").convert_alpha()
sprite6 = pygame.image.load("1618077845174.png").convert_alpha()
sprite7 = pygame.image.load("1618077845174.png").convert_alpha()
sprite8 = pygame.image.load("1618077883554.png").convert_alpha()
sprite9 = pygame.image.load("1618077883554.png").convert_alpha()
sprite10 = pygame.image.load("1618077980876.png").convert_alpha()
sprite11 = pygame.image.load("1618077980876.png").convert_alpha()
sprite12 = pygame.image.load("1618078023646.png").convert_alpha()
sprite13 = pygame.image.load("1618078023646.png").convert_alpha()
sprite14 = pygame.image.load("1618078056874.png").convert_alpha()
sprite15 = pygame.image.load("1618078056874.png").convert_alpha()
sprite16 = pygame.image.load("1618078056874.png").convert_alpha()
sprite17 = pygame.image.load("1618078056874.png").convert_alpha()
sprite18 = pygame.image.load("1618078056874.png").convert_alpha()

# Crear la lista de sprites de la animación
animacion_sprites = [sprite1, sprite2, sprite3, sprite4, sprite6, sprite7, sprite8, sprite9, sprite10, sprite11, sprite12, sprite13, sprite14, sprite15, sprite16, sprite17, sprite18 ]

# Índice del sprite actual
indice_actual = 0

# Posición del sprite en la pantalla
x = 100
y = 100

# Control de la velocidad de la animación (en fotogramas)
velocidad_animacion = 20
contador_animacion = 0

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Limpiar la pantalla
    screen.fill((0, 0, 0))  # Fondo negro

    # Actualizar la animación
    contador_animacion += 1
    if contador_animacion >= velocidad_animacion:
        contador_animacion = 0
        indice_actual = (indice_actual + 1) % len(animacion_sprites)
        sprite_actual = animacion_sprites[indice_actual]
        screen.blit(sprite_actual, (x, y))

    # Dibujar el sprite actual
    else:
        sprite_actual = animacion_sprites[indice_actual]
        screen.blit(sprite_actual, (x, y))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()