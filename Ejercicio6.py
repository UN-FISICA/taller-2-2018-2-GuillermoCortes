#!/usr/bin/python
# -*- coding: utf8-*-
import turtle
import math
from turtle import *
title("Ejercicio 5")
penup()
goto(-100,-200)
pendown()
turtle.backward
y=input('Escriba el numero de filas: ')
def pol(l,f):
  h=1
  while(h<=l):
    turtle.forward(10*math.sqrt(2(1-math.cos((2*math.pi)/(f+2)))))
    turtle.left(360/l)
    h=h+1
def fila(l,f):
  g=1
  while(g<=f):
    pol(l,f)
    penup()
    turtle.forward((10*math.sqrt(2(1-math.cos((2*math.pi)/(f+2)))))+20)
    pendown()
    g=g+1
 s=y
 while(s>=1):
  fila(s+2,s)
  turtle.left(180)
  penup()
  turtle.forward((s-1)*)
  turtle.left(180)
  turtle.forward(15)
  turtle.left(90)
  turtle.forward(30)
  turtle.right(90)
  pendown()
  s=s-1
 raw_input("Pulse una tecla para continuar..") 
