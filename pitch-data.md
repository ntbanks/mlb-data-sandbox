# Strike Zone and Pitch Location
This gets messy but will be essential to look into plate dicipline and chase rate, etc. Took me forever to figure out so I figured I'd write it down before I forget.

The API gives the horizontal and vertical position (in ft) of the pitch as it crosses home plate. Y represents the distance from the catcher out toward the pitcher, X is left and right from the middle of home plate, and Z is distance from the ground. Think of the field as an X/Y grid with home plate being 0,0... so a pitch down the middle is at 0,0,2.5

Horizontal:  
Strike zone width is 20" (17" for the plate and 3" for the ball). The middle of the plate is 0 so converted to feet the zone is -0.83' through 0.83'

Vertical:  
Since height varies by player (and by pitch when their stance changes...) it's included in the pitch data as `strike_zone_top` and `strike_zone_bottom`. 1.5' to 3.5' is pretty much the avg and i THINK most pictures online use that instead of the per batter numbers.

## Zones...
MLB splits this into 13 "zones", which they include in the pitch data. 1-9 split the zone by 9 and 11-14 are an added 33% to catch balls that land in the grey area and sometimes can be called strikes. They read like a book from the catcher's POV so high and inside to a righty is zone 1 (-x values). Most hot/cold zone type of stats for pitchers and batters use these.

<img src="img/strike-zones.png" alt="alt text" width="350"/><img src="img/strike-zones-ex.png" alt="alt text" width="350"/>

### chase zones...
I don't think these are official stats but this is how most deep dives on chase rates are done AFAIK. The idea is to look at distance from the center of the zone instead of inside/outside, low/high. The dashed green line is the strike zone (the line between the 1-9 boxes and the 11-14 boxes in the other model). 

<img src="img/chase-zones-ex.png"/>

The "heart" is a meatball down the middle and the "shadow" is the area the pitcher really wants to attack. Opens the door for some cool analysis though! Function to convert from pitch location to zone will be somewhere in the code. 