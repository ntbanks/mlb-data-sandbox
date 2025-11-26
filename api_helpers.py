import requests
import humps
import json
import os
import pandas as pd
from datetime import datetime 

current_season = datetime.today().year
base_url = "http://statsapi.mlb.com/api/v1"


def process_endpoint_url(endpoint_url, pop_key=None):
    """
    Fetches data from a URL, parses JSON, and optionally pops a key.

    Args:
    endpoint_url: The URL to fetch data from.
    pop_key: The key to pop from the JSON data (optional, defaults to None).

    Returns:
    A pandas DataFrame containing the processed data
    """
    json_result = requests.get(endpoint_url).content

    data = json.loads(json_result)

    # if pop_key is provided, pop key and normalize nested fields
    if pop_key:
        df_result = pd.json_normalize(data.pop(pop_key), sep = '_')
    # if pop_key is not provided, normalize entire json
    else:
        df_result = pd.json_normalize(data)

    return df_result


def call_api(endpoint, params=None):
    """ 
    wrapper for calls to the API. mostly just handles errors. 
    
    endpoint is just the string to add after the base url
        ex: /schedule/games/
    params is a dict of path parameters
        ex: {'season':2025}

    returns a dict
    """
    full_url = base_url + endpoint
    
    try:
        response = requests.get(full_url, params)
    except requests.exceptions.RequestException as e:
        print(f"error making http request: {str(e)}")
        return None

    try:
        data = response.json()
    except (ValueError, requests.JSONDecodeError) as e:
        print(f'Bad JSON in response: {str(e)}')
        return None

    if response.status_code <= 200 and response.status_code <= 299:
        # print(f"success calling: {full_url}")
        if 'copyright' in data:
            del data['copyright']
        return humps.decamelize(data)
    
    elif response.status_code >= 400 and response.status_code <= 499:  
        print(f"server error: {response.reason} {full_url}")
        return None
    
    elif response.status_code >= 500 and response.status_code <= 599:
        print(f"internal error: {response.reason}")
        return None

    else:
        print(f"error: {response.reason}")

    
def get_seasons():
    seasons_resp = call_api('/seasons/all', {'sportId':1})
    if seasons_resp:
        _s = seasons_resp.get('seasons')
        seasons = {s['season_id']:s for s in _s}
    else:
        seasons = {}
    return seasons


def get_teams(season):
    file_path = f'data/teams/{season}.json'
    try:
        with open(file_path) as f:
            teams = json.load(f)
    except FileNotFoundError:
        teams_resp = call_api('/teams', {'sportId': 1, 'season': season})
        if teams_resp:
            teams = teams_resp['teams']
            with open(file_path, 'x') as f:
                f.write(json.dumps(teams))
        else:
            return {}
    finally:
        return teams
        


def _get_season_games(season):
    file_path = f'data/games/{season}.json'
    try:
        with open(file_path) as f:
            games = json.load(f)
    except FileNotFoundError:
        games_resp = call_api('/schedule/games', {'sportId': 1, 'season': season})
        if games_resp:
            games = []
            for d in games_resp['dates']:
                games.extend(d['games'])
        with open(file_path, 'x') as f:
            f.write(json.dumps(games))
    finally:
        return games


def get_games(start='2015'):
    fp = f'data/games/{current_season}.json'
    if os.path.exists(fp):
        print('deleting current season games to retrieve the last few days')
        os.remove(fp)
    games = []
    for i in range(int(start),current_season+1):
        # _get_teams()
        games.extend(_get_season_games(i))
    return games

def get_pbp(g_id):
    end_point = f'/game/{g_id}/playByPlay'
    fp = f'data/pbp/{g_id}.json'
    if os.path.exists(fp):
        # print(f'pbp data for {g_id} already saved')
        with open(fp) as f:
            return json.load(f)
    else:
        pbp_resp = call_api(end_point)
        if pbp_resp:
            print(f'writing {g_id} pbp data to file')
            with open(fp, 'x') as f:
                f.write(json.dumps(pbp_resp))
            return pbp_resp
        else:
            print(f'error getting pbp data for {g_id}')
            return {}                
    
