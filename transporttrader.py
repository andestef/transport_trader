import os
import random
import json
from math import ceil
data = {
'loc':['Charlie','Zeroton Creek'],

'towns':["Echelon One","Nova Junction","Ionvale Depot",'Zeroton Creek',"Dustmarch","Muckspur Terminal"],

'all_towns':["Echelon One","Nova Junction","Ionvale Depot",'Zeroton Creek',"Dustmarch","Muckspur Terminal","Zenith"],

'town_data':{
	"Echelon One":{"size":25,"highway_to":["Nova Junction","Zenith","Zeroton Creek"]},
	"Nova Junction":{"size":20,"highway_to":["Echelon One","Ionvale Depot"]},
	"Ionvale Depot":{"size":13,"highway_to":["Nova Junction","Zeroton Creek"]},
	"Zeroton Creek":{"size":10,"highway_to":["Ionvale Depot","Muckspur Terminal","Echelon One"]},
	"Dustmarch":{"size":7,"highway_to":["Echelon One","Muckspur Terminal"]},
	"Muckspur Terminal":{"size":15,"highway_to":["Zeroton Creek","Dustmarch","Zenith"]},
	"Zenith":{"size":35,"highway_to":["Nova Junction","Muckspur Terminal"]}
},
'highways':{
	"Route 25":{
		"stops":{"Echelon One":{"distance":60,"speed":60},"Nova Junction":{"distance":100,"speed":60},"Ionvale Depot":{"distance":80,"speed":70},"Zeroton Creek":{"distance":0,"speed":0}}
	},
	"Route 74":{
		"stops":{"Echelon One":{"distance":120,"speed":75},"Zeroton Creek":{"distance":0,"speed":0}}
	},
	"Route 50":{
		"stops":{"Zeroton Creek":{"distance":120,"speed":65},"Muckspur Terminal":{"distance":150,"speed":75},"Dustmarch":{"distance":0,"speed":0}}
	},
	"Route 88":{
		"stops":{"Zeroton Creek":{"distance":200,"speed":90},"Dustmarch":{"distance":0,"speed":0}}
	},
	"Freeway 101":{
		"stops":{"Echelon One":{"distance":150,"speed":120},"Zenith":{"distance":0,"speed":0},"Muckspur Terminal":{"distance":0,"speed":0}}
	},
},

"maps":{
"Charlie":"""
              Quadrant Charlie
            F101              R25
    Z=========X=========E1-----------NJ
    ||  1      130Mi     | 1  60Mi  1 |
  F ||  4              R | 2        0 |  R
  1 XX  0              7 | 0        0 |  2
  0 ||  M              4 | M        M |  5            
  1 ||  i                | i   R25  i |      
    ||       R50         |   /--------ID
    MT-------------------ZC--  80Mi
     | 1    120Mi       /
  R  | 5             i /            |                  KEY                      |
  5  | 0            M / R           | Z: Zenith; E1: Echelon One                |
  0  | M           0 / 8            | NJ: Nova Junction; ID: Ionvale Depot      |
     | i         20 / 8             | ZC: Zeroton Creek; DM: Dustmarch          |
    DM--------------                | MT: Muckspur Terminal                     |
            R88                     | R: Route F: Freeway  [X]Mi: Distance (Mi) |
                                    | X Through Highway Indicates Closed        |
                                    | NOTE: Map Not to Scale. Distances Approx. | 
"""
},

"mapdata":{"Charlie":['\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', 'u', 'a', 'd', 'r', 'a', 'n', 't', ' ', 'C', 'h', 'a', 'r', 'l', 'i', 'e', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'F', '1', '0', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R', '2', '5', '\n', ' ', ' ', ' ', ' ', ['town', 'Zenith', '', '', 1], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['freeway', 'F101', 'Zenith', 'Echelon One', 19], ['town', 'Echelon One', '', '', 2], ['town', 'Echelon One', '', '', 2], ['route', 'R25', 'Echelon One', 'Nova Junction', 11], ['route', 'R25', 'Echelon One', 'Nova Junction', 11], ['route', 'R25', 'Echelon One', 'Nova Junction', 11], ['route', 'R25', 'Echelon One', 'Nova Junction', 11], ['route', 'R25', 'Echelon One', 'Nova Junction', 11], ['route', 'R25', 'Echelon One', 'Nova Junction', 11], ['route', 'R25', 'Echelon One', 'Nova Junction', 11], ['route', 'R25', 'Echelon One', 'Nova Junction', 11], ['route', 'R25', 'Echelon One', 'Nova Junction', 11], ['route', 'R25', 'Echelon One', 'Nova Junction', 11], ['route', 'R25', 'Echelon One', 'Nova Junction', 11], ['town', 'Nova Junction', '', '', 2], ['town', 'Nova Junction', '', '', 2], '\n', ' ', ' ', ' ', ' ', ['freeway', 'F101', 'Zenith', 'Muckspur Terminal', 13], ['freeway', 'F101', 'Zenith', 'Muckspur Terminal', 13], ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', '1', '3', '0', 'M', 'i', ' ', ' ', ' ', ' ', ' ', ['freeway', 'F101', 'Zenith', 'Muckspur Terminal', 13], ' ', '1', ' ', ' ', '6', '0', 'M', 'i', ' ', ' ', '1', ' ', ['route', 'R25', 'Nova Junction', 'Ionvale Depot', 5], '\n', ' ', ' ', 'F', ' ', ['freeway', 'F101', 'Zenith', 'Muckspur Terminal', 13], ['freeway', 'F101', 'Zenith', 'Muckspur Terminal', 13], ' ', ' ', '4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R', ' ', ['route', 'R74', 'Echelon One', 'Zeroton Creek', 5], ' ', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', ' ', ['route', 'R25', 'Nova Junction', 'Ionvale Depot', 5], ' ', ' ', 'R', '\n', ' ', ' ', '1', ' ', ['freeway', 'F101', 'Zenith', 'Muckspur Terminal', 13], ['freeway', 'F101', 'Zenith', 'Muckspur Terminal', 13], ' ', ' ', '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '7', ' ', ['route', 'R74', 'Echelon One', 'Zeroton Creek', 5], ' ', '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', ' ', ['route', 'R25', 'Nova Junction', 'Ionvale Depot', 5], ' ', ' ', '2', '\n', ' ', ' ', '0', ' ', ['freeway', 'F101', 'Zenith', 'Muckspur Terminal', 13], ['freeway', 'F101', 'Zenith', 'Muckspur Terminal', 13], ' ', ' ', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '4', ' ', ['route', 'R74', 'Echelon One', 'Zeroton Creek', 5], ' ', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', ' ', ['route', 'R25', 'Nova Junction', 'Ionvale Depot', 5], ' ', ' ', '5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', '1', ' ', ['freeway', 'F101', 'Zenith', 'Muckspur Terminal', 13], ['freeway', 'F101', 'Zenith', 'Muckspur Terminal', 13], ' ', ' ', 'i', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ['route', 'R74', 'Echelon One', 'Zeroton Creek', 5], ' ', 'i', ' ', ' ', ' ', 'R', '2', '5', ' ', ' ', 'i', ' ', ['route', 'R25', 'Nova Junction', 'Ionvale Depot', 5], ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ['freeway', 'F101', 'Zenith', 'Muckspur Terminal', 13], ['freeway', 'F101', 'Zenith', 'Muckspur Terminal', 13], ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R', '5', '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ['route', 'R74', 'Echelon One', 'Zeroton Creek', 5], ' ', ' ', ' ', ['route', 'R25', 'Zeroton Creek', 'Ionvale Depot', 11], ['route', 'R25', 'Zeroton Creek', 'Ionvale Depot', 11], ['route', 'R25', 'Zeroton Creek', 'Ionvale Depot', 11], ['route', 'R25', 'Zeroton Creek', 'Ionvale Depot', 11], ['route', 'R25', 'Zeroton Creek', 'Ionvale Depot', 11], ['route', 'R25', 'Zeroton Creek', 'Ionvale Depot', 11], ['route', 'R25', 'Zeroton Creek', 'Ionvale Depot', 11], ['route', 'R25', 'Zeroton Creek', 'Ionvale Depot', 11], ['route', 'R25', 'Zeroton Creek', 'Ionvale Depot', 11], ['town', 'Ionvale Depot', '', '', 2], ['town', 'Ionvale Depot', '', '', 2], '\n', ' ', ' ', ' ', ' ', ['town', 'Muckspur Terminal', '', '', 2], ['town', 'Muckspur Terminal', '', '', 2], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['route', 'R50', 'Muckspur Terminal', 'Zeroton Creek', 19], ['town', 'Zeroton Creek', '', '', 2], ['town', 'Zeroton Creek', '', '', 2], ['route', 'R25', 'Zeroton Creek', 'Ionvale Depot', 11], ['route', 'R25', 'Zeroton Creek', 'Ionvale Depot', 11], ' ', ' ', '8', '0', 'M', 'i', '\n', ' ', ' ', ' ', ' ', ' ', ['route', 'R50', 'Muckspur Terminal', 'Dustmarch', 5], ' ', '1', ' ', ' ', ' ', ' ', '1', '2', '0', 'M', 'i', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], '\n', ' ', ' ', 'R', ' ', ' ', ['route', 'R50', 'Muckspur Terminal', 'Dustmarch', 5], ' ', '5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'i', ' ', ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K', 'E', 'Y', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\n', ' ', ' ', '5', ' ', ' ', ['route', 'R50', 'Muckspur Terminal', 'Dustmarch', 5], ' ', '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', ' ', ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ' ', 'R', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', 'Z', ':', ' ', 'Z', 'e', 'n', 'i', 't', 'h', ';', ' ', 'E', '1', ':', ' ', 'E', 'c', 'h', 'e', 'l', 'o', 'n', ' ', 'O', 'n', 'e', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\n', ' ', ' ', '0', ' ', ' ', ['route', 'R50', 'Muckspur Terminal', 'Dustmarch', 5], ' ', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', ' ', ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', 'N', 'J', ':', ' ', 'N', 'o', 'v', 'a', ' ', 'J', 'u', 'n', 'c', 't', 'i', 'o', 'n', ';', ' ', 'I', 'D', ':', ' ', 'I', 'o', 'n', 'v', 'a', 'l', 'e', ' ', 'D', 'e', 'p', 'o', 't', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', ' ', ['route', 'R50', 'Muckspur Terminal', 'Dustmarch', 5], ' ', 'i', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2', '0', ' ', ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ' ', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', 'Z', 'C', ':', ' ', 'Z', 'e', 'r', 'o', 't', 'o', 'n', ' ', 'C', 'r', 'e', 'e', 'k', ';', ' ', 'D', 'M', ':', ' ', 'D', 'u', 's', 't', 'm', 'a', 'r', 'c', 'h', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', ['town', 'Dustmarch', '', '', 2], ['town', 'Dustmarch', '', '', 2], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ['route', 'R88', 'Dustmarch', 'Zeroton Creek', 19], ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', 'M', 'T', ':', ' ', 'M', 'u', 'c', 'k', 's', 'p', 'u', 'r', ' ', 'T', 'e', 'r', 'm', 'i', 'n', 'a', 'l', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', 'R', ':', ' ', 'R', 'o', 'u', 't', 'e', ' ', 'F', ':', ' ', 'F', 'r', 'e', 'e', 'w', 'a', 'y', ' ', ' ', '[', 'X', ']', 'M', 'i', ':', ' ', 'D', 'i', 's', 't', 'a', 'n', 'c', 'e', ' ', '(', 'M', 'i', ')', ' ', '|', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', 'X', ' ', 'T', 'h', 'r', 'o', 'u', 'g', 'h', ' ', 'H', 'i', 'g', 'h', 'w', 'a', 'y', ' ', 'I', 'n', 'd', 'i', 'c', 'a', 't', 'e', 's', ' ', 'C', 'l', 'o', 's', 'e', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', 'N', 'O', 'T', 'E', ':', ' ', 'M', 'a', 'p', ' ', 'N', 'o', 't', ' ', 't', 'o', ' ', 'S', 'c', 'a', 'l', 'e', '.', ' ', 'D', 'i', 's', 't', 'a', 'n', 'c', 'e', 's', ' ', 'A', 'p', 'p', 'r', 'o', 'x', '.', ' ', '|', ' ', '\n']},
'stock':{},

'goods_types':["Food and Water"],

'goods_regular':{
	"Water":{"type":"Food and Water","avg":250,"rarity":10},
	"Beef":{"type":"Food and Water","avg":500,"rarity":2},
	"Fish":{"type":"Food and Water","avg":550,"rarity":2},
	"Rice":{"type":"Food and Water","avg":350,"rarity":5},
	"Wheat":{"type":"Food and Water","avg":350,"rarity":6},
	"Corn":{"type":"Food and Water","avg":400,"rarity":4},
	"Potatoes":{"type":"Food and Water","avg":375,"rarity":4},
	"Canned Food":{"type":"Food and Water","avg":400,"rarity":7}
},

'prices':{},

'cargo':[],

'credits':5000
}
def gen():
	prbList = []
	for i in data['goods_regular']:
		prbList.extend([i] * data['goods_regular'][i]['rarity'])
	for i in data['towns']:
		data['stock'][i] = []
		for j in range(data["town_data"][i]['size']):
			data['stock'][i].append(random.choice(prbList))
		data['stock'][i].sort()
		data["prices"][i] = {}
		for j in data['goods_types']:
			change = ceil(random.gauss(0, 10))
			data['prices'][i][j] = change
