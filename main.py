import vk_api,time,requests,colorama,os
from colorama import Fore,Back,Style
colorama.init()

priva = ["""
██████╗░░█████╗░██████╗░░██████╗░██████╗████████╗██╗░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝██║██╔══██╗██║░██╔╝
██████╔╝███████║██████╔╝╚█████╗░╚█████╗░░░░██║░░░██║██║░░╚═╝█████═╝░
██╔═══╝░██╔══██║██╔══██╗░╚═══██╗░╚═══██╗░░░██║░░░██║██║░░██╗██╔═██╗░
██║░░░░░██║░░██║██║░░██║██████╔╝██████╔╝░░░██║░░░██║╚█████╔╝██║░╚██╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝
                           Owner: @chmotie
                           Group: @scripts_xxx
                           Version: 0.1
 1) Включить парсер
 2)В разработке...
"""                          
]
print(Fore.GREEN + priva[0])
parserv = input("->")

if parserv == "1":
	parse = [i for i in range(19415)]
	b = 0
	link = 'https://vk.com/sticker/1'
	for i in parse:
		print(f'{link}-{i}-128')
		p = requests.get(f'{link}-{i}-128')
		out = open(f'путь где будет сохранятся стики/{b}.png', "wb")
		out.write(p.content)
		out.close()
		b += 1
