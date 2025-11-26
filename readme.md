# MLB Data Exploration

The MLB Stats API returns a wealth of granular information down to spin rate//location/inches of break of pitches and exit velocity and angle of hits. My goal in this project is to help make sense of these API responses and enable friends and fellow fans to explore the data and answer deeper questions:
- Are intentional walks really a good idea? 
- Can we look at pitch count per at bat to see how big of an impact comes from being able to read a ball vs. strke?
- How important really is righty vs lefty in pitcher/batter matchups? 
- Do pitchers get less accurate or powerful as pitch count increases, and if so where is the fall off or is it gradual? 
- How often is someone swinging at an 0-2 breaking ball in the dirt after two fastballs down the middle? 
- How often are batters swinging at unhittable pitches on a 3-0 count? 

There are API wrappers that return a lot of this data but that's boring and I prefer to work directly with the API. The API also does lots of aggregations and stuff but again that's boring so this will work with raw data for now.

This API is free and you don't need a token or account to access it, but it's like 25 requests/second or something before it flags you. If this becomes and issue and since historical data doesn't change, i'll eventually include code to save raw data locally to reduce calls.

## Data Availability

- 1901-1968: Boxscore only
- 1969-1988: Play-by-play
- 1989-2007: Pitch-by-pitch
- 2008-2014: Pitch-by-pitch + pitch speed/break
- 2015-present: Pitch-by-pitch + pitch speed/break + exit velo/hr distance

Since I'm just playing around mostly with pitch and exit velo data, everything in this repo will deal with only 2015-present. We don't want steroid era to skew metrics anyway lol