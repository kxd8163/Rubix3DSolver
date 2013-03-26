#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Karina Damico <kxd8163@rit.edu>, Ravdeep Johar <rsj7209@rit.edu>'
__date__ = '12.23.12'
__version__ = '0.0.1'

# Visualization of cube states and transformations using magic VPython 

from visual import *
from pprint import pprint

class Visualizer:
    
    def __init__(self):
        self.speed_rotate = 50
        self.range_rotate = 50
        # self.axes()
        self.d = 0.05 # delta between boxes
        self.arris = 1
        scene.center = (0, 0, 0)
        scene.forward = (-1, -1, -1)
        scene.scale = (0.2,0.2,0.2)
        self.cube = {}
        self.model = None
        self.init_drawing() # Init drawing window and subsystem

    def axes(self):
        x = arrow(pos=(0,0,0), axis=(3,0,0), shaftwidth=0.1)
        y = arrow(pos=(0,0,0), axis=(0,0,3), shaftwidth=0.1)
        z = arrow(pos=(0,0,0), axis=(0,3,0), shaftwidth=0.1)

    #self.observer().notify('rotated', sender = self, args = (previous_state, direction))
    def notify(self, notification, sender = None, args = None):

        if self.model is None and not sender is None:
            self.model = sender
        else:
            if self.model != sender:
                return
        if notification == 'bound_to_cube':
            self.bound_to_cube(sender)    
        if notification == 'rotated':
            #self.refresh_state(args[0])
            self.animate(args)
            #self.refresh_state(sender)


    def animate(self, args):
        if args[1] == 'L+': self.L_plus()
        if args[1] == 'R+': self.R_plus()
        if args[1] == 'B+': self.B_plus()
        if args[1] == 'F+': self.F_plus()
        if args[1] == 'U+': self.U_plus()
        if args[1] == 'D+': self.D_plus()
        if args[1] == 'L-': self.L_minus()
        if args[1] == 'R-': self.R_minus()
        if args[1] == 'B-': self.B_minus()
        if args[1] == 'F-': self.F_minus()
        if args[1] == 'U-': self.U_minus()
        if args[1] == 'D-': self.D_minus()
                    
    def init_drawing(self):
        color_height = 0.01
        color_wide = 0.9
        box_color = color.white
        box1 = box(pos=(-1-self.d,1+self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=box_color)
        box1_1 = box(pos=(box1.pos[0]-(self.arris/2.0),box1.pos[1],box1.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.blue)
        box1_2 = box(pos=(box1.pos[0],box1.pos[1]+(self.arris/2.0),box1.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box1_3 = box(pos=(box1.pos[0],box1.pos[1],box1.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box2 = box(pos=(0,1+self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=box_color)
        box2_1 = box(pos=(box2.pos[0],box2.pos[1]+(self.arris/2.0),box2.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box2_2 = box(pos=(box2.pos[0],box2.pos[1],box2.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box3 = box(pos=(1+self.d,1+self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=box_color)
        box3_1 = box(pos=(box3.pos[0]+(self.arris/2.0),box3.pos[1],box3.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box3_2 = box(pos=(box3.pos[0],box3.pos[1]+(self.arris/2.0),box3.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box3_3 = box(pos=(box3.pos[0],box3.pos[1],box3.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box4 = box(pos=(-1-self.d,0,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box4_1 = box(pos=(box4.pos[0]-(self.arris/2.0),box4.pos[1],box4.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.blue)
        box4_2 = box(pos=(box4.pos[0],box4.pos[1],box4.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box5 = box(pos=(0,0,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box5_1 = box(pos=(box5.pos[0],box5.pos[1],box5.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box6 = box(pos=(1+self.d,0,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box6_1 = box(pos=(box6.pos[0]+(self.arris/2.0),box6.pos[1],box6.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box6_2 = box(pos=(box6.pos[0],box6.pos[1],box6.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box7 = box(pos=(-1-self.d,-1-self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box7_1 = box(pos=(box7.pos[0]-(self.arris/2.0),box7.pos[1],box7.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.blue)
        box7_2 = box(pos=(box7.pos[0],box7.pos[1]-(self.arris/2.0),box7.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box7_3 = box(pos=(box7.pos[0],box7.pos[1],box7.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box8 = box(pos=(0,-1-self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box8_1 = box(pos=(box8.pos[0],box8.pos[1]-(self.arris/2.0),box8.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box8_2 = box(pos=(box8.pos[0],box8.pos[1],box8.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box9 = box(pos=(1+self.d,-1-self.d,1+self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box9_1 = box(pos=(box9.pos[0]+(self.arris/2.0),box9.pos[1],box9.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box9_2 = box(pos=(box9.pos[0],box9.pos[1]-(self.arris/2.0),box9.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box9_3 = box(pos=(box9.pos[0],box9.pos[1],box9.pos[2]+(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.red)
        box10 = box(pos=(-1-self.d,1+self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box10_1 = box(pos=(box10.pos[0]-(self.arris/2.0),box10.pos[1],box10.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.blue)
        box10_2 = box(pos=(box10.pos[0],box10.pos[1]+(self.arris/2.0),box10.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box11 = box(pos=(0,1+self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box11_1 = box(pos=(box11.pos[0],box11.pos[1]+(self.arris/2.0),box11.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box12 = box(pos=(1+self.d,1+self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box12_1 = box(pos=(box12.pos[0]+(self.arris/2.0),box12.pos[1],box12.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box12_2 = box(pos=(box12.pos[0],box12.pos[1]+(self.arris/2.0),box12.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box13 = box(pos=(-1-self.d,0,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box13_1 = box(pos=(box13.pos[0]-(self.arris/2.0),box13.pos[1],box13.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.blue)
        box14 = box(pos=(0,0,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=box_color)
        box15 = box(pos=(1+self.d,0,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box15_1 = box(pos=(box15.pos[0]+(self.arris/2.0),box15.pos[1],box15.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box16 = box(pos=(-1-self.d,-1-self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box16_1 = box(pos=(box16.pos[0]-(self.arris/2.0),box16.pos[1],box16.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.blue)
        box16_2 = box(pos=(box16.pos[0],box16.pos[1]-(self.arris/2.0),box16.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box17 = box(pos=(0,-1-self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box17_1 = box(pos=(box17.pos[0],box17.pos[1]-(self.arris/2.0),box17.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box18 = box(pos=(1+self.d,-1-self.d,0),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box18_1 = box(pos=(box18.pos[0]+(self.arris/2.0),box18.pos[1],box18.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box18_2 = box(pos=(box18.pos[0],box18.pos[1]-(self.arris/2.0),box18.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box19 = box(pos=(-1-self.d,1+self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box19_1 = box(pos=(box19.pos[0]-(self.arris/2.0),box19.pos[1],box19.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.blue)
        box19_2 = box(pos=(box19.pos[0],box19.pos[1]+(self.arris/2.0),box19.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box19_3 = box(pos=(box19.pos[0],box19.pos[1],box19.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.orange)
        box20 = box(pos=(0,1+self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box20_1 = box(pos=(box20.pos[0],box20.pos[1]+(self.arris/2.0),box20.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box20_2 = box(pos=(box20.pos[0],box20.pos[1],box20.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.orange)
        box21 = box(pos=(1+self.d,1+self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box21_1 = box(pos=(box21.pos[0]+(self.arris/2.0),box21.pos[1],box21.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box21_2 = box(pos=(box21.pos[0],box21.pos[1]+(self.arris/2.0),box21.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.yellow)
        box21_3 = box(pos=(box21.pos[0],box21.pos[1],box21.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.orange)
        box22 = box(pos=(-1-self.d,0,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box22_1 = box(pos=(box22.pos[0]-(self.arris/2.0),box22.pos[1],box22.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.blue)
        box22_2 = box(pos=(box22.pos[0],box22.pos[1],box22.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.orange)
        box23 = box(pos=(0,0,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box23_1 = box(pos=(box23.pos[0],box23.pos[1],box23.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.orange)
        box24 = box(pos=(1+self.d,0,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box24_1 = box(pos=(box24.pos[0]+(self.arris/2.0),box24.pos[1],box24.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box24_2 = box(pos=(box24.pos[0],box24.pos[1],box24.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.orange)
        box25 = box(pos=(-1-self.d,-1-self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=color.white)
        box25_1 = box(pos=(box25.pos[0]-(self.arris/2.0),box25.pos[1],box25.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.blue)
        box25_2 = box(pos=(box25.pos[0],box25.pos[1]-(self.arris/2.0),box25.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box25_3 = box(pos=(box25.pos[0],box25.pos[1],box25.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.orange)
        box26 = box(pos=(0,-1-self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=box_color)
        box26_1 = box(pos=(box26.pos[0],box26.pos[1]-(self.arris/2.0),box26.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box26_2 = box(pos=(box26.pos[0],box26.pos[1],box26.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.orange)
        box27 = box(pos=(1+self.d,-1-self.d,-1-self.d),
                   length=self.arris, height=self.arris, width=self.arris,
                   color=box_color)
        box27_1 = box(pos=(box27.pos[0]+(self.arris/2.0),box27.pos[1],box27.pos[2]),
                     length=color_height, height=color_wide, width=color_wide,
                     color=color.green)
        box27_2 = box(pos=(box27.pos[0],box27.pos[1]-(self.arris/2.0),box27.pos[2]),
                     length=color_wide, height=color_height, width=color_wide,
                     color=color.white)
        box27_3 = box(pos=(box27.pos[0],box27.pos[1],box27.pos[2]-(self.arris/2.0)),
                     length=color_wide, height=color_wide, width=color_height,
                     color=color.orange)
        
        self.cube[1] = [box1, box1_1, box1_2, box1_3]
        self.cube[2] = [box2, box2_1, box2_2]
        self.cube[3] = [box3, box3_1, box3_2, box3_3]
        self.cube[4] = [box4, box4_1, box4_2]
        self.cube[5] = [box5, box5_1]
        self.cube[6] = [box6, box6_1, box6_2]
        self.cube[7] = [box7, box7_1, box7_2, box7_3]
        self.cube[8] = [box8, box8_1, box8_2]
        self.cube[9] = [box9, box9_1, box9_2, box9_3]
        self.cube[10] = [box10, box10_1, box10_2]
        self.cube[11] = [box11, box11_1]
        self.cube[12] = [box12, box12_1, box12_2]
        self.cube[13] = [box13, box13_1]
        self.cube[14] = [box14]
        self.cube[15] = [box15, box15_1]
        self.cube[16] = [box16, box16_1, box16_2]
        self.cube[17] = [box17, box17_1]
        self.cube[18] = [box18, box18_1, box18_2]
        self.cube[19] = [box19, box19_1, box19_2, box19_3]
        self.cube[20] = [box20, box20_1, box20_2]
        self.cube[21] = [box21, box21_1, box21_2, box21_3]
        self.cube[22] = [box22, box22_1, box22_2]
        self.cube[23] = [box23, box23_1]
        self.cube[24] = [box24, box24_1, box24_2]
        self.cube[25] = [box25, box25_1, box25_2, box25_3]
        self.cube[26] = [box26, box26_1, box26_2]
        self.cube[27] = [box27, box27_1, box27_2, box27_3]
    
    def refresh_state(self, cube):
        color_cube = {'back':[[],[],[]],
                      'bottom':[[],[],[]],
                      'front':[[],[],[]],
                      'left':[[],[],[]],
                      'right':[[],[],[]],
                      'top':[[],[],[]]}
        # Set colors instead of strings
        for key in cube.fringe.keys():
            for i in range(3):
                for j in range(3):
                    if cube.fringe[key][i][j][0] == 'F':
                        color_cube[key][i].append(color.red)#[j] = color.red
                    if cube.fringe[key][i][j][0] == 'R':
                        color_cube[key][i].append(color.green)#[j] = color.green
                    if cube.fringe[key][i][j][0] == 'L':
                        color_cube[key][i].append(color.blue)#[j] = color.blue
                    if cube.fringe[key][i][j][0] == 'T':
                        color_cube[key][i].append(color.yellow)#[j] = color.yellow
                    if cube.fringe[key][i][j][0] == 'b':
                        color_cube[key][i].append(color.white)#[j] = color.white
                    if cube.fringe[key][i][j][0] == 'B':
                        color_cube[key][i].append(color.orange)#[j] = color.orange
        # Create self.cube dictionary
        proxy_cube = {'back':[[self.cube[25][3],self.cube[26][2],self.cube[27][3]],
                               [self.cube[22][2],self.cube[23][1],self.cube[24][2]],
                               [self.cube[19][3],self.cube[20][2],self.cube[21][3]]],
                      'bottom':[[self.cube[7][2],self.cube[8][1],self.cube[9][2]],
                               [self.cube[16][2],self.cube[17][1],self.cube[18][2]],
                               [self.cube[25][2],self.cube[26][1],self.cube[27][2]]],
                      'front':[[self.cube[1][3],self.cube[2][2],self.cube[3][3]],
                               [self.cube[4][2],self.cube[5][1],self.cube[6][2]],
                               [self.cube[7][3],self.cube[8][2],self.cube[9][3]]],
                      'left':[[self.cube[19][1],self.cube[10][1],self.cube[1][1]],
                               [self.cube[22][1],self.cube[13][1],self.cube[4][1]],
                               [self.cube[25][1],self.cube[16][1],self.cube[7][1]]],
                      'right':[[self.cube[3][1],self.cube[12][1],self.cube[21][1]],
                               [self.cube[6][1],self.cube[15][1],self.cube[24][1]],
                               [self.cube[9][1],self.cube[18][1],self.cube[27][1]]],
                      'top':[[self.cube[19][2],self.cube[20][1],self.cube[21][2]],
                               [self.cube[10][2],self.cube[11][1],self.cube[12][2]],
                               [self.cube[1][2],self.cube[2][1],self.cube[3][2]]]
                      }
        # Map cube color dict to proxy_cube colors
        for key in proxy_cube.keys():
            for i in range(3):
                for j in range(3):
                    proxy_cube[key][i][j].color = color_cube[key][i][j]

    
    def bound_to_cube(self, cube):
        self.refresh_state(cube)
        
    
    def rotate_X_plus(self, figure):
        figure.rotate(angle=-pi/(self.range_rotate*2), axis=vector((1,0,0)),
            origin=(0,0,0))
    def rotate_Y_plus(self, figure):
        figure.rotate(angle=-pi/(self.range_rotate*2), axis=vector((0,0,1)),
            origin=(0,0,0))
    def rotate_Z_plus(self, figure):
        figure.rotate(angle=pi/(self.range_rotate*2), axis=vector((0,1,0)),
            origin=(0,0,0))
    def rotate_X_minus(self, figure):
        figure.rotate(angle=pi/(self.range_rotate*2), axis=vector((1,0,0)),
            origin=(0,0,0))
    def rotate_Y_minus(self, figure):
        figure.rotate(angle=pi/(self.range_rotate*2), axis=vector((0,0,1)),
            origin=(0,0,0))
    def rotate_Z_minus(self, figure):
        figure.rotate(angle=-pi/(self.range_rotate*2), axis=vector((0,10,0)),
            origin=(0,0,0))
    
    def L_plus(self):
        side_list = [1, 4, 7, 10, 13, 16, 19, 22, 25]
        cube_list = [self.cube[i] for i in side_list]
        box_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for cube in box_list:
                self.rotate_X_plus(cube)
        new_cube_list = {1:self.cube[7], 4:self.cube[16], 7:self.cube[25],
                         10:self.cube[4], 13:self.cube[13], 16:self.cube[22],
                         19:self.cube[1], 22:self.cube[10], 25:self.cube[19]}
        for key in new_cube_list.keys():
            self.cube[key]=new_cube_list[key]

    def R_plus(self):
        side_list = [3, 6, 9, 12, 15, 18, 21, 24, 27]
        cube_list = [self.cube[i] for i in side_list]
        box_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for cube in box_list:
                self.rotate_X_plus(cube)
        new_cube_list = {3:self.cube[9], 12:self.cube[6], 21:self.cube[3],
                         6:self.cube[18], 15:self.cube[15], 24:self.cube[12],
                         9:self.cube[27], 18:self.cube[24], 27:self.cube[21]}
        for key in new_cube_list.keys():
            self.cube[key]=new_cube_list[key]

    def B_plus(self):
        side_list = [19, 20, 21, 22, 23, 24, 25, 26, 27]
        cube_list = [self.cube[i] for i in side_list]
        box_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for cube in box_list:
                self.rotate_Y_plus(cube)
        new_cube_list = {19:self.cube[25], 20:self.cube[22], 21:self.cube[19],
                         22:self.cube[26], 23:self.cube[23], 24:self.cube[20],
                         25:self.cube[27], 26:self.cube[24], 27:self.cube[21]}
        for key in new_cube_list.keys():
            self.cube[key]=new_cube_list[key]

    def F_plus(self):
        side_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        cube_list = [self.cube[i] for i in side_list]
        box_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for cube in box_list:
                self.rotate_Y_plus(cube)
        new_cube_list = {1:self.cube[7], 2:self.cube[4], 3:self.cube[1],
                         4:self.cube[8], 5:self.cube[5], 6:self.cube[2],
                         7:self.cube[9], 8:self.cube[6], 9:self.cube[3]}
        for key in new_cube_list.keys():
            self.cube[key]=new_cube_list[key]

    def U_plus(self):
        side_list = [1, 2, 3, 10, 11, 12, 19, 20, 21]
        cube_list = [self.cube[i] for i in side_list]
        box_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for cube in box_list:
                self.rotate_Z_plus(cube)
        new_cube_list = {3:self.cube[1], 2:self.cube[10], 1:self.cube[19],
                         12:self.cube[2], 11:self.cube[11], 10:self.cube[20],
                         21:self.cube[3], 20:self.cube[12], 19:self.cube[21]}
        for key in new_cube_list.keys():
            self.cube[key]=new_cube_list[key]
    
    def D_plus(self):
        side_list = [7, 8, 9, 16, 17, 18, 25, 26, 27]
        cube_list = [self.cube[i] for i in side_list]
        box_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for cube in box_list:
                self.rotate_Z_plus(cube)
        new_cube_list = {7:self.cube[25], 8:self.cube[16], 9:self.cube[7],
                         16:self.cube[26], 17:self.cube[17], 18:self.cube[8],
                         25:self.cube[27], 26:self.cube[18], 27:self.cube[9]}
        for key in new_cube_list.keys():
            self.cube[key]=new_cube_list[key]

    def L_minus(self):
        side_list = [1, 4, 7, 10, 13, 16, 19, 22, 25]
        cube_list = [self.cube[i] for i in side_list]
        box_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for cube in box_list:
                self.rotate_X_minus(cube)
        new_cube_list = {1:self.cube[19], 4:self.cube[10], 7:self.cube[1],
                         10:self.cube[22], 13:self.cube[13], 16:self.cube[4],
                         19:self.cube[25], 22:self.cube[16], 25:self.cube[7]}
        for key in new_cube_list.keys():
            self.cube[key]=new_cube_list[key]

    def R_minus(self):
        side_list = [3, 6, 9, 12, 15, 18, 21, 24, 27]
        cube_list = [self.cube[i] for i in side_list]
        box_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for cube in box_list:
                self.rotate_X_minus(cube)
        new_cube_list = {3:self.cube[21], 12:self.cube[24], 21:self.cube[27],
                         6:self.cube[12], 15:self.cube[15], 24:self.cube[18],
                         9:self.cube[3], 18:self.cube[6], 27:self.cube[9]}
        for key in new_cube_list.keys():
            self.cube[key]=new_cube_list[key]

    def B_minus(self):
        side_list = [19, 20, 21, 22, 23, 24, 25, 26, 27]
        cube_list = [self.cube[i] for i in side_list]
        box_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for cube in box_list:
                self.rotate_Y_minus(cube)
        new_cube_list = {19:self.cube[21], 20:self.cube[24], 21:self.cube[27],
                         22:self.cube[20], 23:self.cube[23], 24:self.cube[26],
                         25:self.cube[19], 26:self.cube[22], 27:self.cube[25]}
        for key in new_cube_list.keys():
            self.cube[key]=new_cube_list[key]

    def F_minus(self):
        side_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        cube_list = [self.cube[i] for i in side_list]
        box_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for cube in box_list:
                self.rotate_Y_minus(cube)
        new_cube_list = {1:self.cube[3], 2:self.cube[6], 3:self.cube[9],
                         4:self.cube[2], 5:self.cube[5], 6:self.cube[8],
                         7:self.cube[1], 8:self.cube[4], 9:self.cube[7]}
        for key in new_cube_list.keys():
            self.cube[key]=new_cube_list[key]

    def U_minus(self):
        side_list = [1, 2, 3, 10, 11, 12, 19, 20, 21]
        cube_list = [self.cube[i] for i in side_list]
        box_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for cube in box_list:
                self.rotate_Z_minus(cube)
        new_cube_list = {3:self.cube[21], 2:self.cube[12], 1:self.cube[3],
                         12:self.cube[20], 11:self.cube[11], 10:self.cube[2],
                         21:self.cube[19], 20:self.cube[10], 19:self.cube[1]}
        for key in new_cube_list.keys():
            self.cube[key]=new_cube_list[key]
    
    def D_minus(self):
        side_list = [7, 8, 9, 16, 17, 18, 25, 26, 27]
        cube_list = [self.cube[i] for i in side_list]
        box_list = [j for i in cube_list for j in i]
        for i in range(self.range_rotate):
            rate(self.speed_rotate)
            for cube in box_list:
                self.rotate_Z_minus(cube)
        new_cube_list = {7:self.cube[9], 8:self.cube[18], 9:self.cube[27],
                         16:self.cube[8], 17:self.cube[17], 18:self.cube[26],
                         25:self.cube[7], 26:self.cube[16], 27:self.cube[25]}
        for key in new_cube_list.keys():
            self.cube[key]=new_cube_list[key]
            