def start_menu():
	print("Transport Trader\nVersion 1.0\nCopyright (c) 2025 Alexander DeStefano\n1. Load Game\n2. New Game\n3. Exit")
	choice = input(":")
	if choice == "1":
		pass
	elif choice == "2":
		gen()
		menu()
	elif choice == "3":
		exit()
def print_enter(*args,**kwargs):
	print(*args, **kwargs)
	input("Press Enter to continue...\n")
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
def prettify_stock(val,sect,number=False):
	it = {}
	for i in sect:
		if val.count(i) != 0:
			it[i] = val.count(i)
	c = 1
	for i,t in it.items():
		price = data['goods_regular'][i]['avg']
		if data['prices'][data['loc'][1]][data['goods_regular'][i]['type']] > 0:
			price += ceil(price * (data['prices'][data['loc'][1]][data['goods_regular'][i]['type']] / 100))
		elif data['prices'][data['loc'][1]][data['goods_regular'][i]['type']] < 0:
			price -= ceil(price * (abs(data['prices'][data['loc'][1]][data['goods_regular'][i]['type']]) / 100))
		if t > 1:
			print(f"    {str(c)+'.'+' ' if number else ''}{i}: {t} units ({price} credits:",end='')

		else:
			print(f"    {str(c)+'.'+' ' if number else ''}{i}: {t} unit ({price} credits:",end='')
		if data['prices'][data['loc'][1]][data['goods_regular'][i]['type']] > 0:
			print(f" UP {data['prices'][data['loc'][1]][data['goods_regular'][i]['type']]}%)")
		elif data['prices'][data['loc'][1]][data['goods_regular'][i]['type']] == 0:
			print(" 0%)")
		else:
			print(f" DOWN {abs(data['prices'][data['loc'][1]][data['goods_regular'][i]['type']])}%)")
		c += 1
	return it
