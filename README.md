# EssentialDignitiesCalculator

> ⚠️ **Development Status: Beta**  
> This project is currently in active beta. The core structures are stable, but specific calculation logic and available features are in flux. Basically you can enter latitude and longitude, birth time and date, and timezone, and get a chart. This leverages several libraries to get this astronomical information into a usable arrangement.

## What does this tool do
> There is the concept in medieval astrology of "essential dignity" whereby you can rank the strength of different planets in a chart. This is done by looking at the sign and angle placements and seeing how they compare to standards. There are various schemes in the literature; here we use a scheme listed in Chapter 6 of _On the Heavenly Spheres: A Treatise on Traditional Astrology_ by Avelar and Ribeiro (2010). The logic in this program institutes an algorithm whereby one can rank these planets. It prints out the rankings of the seven "classical planets" (Moon, Mercury, Venus, Sun, Mars, Jupiter, Saturn) and displays a spider chart of the rankings. (See below for example input and output.)

## Logic 
1. **+5 Points Rulership**
The sign that the planet occupies... is this a sign that the planet "rules" in the classical scheme? If so we score five points. 
```
	"Saturn" : ["Capricorn", "Aquarius"],
	"Jupiter": ["Sagittarius", "Pisces"], 
	"Mars": ["Aries","Scorpio"], 
	"Sun": ["Leo"], 
	"Venus": ["Taurus","Libra"], 
	"Mercury" : ["Gemini","Virgo"], 
	"Moon" : ["Cancer"]
  ```
2. **+4 Points Exaltation**
We next look at whether the sign is one in which the planet is "exalted" in the classical scheme... not the sign it rules but one in which nevertheless it is considered especially potent. If so, we score four. 
```
	"Saturn" : "Libra" ,
	"Jupiter": "Cancer", 
	"Mars": "Capricorn", 
	"Sun": "Aries", 
	"Venus": "Pisces", 
	"Mercury" : "Virgo", 
	"Moon" : "Taurus" 
```
3. **-5 Points Detriment**
If the planet is not in a sign it rules, but rather is on the opposite end of the ring of zodiac signs, it is in detriment and loses five points. This sequence lists opposing pairs and is used in steps (3) and (4) of this algorithm: 
```
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
```
4. **-4 Points Fall**
If the planet is not in a sign in which it is exalted, but rather is on the opposite end of the ring of zodiac signs, it is in its "fall" and loses four. 
5.  **+3 Points Triplicity**
We look at the diurnal, nocturnal, and participatory rulers in the classical Dorothean scheme; if the given planet is one of these three rulers for the sign, we score three points. 
```
	( "Aries" ,"Leo", "Sagittarius" ): ["Sun", "Jupiter", "Saturn"], 
	("Taurus","Virgo", "Capricorn" ) : ["Venus","Moon", "Mars"], 
	("Gemini" , "Libra","Aquarius"): ["Saturn", "Mercury", "Jupiter"], 
	("Cancer", "Scorpio","Pisces"): ["Venus", "Mars","Moon"  ]
```
6.  **+2 Points Term**
We look at the classical rulers of each range of angles within a sign; if the planet matches the planetary ruler of that "term" or bound, we score two points. 
```
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
```
7. **+1 Points Decan**
We look at the classical chaldean planetary rulers of decans (10 degree increments, three to each sign). If the planet matches its decan ruler, we score a point:
```
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
```
9. **-5 Points Peregrination**
If after the previous steps the planet has scored zero, we deduct 5 points. Note that in the spider chart, a negative score is plotted as zero.  


## Example input 
```
#See sample file config.py for configuration.
$ python3 essential_dignities.py
```

## Example results 
<img width="2432" height="1256" alt="image" src="https://github.com/user-attachments/assets/7d277ef4-85c5-4eee-ac0c-61a9eca635b0" />


## Installation
```bash
git clone https://github.com/DevByBrandonAR/EssentialDignitiesCalculator.git
cd EssentialDignitiesCalculator
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
python3 -m pip install .
```




