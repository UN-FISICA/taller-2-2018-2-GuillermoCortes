#!/usr/bin/python
# -*- coding: utf8-*-
import turtle
from turtle import *
title("Ejercicio 4")
penup()
goto(-100,-200)
pendown()
turtle.backward
x=input('Escriba el numero de lados de los poligonos: ')
y=input('Escriba el numero de filas: ')
def pol(l):
  h=1
  while(h<=l):
    turtle.forward(20)
    turtle.left(360/l)
    h=h+1
def fila(l,f):
  g=1
  while(g<=f):
    pol(l)
    penup()
    turtle.forward(30)
    pendown()
    g=g+1
 s=y
 while(s>=1):
  fila(x,s)
  turtle.left(180)
  penup()
  turtle.forward((s-1)*30)
  turtle.left(180)
  turtle.forward(15)
  turtle.left(90)
  turtle.forward(30)
  turtle.right(90)
  pendown()
  s=s-1
 raw_input("Pulse una tecla para continuar..") 
