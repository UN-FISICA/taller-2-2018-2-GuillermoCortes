#!/usr/bin/python
# -*- coding: UTF-8-*-
import turtle
from turtle import *

title("Ejercicio 1")
penup()
goto(-100,-200)
pendown()
turtle.backward
def polpeq1(l):
	g=1
	while (g<=l):
		turtle.forward(50)
		turtle.left(360/l)
		g=g+1

def polgrande(l,m):
	h=1
	while(h<=m):
		polpeq1(l)
		penup()
		turtle.forward(150)
		pendown()
		turtle.left(360/m)
		h=h+1	
polgrande(4,4)
raw_input("Pulse una tecla para continuar..")
