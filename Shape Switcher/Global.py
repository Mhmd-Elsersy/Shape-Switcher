def indexDec(index):
	x, y = index.split(',')
	return [float(x), float(y)]

def indexEnc(index):
	x = "".join(str(index))
	return x[1:len(x)-1]

d2 = {
	"1, 1": "balata color blue",
	"1, 2": "balata",
	"1, 3": "wall",
	"1, 4": "balata",
	"1, 6": "balata",
	"1, 7": "balata shape rect",

	"2, 1": "balata",
	"2, 2": "balata",
	"2, 3": "wall",
	"2, 4": "balata",
	"2, 5": "wall",
	"2, 6": "balata",
	"2, 7": "balata",

	"3, 1": "balata",
	"3, 2": "balata",
	"3, 4": "balata",
	"3, 5": "wall",
	"3, 6": "wall",

	"4, 2": "wall",
	"4, 3": "wall",
	"4, 4": "balata",
	"4, 5": "balata",
	"4, 6": "balata",
	"4, 7": "balata",

	"5, 1": "balata",
	"5, 2": "balata",
	"5, 3": "balata",
	"5, 4": "balata",
	"5, 5": "wall",
	"5, 7": "wall",

	"6, 1": "wall",
	"6, 3": "wall",
	"6, 4": "balata",
	"6, 6": "balata",
	"6, 7": "balata color green",

	"7, 1": "balata",
	"7, 2": "balata",
	"7, 3": "wall",
	"7, 4": "balata",
	"7, 5": "wall",
	"7, 6": "wall",
	"7, 7": "wall",

	"8, 1": "balata",
	"8, 2": "balata",
	"8, 4": "balata",
	"8, 6": "balata",
	"8, 7": "balata",

	"9, 1": "balata shape tri",
	"9, 2": "balata",
	"9, 3": "wall",
	"9, 4": "balata",
	"9, 5": "wall",
	"9, 6": "balata",
	"9, 7": "balata shape star"
}

d = {}

def setLevel(dic):
	d.update(dic)