def view_prices():
	clear()
	print(f"Transport Trader - Prices\nYou are in Quadrant {data['loc'][0]}: {data['loc'][1]}")
	for t in data['towns']:
		print("Prices in",t + ":")
		vals = {}
		for i in data['prices'][t]:
			vals[i] = data['prices'][t][i]
		vals = sorted(vals.items(), reverse=True)
		for i in vals:
			if i[1] > 0:
				print(f"\t{i[0]}: UP {i[1]}%")
			elif i[1] == 0:
				print(f"\t{i[0]}: 0%")
			else:
				print(f"\t{i[0]}: DOWN {abs(i[1])}%")
		print()
	print_enter()
def view_cargo():
	clear()
	print(f"Transport Trader - Cargo\nYou are in Quadrant {data['loc'][0]}: {data['loc'][1]}")
	if len(data['cargo']) == 0:
		print("You have no cargo.")
	else:
		print("Your cargo:")
		prettify_stock(data['cargo'], data['goods_regular'])
	print_enter()
def buy_goods():
	clear()
	print(f"Transport Trader - Buy Goods\nYou are in Quadrant {data['loc'][0]}: {data['loc'][1]}")
	print("Available goods:")
	it = prettify_stock(data['stock'][data['loc'][1]], data['goods_regular'],True)
	print(f"    {len(it)+1}. Exit Shop")
	print(f"You have {data['credits']} credits.")
	print("\nWhat would you like to buy?")
	c = input(":").strip()
	if not c.isdigit():
		buy_goods()
		return
	c = int(c)-1
	if c == len(it):
		return
	elif c > len(it):
		buy_goods()
		return
	choice = list(it.keys())[c]
	price = data['goods_regular'][choice]['avg']
	if data['prices'][data['loc'][1]][data['goods_regular'][choice]['type']] > 0:
		price += ceil(price * (data['prices'][data['loc'][1]][data['goods_regular'][choice]['type']] / 100))
	elif data['prices'][data['loc'][1]][data['goods_regular'][choice]['type']] < 0:
		price -= ceil(price * (abs(data['prices'][data['loc'][1]][data['goods_regular'][choice]['type']]) / 100))
	print(f"How many units would you like to buy? (1 unit = {price} credits)\nYou can buy {it[choice]} units of {choice}.")
	amount = input(":").strip()
	if not amount.isdigit():
		buy_goods()
		return
	else:
		amount = int(amount)
	if amount < 1:
		print_enter("You must buy at least 1 unit of an item.")
		buy_goods()
		return
	if amount > it[choice]:
		print_enter(f"You can only buy {it[choice]} units of {choice}.")
		buy_goods()
		return
	price *= amount
	if data['credits'] < price:
		print_enter("You do not have enough credits to buy this item.")
		buy_goods()
		return
	data['credits'] -= price
	for i in range(amount):
		data['stock'][data['loc'][1]].remove(choice)
		data['cargo'].append(choice)
	print_enter(f"You bought {amount} unit{'s' if amount > 1 else ''} of {choice} for {price} credits. You now have {data['credits']} credits left.")
