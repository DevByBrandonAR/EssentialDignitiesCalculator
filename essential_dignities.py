
import plot 
import config 

planets = config.planets

ruled_by = { 
	"Saturn" : ["Capricorn", "Aquarius"],
	"Jupiter": ["Sagittarius", "Pisces"], 
	"Mars": ["Aries","Scorpio"], 
	"Sun": ["Leo"], 
	"Venus": ["Taurus","Libra"], 
	"Mercury" : ["Gemini","Virgo"], 
	"Moon" : ["Cancer"]
} 

exalted_in = { 
	"Saturn" : "Libra" ,
	"Jupiter": "Cancer", 
	"Mars": "Capricorn", 
	"Sun": "Aries", 
	"Venus": "Pisces", 
	"Mercury" : "Virgo", 
	"Moon" : "Taurus" 
} 

opposites = { 
"Aries" : "Libra", 
"Taurus" : "Scorpio", 
"Gemini" : "Sagittarius", 
"Cancer" : "Capricorn", 
"Leo":"Aquarius", 
"Virgo": "Pisces", 
"Libra": "Aries", 
"Scorpio": "Taurus", 
"Sagittarius": "Gemini", 
"Capricorn":"Cancer", 
"Aquarius":"Leo", 
"Pisces":"Virgo"
} 

triplicities= {
	( "Aries" ,"Leo", "Sagittarius" ): ["Sun", "Jupiter", "Saturn"], 
	("Taurus","Virgo", "Capricorn" ) : ["Venus","Moon", "Mars"], 
	("Gemini" , "Libra","Aquarius"): ["Saturn", "Mercury", "Jupiter"], 
	("Cancer", "Scorpio","Pisces"): ["Venus", "Mars","Moon"  ]
}

decans = {
"Aries" : ["Mars", "Sun","Venus" ], 
"Taurus" : ["Mercury", "Moon", "Saturn"],  
"Gemini" : ["Jupiter","Mars","Sun"], 
"Cancer" : ["Venus", "Mercury", "Moon"], 
"Leo": ["Saturn","Jupiter", "Mars"], 
"Virgo": ["Sun", "Venus","Mercury"], 
"Libra": ["Moon" ,"Saturn", "Jupiter" ], 
"Scorpio": ["Mars","Sun",  "Venus"],  
"Sagittarius": ["Mercury", "Moon", "Saturn"], 
"Capricorn":["Jupiter", "Mars", "Sun"], 
"Aquarius":["Venus","Mercury",  "Moon"], 
"Pisces":["Saturn", "Jupiter","Mars"]
}
terms = {
	"Aries": {(0,6):"Jupiter", (6,12):"Venus", (12,20): "Mercury", (20,25):"Mars", (25,30):"Saturn"}, 
	"Taurus":  {(0,8): "Venus", (8,14): "Mercury", (14,22): "Jupiter", (22,27):"Saturn", (27,30):"Mars"}, 
	"Gemini":  {(0,6):"Mercury", (6,12):"Jupiter", (12,17):"Venus", (17,24):"Mars", (24,30):"Saturn"}, 
	"Cancer":  {(0,7):"Mars", (7,13):"Venus", (13,19):"Mercury", (19,26):"Jupiter", (26,30):"Saturn"}, 
	"Leo":  {(0,6):"Jupiter", (6,11):"Venus", (11,18):"Saturn", (18,24):"Mercury", (24,30):"Mars"}, 
	"Virgo":  {(0,7): "Mercury", (7,17):"Venus", (17,21):"Jupiter", (21,28):"Mars", (28,30):"Saturn"}, 
	"Libra":  {(0,6):"Venus", (6,14):"Mercury", (14,21):"Jupiter", (21,28):"Mars", (28,30):"Saturn"}, 
	"Scorpio":  {(0,7):"Mars", (7,11):"Venus", (11,19):"Mercury", (19,24):"Jupiter", (24,30):"Saturn"}, 
	"Sagittarius": {(0,12):"Jupiter", (12,17):"Venus", (17,21):"Mercury", (21,26):"Saturn", (26,30):"Mars"}, 
	"Capricorn":  {(0,7):"Mercury", (7,14):"Jupiter", (14,22):"Venus", (22,26):"Saturn", (26,30):"Mars"}, 
	"Aquarius":  {(0,7):"Mercury", (7,13):"Venus", (13,20):"Jupiter", (20,25):"Mars", (25,30):"Saturn"}, 
	"Pisces":   {(0,12):"Venus", (12,16):"Jupiter", (16,19):"Mercury", (19,28):"Mars", (28,30):"Saturn"}
}	



scores = {planet : 0 for planet in planets.keys()}

for planet in scores.keys(): 
	print(planet)
	# Rulers 
	for sign in ruled_by[planet]:  
		if sign == planets[planet]["Sign"]: 
			scores[planet] += 5 
			print("--> +5 Ruler")
		elif planets[planet]["Sign"] == opposites[sign]:
			scores[planet] -= 5
			print("--> -5 Detriment")
	if exalted_in[planet] == planets[planet]["Sign"]: 
		scores[planet] += 4 
		print("--> +4 Exalted") 
	elif   planets[planet]["Sign"] ==  opposites[exalted_in[planet]]:
		scores[planet] -= 4
		print("--> -4 Fall") 
	for triplicity in triplicities.keys(): 
			if planets[planet]["Sign"] in triplicity: 	
				if planet in triplicities[triplicity]: 
					scores[planet] += 3 
					print("--> +3 Triplicity") 
	for i in range(len(decans[planets[planet]["Sign"]])):
		a = i*10 
		b = a + 9 
		if planets[planet]["Degree"] >= a and planets[planet]["Degree"] <= b and planet == decans[planets[planet]["Sign"]][i]: 
			scores[planet] += 1 
			print("--> +1 Decan") 
	for angle_range in terms[planets[planet]["Sign"]].keys(): 
		a = angle_range[0] 
		b = angle_range[1] 
		if planets[planet]["Degree"] >= a and planets[planet]["Degree"] <= b: 
			if planet == terms[planets[planet]["Sign"]][angle_range]: 
				scores[planet] += 2 
				print("--> +2 Term") 
	if scores[planet] == 0: 
		scores[planet] -= 5 
		print(" --> -5 Peregrination") 
print("---------------------")
print("Totals")
print("---------------------")
for key in scores.keys(): 
	print(key, scores[key]) 
plot.plot(scores) 
	