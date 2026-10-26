# EssentialDignitiesCalculator

> ⚠️ **Development Status: Beta**  
> This project is currently in active beta. The core structures are stable, but specific calculation logic and available features are in flux. Basically you can enter latitude and longitude, birth time and date, and timezone, and get a chart. This leverages several libraries to get this astronomical information into a usable arrangement.

## What does this tool do
> There is the concept in medieval astrology of "essential dignity" whereby you can rank the strength of different planets in a chart. This is done by looking at the sign and angle placements and seeing how they compare to standards. There are various schemes in the literature; here we use a scheme listed in Chapter 6 of _On the Heavenly Spheres: A Treatise on Traditional Astrology_ by Avelar and Ribeiro (2010). The logic in this program institutes an algorithm whereby one can rank these planets. It prints out the rankings of the seven "classical planets" (Moon, Mercury, Venus, Sun, Mars, Jupiter, Saturn) and displays a spider chart of the rankings. (See below for example input and output.)

## Logic 
1. +5 Points Rulership
2. +4 Points Exaltation
3. -5 Points Detriment
4. -4 Points Fall
5.  +3 Points Triplicity
6.  +2 Points Term
7. +1 Points Decan
8. -5 Points Peregrination 


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

## Sample Partial Terminal Session 
```
#Text here
```

## Known Issues
```
#text here
```