def sell_goods():
	clear()
	print(f"Transport Trader - Sell Goods\nYou are in Quadrant {data['loc'][0]}: {data['loc'][1]}")
	if len(data['cargo']) == 0:
		print("You have no cargo to sell.")
		print_enter()
		return
	print("Your cargo:")
	it = prettify_stock(data['cargo'], data['goods_regular'],True)
	print(f"    {len(it)+1}. Exit Shop")
	print(f"You have {data['credits']} credits.")
	print("What would you like to sell?")
	c = input(":").strip()
	if not c.isdigit():
		sell_goods()
		return
	c = int(c)-1
	if c == len(it):
		return
	elif c > len(it):
		sell_goods()
		return
	choice = list(it.keys())[c]
	price = data['goods_regular'][choice]['avg']
	if data['prices'][data['loc'][1]][data['goods_regular'][choice]['type']] > 0:
		price += ceil(price * (data['prices'][data['loc'][1]][data['goods_regular'][choice]['type']] / 100))
	elif data['prices'][data['loc'][1]][data['goods_regular'][choice]['type']] < 0:
		price -= ceil(price * (abs(data['prices'][data['loc'][1]][data['goods_regular'][choice]['type']]) / 100))
	print(f"How many units would you like to sell? (1 unit = {price} credits)\nYou can sell {it[choice]} units of {choice}.")
	amount = input(":").strip()
	if not amount.isdigit():
		sell_goods()
		return
	else:
		amount = int(amount)
	if amount < 1:
		print_enter("You must sell at least 1 unit of an item.")
		sell_goods()
		return
	if amount > it[choice]:
		print_enter(f"You can only sell {it[choice]} units of {choice}.")
		sell_goods()
		return
	price *= amount
	data['credits'] += price
	for i in range(amount):
		data['cargo'].remove(choice)
		data['stock'][data['loc'][1]].append(choice)
	data['stock'][data['loc'][1]].sort()
	print_enter(f"You sold {amount} unit{'s' if amount > 1 else ''} of {choice} for {price} credits. You now have {data['credits']} credits.")
