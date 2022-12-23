# To to touch grass or not to touch grass By Soup Noodles

# Roster:
1. Ivan Yeung (PM)
2. Vivian Graeber (Devo)
3. Jeff Chen (Devo)
4. Brian Chen (Devo)

# Site Description:  
This site will determine whether it would be optimal for the user to go outside based on their preferences and events that are going on. We will be drawing from the factors like weather, games, shows to determine the result. There will also be a scale for the each topic that the user can show their level of interest for. This site weighs and combines these factors and output the suggestion to the user.

# How Our Algorithm Works:
* To determine the weight of the weather, we use 75 degrees (F), 60 % humidity, and 0 % chance of rain as the 'standard', 100%
    * To calculate the weight of the temperature, we use 2 separate distributions.
        * If the temperature is 75 or below, we divide the temperature by 75.
        * If the temperature is at or above 75, we take the difference of the temperature and 75 and get the inverse.
    * Humidity is the same:
        * Less than or equal 60: humidity / 60
        * More than 60: (humidity - 60) / 100
    * Rain chance is 1 - (rain chance / 100), since rain chance is expressed as a percentage

* To determine the weight of NBA games, we find the difference between the current time and the next NBA game
    * If the difference is under 30 min and at or above 0 (game is starting in less than 30 min), we subtract (difference / 30) from 1 to get the weight
    * If the difference is between -60 and 0, the weight is set to 0 (game has been going on for less than an hour)
    * If neither of these conditions are filled, the weight is set to 1

* To determine the weight of the user's favorite anime, we check 2 things: if the anime is finished airing, and if the anime will air a new episode within 30 minutes
    * Uses a the same algorithm as NBA, except it checks if the anime is finished airing. If it is, the weight is automatically set to 0.

* The weights of the three APIs are averaged, then used in a picker, which picks between going outside or not, with the calculated weight used for the weight of going outside.


# APIs used:
* [Weather API](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_weatherAPI.md)
* [NBA Schedule API](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_NBA_Schedule.md)
* [My Anime List API](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_MyAnimeList.md)

# Launch Codes:

1. Clone this repo:
```sh
git@github.com:IvanYeung0610/P01.git
```

2. Cd into the directory:
```sh
cd P01/
```

3. Install all dependencies:
```sh
pip install -r requirements.txt
```

4. Cd into the app folder of the directory
```sh
cd app/
```

5. Run the init python file:
```sh
python3 __init__.py
```

6. Copy the link(http://127.0.0.1:5000) from terminal onto a web browser. Or Ctrl + click the link(http://127.0.0.1:5000).
```sh
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 924-082-676

```
