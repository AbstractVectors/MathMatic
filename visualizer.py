import pygame
from pygame.locals import *
from node_placeholder import *

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('GPT Tree Visualizer')
pygame.init()

original_size = 4000
size = original_size
surface = pygame.surface.Surface((size, size))
surface.fill((255, 255, 255))
blit_x = -original_size // 2
blit_y = 0
mouse_down = False
mouse_last_pos = (0, 0)
move = [0, 0]


def show_text(surface, text, x, y, color=(0, 0, 0)):
    textobj=pygame.font.SysFont('courier new', 32).render(text, False, color)
    surface.blit(textobj, (x, y))


class Button:

    def __init__(self, text, x, y):
        self.text = text
        self.position = [x, y]
        self.dimensions = [len(text) * 30, 30]
        self.rect = None

    def draw(self):
        self.rect = pygame.draw.rect(screen, (0, 0, 0), self.position + self.dimensions, 2)
        show_text(screen, self.text, self.position[0] + 3, self.position[1] - 3)


class Rectangle:

    def __init__(self, x, y, node: Node, parent_node):
        self.position = [x, y]
        self.dimensions = [600, 200]
        self.node = node
        self.rect = None
        self.parent_node = parent_node

    def draw(self):
        self.rect = pygame.draw.rect(surface, (0, 0, 0), self.position + self.dimensions, 4)
        if self.parent_node is not None:
            pygame.draw.line(surface, (0, 0, 0), (self.position[0] + self.dimensions[0] // 2, self.position[1]), (self.parent_node.position[0] + self.parent_node.dimensions[0] // 2, self.parent_node.position[1] + self.parent_node.dimensions[1]), 2)
        show_text(surface, 'id: ' + str(self.node.id), self.position[0] + 5, self.position[1] + 5)
        show_text(surface, 'level: ' + str(self.node.level), self.position[0] + 5, self.position[1] + 40)

    def print_data(self):
        print('id: ' + str(self.node.id))
        print('prompt: ' + levels[self.node.level])
        print('gpt output: ' + gpt_output_lookup_table[self.node.id])


node_rectangles = {}
num_leaves = 0


def build_node_rects(current, parent_rect):
    global node_rectangles, num_leaves
    node_rectangles[current] = (Rectangle(0, (current.level + 1) * 300, current, parent_rect))
    if len(current.children) == 0:
        num_leaves += 1
    for child in current.children:
        build_node_rects(child, node_rectangles[current])


build_node_rects(root, None)
tree_list = [[]]


def listify_tree(current):
    global tree_list
    if len(tree_list) == current.level:
        tree_list.append([])
    tree_list[-1].append(current)
    for child in current.children:
        listify_tree(child)


listify_tree(root)
x = 50
for node in tree_list[-1]:
    node_rectangles[node].position[0] = x
    x += 650

for i in range(len(tree_list) - 2, -1, -1):
    layer = tree_list[i]
    for node in layer:
        node_rectangles[node].position[0] = (node_rectangles[node.children[0]].position[0] + node_rectangles[node.children[-1]].position[0]) // 2


for rect in node_rectangles.values():
    rect.draw()


zoom_in = Button('+', 1000, 720)
zoom_out = Button('-', 1000, 750)


while True:
    blit_x += move[0]
    blit_y += move[1]
    #display_surface.fill((255, 255, 255))
    #display_surface.blit(pygame.transform.scale(surface, (int(size), int(size))), (blit_x, blit_y))
    screen.blit(pygame.transform.scale(surface, (int(size), int(size))), (blit_x, blit_y))

    zoom_in.draw()
    zoom_out.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_down = True
            mouse_last_pos = event.pos
            surface_click = ((mouse_last_pos[0] - blit_x) * original_size // int(size), (mouse_last_pos[1] - blit_y) * original_size // int(size))
            if zoom_in.rect.collidepoint(event.pos):
                size *= 1.2
            elif zoom_out.rect.collidepoint(event.pos):
                size /= 1.2
            else:
                for rect in node_rectangles.values():
                    rect.draw()
                    if rect.rect.collidepoint(surface_click):
                        rect.print_data()
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            mouse_down = False
        elif event.type == MOUSEMOTION:
            if mouse_down:
                blit_x += (event.pos[0] - mouse_last_pos[0]) // ( original_size // size)
                blit_y += (event.pos[1] - mouse_last_pos[1]) // ( original_size // size)
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                move[1] = -10
            elif event.key == K_DOWN:
                move[1] = 10
            elif event.key == K_LEFT:
                move[0] = -10
            elif event.key == K_RIGHT:
                move[0] = 10
        elif event.type == KEYUP:
            if event.key == K_UP:
                move[1] = 0
            elif event.key == K_DOWN:
                move[1] = 0
            elif event.key == K_LEFT:
                move[0] = 0
            elif event.key == K_RIGHT:
                move[0] = 0
    pygame.display.update()