def shop():
	clear()
	print(f"Transport Trader - Shop\nYou are in Quadrant {data['loc'][0]}: {data['loc'][1]}")
	print("Prices in",data['loc'][1] + ":")
	vals = {}
	for i in data['prices'][data['loc'][1]]:
		vals[i] = data['prices'][data['loc'][1]][i]
	vals = sorted(vals.items(), reverse=True)
	for i in vals:
		if i[1] > 0:
			print(f"\t{i[0]}: UP {i[1]}%")
		elif i[1] == 0:
			print(f"\t{i[0]}: 0%")
		else:
			print(f"\t{i[0]}: DOWN {abs(i[1])}%")
	print("\nWhat would you like to do?")
	print("1. Buy Goods")
	print("2. Sell Goods")
	print("3. Exit Shop")
	choice = input(":")
	if choice == "1":
		buy_goods()
	elif choice == "2":
		sell_goods()
	elif choice == "3":
		return
	else:
		print_enter("Invalid choice, please try again.")
		shop()
def travel():
	clear()
	print(f"Transport Trader - Travel\nYou are in Quadrant {data['loc'][0]}: {data['loc'][1]}")
	print(data['maps'][data['loc'][0]])
	print("Available routes:")
	c = 0
	locs = []
	for i,d in data['highways'].items():
		ld = list(d['stops'].keys())
		if data['loc'][1] in ld:
			e = ld.index(data['loc'][1])
			if d['stops'][ld[e]] != {"distance":0,"speed":0}:
				c += 1
				print(f"    {c}. {i} to {ld[e+1]}: {d['stops'][data['loc'][1]]['distance']} miles at {d['stops'][data['loc'][1]]['speed']} mph")
				locs.append([i,ld[e+1]])
			if e != 0:
				c += 1
				print(f"    {c}. {i} to {ld[e-1]}: {d['stops'][ld[e-1]]['distance']} miles at {d['stops'][ld[e-1]]['speed']} mph")
				locs.append([i,ld[e-1]])
	c += 1
	print(f"    {c}. Exit Travel")
	destination = input(":")
def menu():
	clear()
	print(f"Transport Trader\nYou are in Quadrant {data['loc'][0]}: {data['loc'][1]}\n1. View Prices\n2. View Cargo\n3. Shop\n4. Travel\n5. Jobs\n6. Menu")
	choice = input(":")
	if choice == "1":
		view_prices()
	elif choice == "2":
		view_cargo()
	elif choice == "3":
		shop()
	elif choice == "4":
		travel()
		'''elif choice == "5":
		jobs()'''
	elif choice == "6":
		start_menu()
	else:
		print_enter("Invalid choice, please try again.")
		menu()
	menu()
#start_menu()
print(data['maps']['Charlie'])
loc = data['mapdata']['Charlie'].index(['route', 'R25', 'Echelon One', 'Nova Junction', 1])