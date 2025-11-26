## Lookup Values

Like most APIs there's lots of lookup values they reference by a code with very little extra info. Most can be found at at this end point: `/lookup/values/all`

I documented alot of the frequently used ones here.

### Hit Trajectories

<table border="1" class="dataframe" height="300px">
  <thead>
    <tr style="text-align: right;">
      <th>code</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bunt_grounder</td>
      <td>Bunt - Ground Ball</td>
    </tr>
    <tr>
      <td>bunt_popup</td>
      <td>Bunt - Popup</td>
    </tr>
    <tr>
      <td>bunt_line_drive</td>
      <td>Bunt - Line Drive</td>
    </tr>
    <tr>
      <td>line_drive</td>
      <td>Line Drive</td>
    </tr>
    <tr>
      <td>ground_ball</td>
      <td>Ground Ball</td>
    </tr>
    <tr>
      <td>fly_ball</td>
      <td>Fly Ball</td>
    </tr>
    <tr>
      <td>popup</td>
      <td>Popup</td>
    </tr>
  </tbody>
</table>

### Event Types

<table height=300px border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>code</th>
      <th>plate_appearance</th>
      <th>hit</th>
      <th>base_running_event</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>pickoff_1b</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Pickoff 1B</td>
    </tr>
    <tr>
      <th>pickoff_2b</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Pickoff 2B</td>
    </tr>
    <tr>
      <th>pickoff_3b</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Pickoff 3B</td>
    </tr>
    <tr>
      <th>pitcher_step_off</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Pitcher Step Off</td>
    </tr>
    <tr>
      <th>pickoff_error_1b</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Pickoff Error 1B</td>
    </tr>
    <tr>
      <th>pickoff_error_2b</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Pickoff Error 2B</td>
    </tr>
    <tr>
      <th>pickoff_error_3b</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Pickoff Error 3B</td>
    </tr>
    <tr>
      <th>batter_timeout</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Batter Timeout</td>
    </tr>
    <tr>
      <th>mound_visit</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Mound Visit</td>
    </tr>
    <tr>
      <th>no_pitch</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>No Pitch</td>
    </tr>
    <tr>
      <th>single</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>Single</td>
    </tr>
    <tr>
      <th>double</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>Double</td>
    </tr>
    <tr>
      <th>triple</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>Triple</td>
    </tr>
    <tr>
      <th>home_run</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>Home Run</td>
    </tr>
    <tr>
      <th>double_play</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Double Play</td>
    </tr>
    <tr>
      <th>field_error</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Field Error</td>
    </tr>
    <tr>
      <th>error</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Error</td>
    </tr>
    <tr>
      <th>field_out</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Field Out</td>
    </tr>
    <tr>
      <th>fielders_choice</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Fielders Choice</td>
    </tr>
    <tr>
      <th>fielders_choice_out</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Fielders Choice Out</td>
    </tr>
    <tr>
      <th>force_out</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Forceout</td>
    </tr>
    <tr>
      <th>grounded_into_double_play</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Grounded Into DP</td>
    </tr>
    <tr>
      <th>grounded_into_triple_play</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Grounded Into TP</td>
    </tr>
    <tr>
      <th>strikeout</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Strikeout</td>
    </tr>
    <tr>
      <th>strike_out</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Strike Out</td>
    </tr>
    <tr>
      <th>strikeout_double_play</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Strikeout Double Play</td>
    </tr>
    <tr>
      <th>strikeout_triple_play</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Strikeout Triple Play</td>
    </tr>
    <tr>
      <th>triple_play</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Triple Play</td>
    </tr>
    <tr>
      <th>sac_fly</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Sac Fly</td>
    </tr>
    <tr>
      <th>catcher_interf</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Catcher Interference</td>
    </tr>
    <tr>
      <th>batter_interference</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Batter Interference</td>
    </tr>
    <tr>
      <th>fielder_interference</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Fielder Interference</td>
    </tr>
    <tr>
      <th>runner_interference</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Runner Interference</td>
    </tr>
    <tr>
      <th>fan_interference</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Fan Interference</td>
    </tr>
    <tr>
      <th>batter_turn</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Batter Turn</td>
    </tr>
    <tr>
      <th>ejection</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Ejection</td>
    </tr>
    <tr>
      <th>cs_double_play</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Cs Double Play</td>
    </tr>
    <tr>
      <th>defensive_indiff</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Defensive Indiff</td>
    </tr>
    <tr>
      <th>sac_fly_double_play</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Sac Fly Double Play</td>
    </tr>
    <tr>
      <th>sac_bunt</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Sac Bunt</td>
    </tr>
    <tr>
      <th>sac_bunt_double_play</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Sac Bunt Double Play</td>
    </tr>
    <tr>
      <th>walk</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Walk</td>
    </tr>
    <tr>
      <th>intent_walk</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Intent Walk</td>
    </tr>
    <tr>
      <th>hit_by_pitch</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Hit By Pitch</td>
    </tr>
    <tr>
      <th>injury</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Injury</td>
    </tr>
    <tr>
      <th>os_ruling_pending_prior</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Official Scorer Ruling Pending</td>
    </tr>
    <tr>
      <th>os_ruling_pending_primary</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>Official Scorer Ruling Pending</td>
    </tr>
    <tr>
      <th>at_bat_start</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>At Bat Start</td>
    </tr>
    <tr>
      <th>passed_ball</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Passed Ball</td>
    </tr>
    <tr>
      <th>other_advance</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Other Advance</td>
    </tr>
    <tr>
      <th>runner_double_play</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Runner Double Play</td>
    </tr>
    <tr>
      <th>runner_placed</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Runner Placed On Base</td>
    </tr>
    <tr>
      <th>pitching_substitution</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Pitching Substitution</td>
    </tr>
    <tr>
      <th>offensive_substitution</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Offensive Substitution</td>
    </tr>
    <tr>
      <th>defensive_switch</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Defensive Switch</td>
    </tr>
    <tr>
      <th>umpire_substitution</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Umpire Substitution</td>
    </tr>
    <tr>
      <th>pitcher_switch</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Pitcher Switch</td>
    </tr>
    <tr>
      <th>game_advisory</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Game Advisory</td>
    </tr>
    <tr>
      <th>stolen_base</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Stolen Base</td>
    </tr>
    <tr>
      <th>stolen_base_2b</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Stolen Base 2B</td>
    </tr>
    <tr>
      <th>stolen_base_3b</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Stolen Base 3B</td>
    </tr>
    <tr>
      <th>stolen_base_home</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Stolen Base Home</td>
    </tr>
    <tr>
      <th>caught_stealing</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Caught Stealing</td>
    </tr>
    <tr>
      <th>caught_stealing_2b</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Caught Stealing 2B</td>
    </tr>
    <tr>
      <th>caught_stealing_3b</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Caught Stealing 3B</td>
    </tr>
    <tr>
      <th>caught_stealing_home</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Caught Stealing Home</td>
    </tr>
    <tr>
      <th>defensive_substitution</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>Defensive Sub</td>
    </tr>
    <tr>
      <th>pickoff_caught_stealing_2b</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Pickoff Caught Stealing 2B</td>
    </tr>
    <tr>
      <th>pickoff_caught_stealing_3b</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Pickoff Caught Stealing 3B</td>
    </tr>
    <tr>
      <th>pickoff_caught_stealing_home</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Pickoff Caught Stealing Home</td>
    </tr>
    <tr>
      <th>balk</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Balk</td>
    </tr>
    <tr>
      <th>forced_balk</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Disengagement Violation</td>
    </tr>
    <tr>
      <th>wild_pitch</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Wild Pitch</td>
    </tr>
    <tr>
      <th>other_out</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>Runner Out</td>
    </tr>
  </tbody>
</table>

### Player Status Codes

<table height=300px border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>code</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A</td>
      <td>Active</td>
    </tr>
    <tr>
      <td>D7</td>
      <td>7-day IL</td>
    </tr>
    <tr>
      <td>D10</td>
      <td>10-day IL</td>
    </tr>
    <tr>
      <td>D15</td>
      <td>15-day IL</td>
    </tr>
    <tr>
      <td>D60</td>
      <td>60-day IL</td>
    </tr>
    <tr>
      <td>D0</td>
      <td>IL</td>
    </tr>
    <tr>
      <td>ILF</td>
      <td>Full Season IL</td>
    </tr>
    <tr>
      <td>RM</td>
      <td>Reassigned</td>
    </tr>
    <tr>
      <td>RA</td>
      <td>Rehab</td>
    </tr>
    <tr>
      <td>DEV</td>
      <td>Development List</td>
    </tr>
    <tr>
      <td>ASG</td>
      <td>Assigned</td>
    </tr>
    <tr>
      <td>SU</td>
      <td>Suspended</td>
    </tr>
    <tr>
      <td>RES</td>
      <td>Reserve</td>
    </tr>
    <tr>
      <td>BRV</td>
      <td>Bereavement</td>
    </tr>
    <tr>
      <td>ADM</td>
      <td>Administrative Leave</td>
    </tr>
    <tr>
      <td>RST</td>
      <td>Restricted</td>
    </tr>
    <tr>
      <td>MIL</td>
      <td>Military Leave</td>
    </tr>
    <tr>
      <td>40M</td>
      <td>Forty Man</td>
    </tr>
    <tr>
      <td>IN</td>
      <td>Ineligible List</td>
    </tr>
    <tr>
      <td>TI</td>
      <td>Temporary Inactive</td>
    </tr>
    <tr>
      <td>RET</td>
      <td>Retired</td>
    </tr>
    <tr>
      <td>FME</td>
      <td>Family Medical</td>
    </tr>
    <tr>
      <td>PL</td>
      <td>Paternity</td>
    </tr>
    <tr>
      <td>MIN</td>
      <td>Minor League Contract</td>
    </tr>
    <tr>
      <td>NRI</td>
      <td>NRI</td>
    </tr>
    <tr>
      <td>WA</td>
      <td>Waived</td>
    </tr>
    <tr>
      <td>TR</td>
      <td>Traded</td>
    </tr>
    <tr>
      <td>RL</td>
      <td>Released</td>
    </tr>
    <tr>
      <td>FA</td>
      <td>Free agent</td>
    </tr>
    <tr>
      <td>DEC</td>
      <td>Deceased</td>
    </tr>
    <tr>
      <td>CL</td>
      <td>Claimed</td>
    </tr>
    <tr>
      <td>DES</td>
      <td>DFA</td>
    </tr>
    <tr>
      <td>BN</td>
      <td>Banned</td>
    </tr>
    <tr>
      <td>TAX</td>
      <td>Taxi Squad</td>
    </tr>
    <tr>
      <td>NYR</td>
      <td>Not Yet Reported</td>
    </tr>
    <tr>
      <td>D45</td>
      <td>45-day IL</td>
    </tr>
  </tbody>
</table>

### Schedule Types

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>id</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>games</td>
      <td>game schedule</td>
    </tr>
    <tr>
      <td>xref</td>
      <td>xref games</td>
    </tr>
    <tr>
      <td>events</td>
      <td>all events schedule</td>
    </tr>
  </tbody>
</table>

### Game Statuses

<table height="300px" border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>abstract_game_state</th>
      <th>coded_game_state</th>
      <th>detailed_state</th>
      <th>status_code</th>
      <th>abstract_game_code</th>
      <th>reason</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Preview</td>
      <td>S</td>
      <td>Scheduled</td>
      <td>S</td>
      <td>P</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Pre-Game</td>
      <td>P</td>
      <td>P</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>P</td>
      <td>Warmup</td>
      <td>PW</td>
      <td>L</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: Rain</td>
      <td>PR</td>
      <td>P</td>
      <td>Rain</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: Snow</td>
      <td>PS</td>
      <td>P</td>
      <td>Snow</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: Wet Grounds</td>
      <td>PG</td>
      <td>P</td>
      <td>Wet Grounds</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: Venue</td>
      <td>PV</td>
      <td>P</td>
      <td>Venue</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: Fog</td>
      <td>PF</td>
      <td>P</td>
      <td>Fog</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: Cold</td>
      <td>PC</td>
      <td>P</td>
      <td>Cold</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: Air Quality</td>
      <td>PD</td>
      <td>P</td>
      <td>Air Quality</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: Wind</td>
      <td>PB</td>
      <td>P</td>
      <td>Wind</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: Inclement Weather</td>
      <td>PI</td>
      <td>P</td>
      <td>Inclement Weather</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: Power</td>
      <td>PP</td>
      <td>P</td>
      <td>Power</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: Ceremony</td>
      <td>PY</td>
      <td>P</td>
      <td>Ceremony</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: Lightning</td>
      <td>PL</td>
      <td>P</td>
      <td>Lightning</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: COVID-19</td>
      <td>PE</td>
      <td>P</td>
      <td>COVID-19</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start: Tragedy</td>
      <td>PA</td>
      <td>P</td>
      <td>Tragedy</td>
    </tr>
    <tr>
      <td>Preview</td>
      <td>P</td>
      <td>Delayed Start</td>
      <td>PO</td>
      <td>P</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>In Progress</td>
      <td>I</td>
      <td>L</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: Rain</td>
      <td>IR</td>
      <td>L</td>
      <td>Rain</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: Snow</td>
      <td>IS</td>
      <td>L</td>
      <td>Snow</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: Wet Grounds</td>
      <td>IG</td>
      <td>L</td>
      <td>Wet Grounds</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: Venue</td>
      <td>IV</td>
      <td>L</td>
      <td>Venue</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: Fog</td>
      <td>IF</td>
      <td>L</td>
      <td>Fog</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: Cold</td>
      <td>IC</td>
      <td>L</td>
      <td>Cold</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: Air Quality</td>
      <td>ID</td>
      <td>L</td>
      <td>Air Quality</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: Wind</td>
      <td>IB</td>
      <td>L</td>
      <td>Wind</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: Inclement Weather</td>
      <td>II</td>
      <td>L</td>
      <td>Inclement Weather</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: Power</td>
      <td>IP</td>
      <td>L</td>
      <td>Power</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: Ceremony</td>
      <td>IY</td>
      <td>L</td>
      <td>Ceremony</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: Lightning</td>
      <td>IL</td>
      <td>L</td>
      <td>Lightning</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: COVID-19</td>
      <td>IE</td>
      <td>L</td>
      <td>COVID-19</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: Tragedy</td>
      <td>IA</td>
      <td>L</td>
      <td>Tragedy</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Instant Replay</td>
      <td>IH</td>
      <td>L</td>
      <td>Review</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed</td>
      <td>IO</td>
      <td>L</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>I</td>
      <td>Delayed: About to Resume</td>
      <td>IZ</td>
      <td>L</td>
      <td>About to Resume</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Close play at 1st</td>
      <td>MF</td>
      <td>L</td>
      <td>Close play at 1st</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Tag play</td>
      <td>MA</td>
      <td>L</td>
      <td>Tag play</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Tag-up play</td>
      <td>MU</td>
      <td>L</td>
      <td>Tag-up play</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Timing play</td>
      <td>MM</td>
      <td>L</td>
      <td>Timing play</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Force play</td>
      <td>MC</td>
      <td>L</td>
      <td>Force play</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Home-plate collision</td>
      <td>MP</td>
      <td>L</td>
      <td>Home-plate collision</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Slide interference</td>
      <td>ME</td>
      <td>L</td>
      <td>Slide interference</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Home run</td>
      <td>MH</td>
      <td>L</td>
      <td>Home run</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Fair/foul in outfield</td>
      <td>MO</td>
      <td>L</td>
      <td>Fair/foul in outfield</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Catch/drop in outfield</td>
      <td>MD</td>
      <td>L</td>
      <td>Catch/drop in outfield</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Trap play in outfield</td>
      <td>MT</td>
      <td>L</td>
      <td>Trap play in outfield</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Hit by pitch</td>
      <td>MI</td>
      <td>L</td>
      <td>Hit by pitch</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Touching a base</td>
      <td>MB</td>
      <td>L</td>
      <td>Touching a base</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Passing runners</td>
      <td>MR</td>
      <td>L</td>
      <td>Passing runners</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Fan interference</td>
      <td>MN</td>
      <td>L</td>
      <td>Fan interference</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Stadium boundary call</td>
      <td>MS</td>
      <td>L</td>
      <td>Stadium boundary call</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Grounds rule</td>
      <td>MG</td>
      <td>L</td>
      <td>Grounds rule</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Rules check</td>
      <td>MQ</td>
      <td>L</td>
      <td>Rules check</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Record keeping</td>
      <td>MK</td>
      <td>L</td>
      <td>Record keeping</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Multiple issues</td>
      <td>ML</td>
      <td>L</td>
      <td>Multiple issues</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge</td>
      <td>MX</td>
      <td>L</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Manager challenge: Catchers Interference</td>
      <td>MV</td>
      <td>L</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>M</td>
      <td>Player challenge: Pitch Result</td>
      <td>MJ</td>
      <td>L</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Close play at 1st</td>
      <td>NF</td>
      <td>L</td>
      <td>Close play at 1st</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Tag play</td>
      <td>NA</td>
      <td>L</td>
      <td>Tag play</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Tag-up play</td>
      <td>NU</td>
      <td>L</td>
      <td>Tag-up play</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Def Shift Violation</td>
      <td>NW</td>
      <td>L</td>
      <td>Def Shift Violation</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Timing play</td>
      <td>NM</td>
      <td>L</td>
      <td>Timing play</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Force play</td>
      <td>NC</td>
      <td>L</td>
      <td>Force play</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Home-plate collision</td>
      <td>NP</td>
      <td>L</td>
      <td>Home-plate collision</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Slide interference</td>
      <td>NE</td>
      <td>L</td>
      <td>Slide interference</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Home run</td>
      <td>NH</td>
      <td>L</td>
      <td>Home run</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Fair/foul in outfield</td>
      <td>NO</td>
      <td>L</td>
      <td>Fair/foul in outfield</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Catch/drop in outfield</td>
      <td>ND</td>
      <td>L</td>
      <td>Catch/drop in outfield</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Trap play in outfield</td>
      <td>NT</td>
      <td>L</td>
      <td>Trap play in outfield</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Hit by pitch</td>
      <td>NI</td>
      <td>L</td>
      <td>Hit by pitch</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Touching a base</td>
      <td>NB</td>
      <td>L</td>
      <td>Touching a base</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Passing runners</td>
      <td>NR</td>
      <td>L</td>
      <td>Passing runners</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Fan interference</td>
      <td>NN</td>
      <td>L</td>
      <td>Fan interference</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Stadium boundary call</td>
      <td>NS</td>
      <td>L</td>
      <td>Stadium boundary call</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Grounds rule</td>
      <td>NG</td>
      <td>L</td>
      <td>Grounds rule</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Rules check</td>
      <td>NQ</td>
      <td>L</td>
      <td>Rules check</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Record keeping</td>
      <td>NK</td>
      <td>L</td>
      <td>Record keeping</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review: Multiple issues</td>
      <td>NL</td>
      <td>L</td>
      <td>Multiple issues</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire review</td>
      <td>NX</td>
      <td>L</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>N</td>
      <td>Umpire Challenge: Pitch Result</td>
      <td>NJ</td>
      <td>L</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed: Rain</td>
      <td>DR</td>
      <td>F</td>
      <td>Rain</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed: Snow</td>
      <td>DS</td>
      <td>F</td>
      <td>Snow</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed: Wet Grounds</td>
      <td>DG</td>
      <td>F</td>
      <td>Wet Grounds</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed: Venue</td>
      <td>DV</td>
      <td>F</td>
      <td>Venue</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed: Fog</td>
      <td>DF</td>
      <td>F</td>
      <td>Fog</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed: Cold</td>
      <td>DC</td>
      <td>F</td>
      <td>Cold</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed: Air Quality</td>
      <td>DD</td>
      <td>F</td>
      <td>Air Quality</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed: Wind</td>
      <td>DB</td>
      <td>F</td>
      <td>Wind</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed: Inclement Weather</td>
      <td>DI</td>
      <td>F</td>
      <td>Inclement Weather</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed: Power</td>
      <td>DP</td>
      <td>F</td>
      <td>Power</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed: Lightning</td>
      <td>DL</td>
      <td>F</td>
      <td>Lightning</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed: COVID-19</td>
      <td>DE</td>
      <td>F</td>
      <td>COVID-19</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed: Tragedy</td>
      <td>DA</td>
      <td>F</td>
      <td>Tragedy</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>D</td>
      <td>Postponed</td>
      <td>DO</td>
      <td>F</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled: Rain</td>
      <td>CR</td>
      <td>F</td>
      <td>Rain</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled: Snow</td>
      <td>CS</td>
      <td>F</td>
      <td>Snow</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled: Wet Grounds</td>
      <td>CG</td>
      <td>F</td>
      <td>Wet Grounds</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled: Venue</td>
      <td>CV</td>
      <td>F</td>
      <td>Venue</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled: Fog</td>
      <td>CF</td>
      <td>F</td>
      <td>Fog</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled: Cold</td>
      <td>CC</td>
      <td>F</td>
      <td>Cold</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled: Air Quality</td>
      <td>CD</td>
      <td>F</td>
      <td>Air Quality</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled: Wind</td>
      <td>CB</td>
      <td>F</td>
      <td>Wind</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled: Inclement Weather</td>
      <td>CI</td>
      <td>F</td>
      <td>Inclement Weather</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled: Power</td>
      <td>CP</td>
      <td>F</td>
      <td>Power</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled: Lightning</td>
      <td>CL</td>
      <td>F</td>
      <td>Lightning</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled: COVID-19</td>
      <td>CE</td>
      <td>F</td>
      <td>COVID-19</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled: Tragedy</td>
      <td>CA</td>
      <td>F</td>
      <td>Tragedy</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>C</td>
      <td>Cancelled</td>
      <td>CO</td>
      <td>F</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Game Over</td>
      <td>O</td>
      <td>F</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: Rain</td>
      <td>OR</td>
      <td>F</td>
      <td>Rain</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: Snow</td>
      <td>OS</td>
      <td>F</td>
      <td>Snow</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: Wet Grounds</td>
      <td>OG</td>
      <td>F</td>
      <td>Wet Grounds</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: Venue</td>
      <td>OV</td>
      <td>F</td>
      <td>Venue</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: Fog</td>
      <td>OF</td>
      <td>F</td>
      <td>Fog</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: Cold</td>
      <td>OC</td>
      <td>F</td>
      <td>Cold</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: Air Quality</td>
      <td>OD</td>
      <td>F</td>
      <td>Air Quality</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: Wind</td>
      <td>OB</td>
      <td>F</td>
      <td>Wind</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: Inclement Weather</td>
      <td>OI</td>
      <td>F</td>
      <td>Inclement Weather</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: Power</td>
      <td>OP</td>
      <td>F</td>
      <td>Power</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: Lightning</td>
      <td>OL</td>
      <td>F</td>
      <td>Lightning</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: COVID-19</td>
      <td>OE</td>
      <td>F</td>
      <td>COVID-19</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: Tragedy</td>
      <td>OA</td>
      <td>F</td>
      <td>Tragedy</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early: Mercy Rule</td>
      <td>OM</td>
      <td>F</td>
      <td>Mercy</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Completed Early</td>
      <td>OO</td>
      <td>F</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Game Over: Tied</td>
      <td>OT</td>
      <td>F</td>
      <td>Tied</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>O</td>
      <td>Game Over: Tie, decision by tiebreaker</td>
      <td>OW</td>
      <td>F</td>
      <td>Tied (won in tiebreaker)</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Final</td>
      <td>F</td>
      <td>F</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: Rain</td>
      <td>FR</td>
      <td>F</td>
      <td>Rain</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: Snow</td>
      <td>FS</td>
      <td>F</td>
      <td>Snow</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: Wet Grounds</td>
      <td>FG</td>
      <td>F</td>
      <td>Wet Grounds</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: Venue</td>
      <td>FV</td>
      <td>F</td>
      <td>Venue</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: Fog</td>
      <td>FF</td>
      <td>F</td>
      <td>Fog</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: Cold</td>
      <td>FC</td>
      <td>F</td>
      <td>Cold</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: Air Quality</td>
      <td>FD</td>
      <td>F</td>
      <td>Air Quality</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: Wind</td>
      <td>FB</td>
      <td>F</td>
      <td>Wind</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: Inclement Weather</td>
      <td>FI</td>
      <td>F</td>
      <td>Inclement Weather</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: Power</td>
      <td>FP</td>
      <td>F</td>
      <td>Power</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: Lightning</td>
      <td>FL</td>
      <td>F</td>
      <td>Lightning</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: COVID-19</td>
      <td>FE</td>
      <td>F</td>
      <td>COVID-19</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: Tragedy</td>
      <td>FA</td>
      <td>F</td>
      <td>Tragedy</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early: Mercy Rule</td>
      <td>FM</td>
      <td>F</td>
      <td>Mercy</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Completed Early</td>
      <td>FO</td>
      <td>F</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Final: Tied</td>
      <td>FT</td>
      <td>F</td>
      <td>Tied</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>F</td>
      <td>Final: Tie, decision by tiebreaker</td>
      <td>FW</td>
      <td>F</td>
      <td>Tied (won in tiebreaker)</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended</td>
      <td>T</td>
      <td>L</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: Rain</td>
      <td>TR</td>
      <td>L</td>
      <td>Rain</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: Snow</td>
      <td>TS</td>
      <td>L</td>
      <td>Snow</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: Wet Grounds</td>
      <td>TG</td>
      <td>L</td>
      <td>Wet Grounds</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: Venue</td>
      <td>TV</td>
      <td>L</td>
      <td>Venue</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: Fog</td>
      <td>TF</td>
      <td>L</td>
      <td>Fog</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: Cold</td>
      <td>TC</td>
      <td>L</td>
      <td>Cold</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: Air Quality</td>
      <td>TD</td>
      <td>L</td>
      <td>Air Quality</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: Wind</td>
      <td>TB</td>
      <td>L</td>
      <td>Wind</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: Inclement Weather</td>
      <td>TI</td>
      <td>L</td>
      <td>Inclement Weather</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: Power</td>
      <td>TP</td>
      <td>L</td>
      <td>Power</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: Lightning</td>
      <td>TL</td>
      <td>L</td>
      <td>Lightning</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: COVID-19</td>
      <td>TE</td>
      <td>L</td>
      <td>COVID-19</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: Tragedy</td>
      <td>TA</td>
      <td>L</td>
      <td>Tragedy</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended: Appeal Upheld</td>
      <td>TU</td>
      <td>L</td>
      <td>Appeal Upheld</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>T</td>
      <td>Suspended</td>
      <td>TO</td>
      <td>L</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended</td>
      <td>U</td>
      <td>L</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: Rain</td>
      <td>UR</td>
      <td>L</td>
      <td>Rain</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: Snow</td>
      <td>US</td>
      <td>L</td>
      <td>Snow</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: Wet Grounds</td>
      <td>UG</td>
      <td>L</td>
      <td>Wet Grounds</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: Venue</td>
      <td>UV</td>
      <td>L</td>
      <td>Venue</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: Fog</td>
      <td>UF</td>
      <td>L</td>
      <td>Fog</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: Cold</td>
      <td>UC</td>
      <td>L</td>
      <td>Cold</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: Air Quality</td>
      <td>UD</td>
      <td>L</td>
      <td>Air Quality</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: Wind</td>
      <td>UB</td>
      <td>L</td>
      <td>Wind</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: Inclement Weather</td>
      <td>UI</td>
      <td>L</td>
      <td>Inclement Weather</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: Power</td>
      <td>UP</td>
      <td>L</td>
      <td>Power</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: Lightning</td>
      <td>UL</td>
      <td>L</td>
      <td>Lightning</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: COVID-19</td>
      <td>UE</td>
      <td>L</td>
      <td>COVID-19</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: Tragedy</td>
      <td>UA</td>
      <td>L</td>
      <td>Tragedy</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: Appeal Upheld</td>
      <td>UU</td>
      <td>L</td>
      <td>Appeal Upheld</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended</td>
      <td>UO</td>
      <td>L</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Live</td>
      <td>U</td>
      <td>Suspended: About to Resume</td>
      <td>UZ</td>
      <td>L</td>
      <td>About to Resume</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>Q</td>
      <td>Forfeit: Game Over</td>
      <td>Q</td>
      <td>F</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>Q</td>
      <td>Forfeit: Delay of game</td>
      <td>QK</td>
      <td>F</td>
      <td>Delay</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>Q</td>
      <td>Forfeit: Failure to appear</td>
      <td>QX</td>
      <td>F</td>
      <td>Appear</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>Q</td>
      <td>Forfeit: Failure to field lineup</td>
      <td>QQ</td>
      <td>F</td>
      <td>Lineup</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>Q</td>
      <td>Forfeit: Ignoring ejection</td>
      <td>QJ</td>
      <td>F</td>
      <td>Ejection</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>Q</td>
      <td>Forfeit: Ineligible player</td>
      <td>QI</td>
      <td>F</td>
      <td>Ineligible</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>Q</td>
      <td>Forfeit: Refuses to play</td>
      <td>QN</td>
      <td>F</td>
      <td>Refusal</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>Q</td>
      <td>Forfeit: Unplayable field</td>
      <td>QV</td>
      <td>F</td>
      <td>Unplayable</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>Q</td>
      <td>Forfeit: Willful rule violation</td>
      <td>QR</td>
      <td>F</td>
      <td>Rule</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>Q</td>
      <td>Forfeit</td>
      <td>QO</td>
      <td>F</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>R</td>
      <td>Forfeit: Final</td>
      <td>R</td>
      <td>F</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>R</td>
      <td>Forfeit: Delay of game</td>
      <td>RK</td>
      <td>F</td>
      <td>Delay</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>R</td>
      <td>Forfeit: Failure to appear</td>
      <td>RX</td>
      <td>F</td>
      <td>Appear</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>R</td>
      <td>Forfeit: Failure to field lineup</td>
      <td>RQ</td>
      <td>F</td>
      <td>Lineup</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>R</td>
      <td>Forfeit: Ignoring ejection</td>
      <td>RJ</td>
      <td>F</td>
      <td>Ejection</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>R</td>
      <td>Forfeit: Ineligible player</td>
      <td>RI</td>
      <td>F</td>
      <td>Ineligible</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>R</td>
      <td>Forfeit: Refuses to play</td>
      <td>RN</td>
      <td>F</td>
      <td>Refusal</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>R</td>
      <td>Forfeit: Unplayable field</td>
      <td>RV</td>
      <td>F</td>
      <td>Unplayable</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>R</td>
      <td>Forfeit: Willful rule violation</td>
      <td>RR</td>
      <td>F</td>
      <td>Rule</td>
    </tr>
    <tr>
      <td>Final</td>
      <td>R</td>
      <td>Forfeit</td>
      <td>RO</td>
      <td>F</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>X</td>
      <td>Unknown</td>
      <td>X</td>
      <td>O</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>W</td>
      <td>Writing</td>
      <td>W</td>
      <td>O</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>

### Transaction Types

<table height=300px border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>code</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SC</td>
      <td>Status Change</td>
    </tr>
    <tr>
      <td>ASG</td>
      <td>Assigned</td>
    </tr>
    <tr>
      <td>DES</td>
      <td>Designated for Assignment</td>
    </tr>
    <tr>
      <td>OPT</td>
      <td>Optioned</td>
    </tr>
    <tr>
      <td>OUT</td>
      <td>Outrighted</td>
    </tr>
    <tr>
      <td>TR</td>
      <td>Trade</td>
    </tr>
    <tr>
      <td>DFA</td>
      <td>Declared Free Agency</td>
    </tr>
    <tr>
      <td>REL</td>
      <td>Released</td>
    </tr>
    <tr>
      <td>URL</td>
      <td>Unconditional Release</td>
    </tr>
    <tr>
      <td>WA</td>
      <td>Waived</td>
    </tr>
    <tr>
      <td>RET</td>
      <td>Retired</td>
    </tr>
    <tr>
      <td>SU</td>
      <td>Suspension</td>
    </tr>
    <tr>
      <td>DEI</td>
      <td>Declared Ineligible</td>
    </tr>
    <tr>
      <td>RES</td>
      <td>Reserved</td>
    </tr>
    <tr>
      <td>DEC</td>
      <td>Deceased</td>
    </tr>
    <tr>
      <td>NUM</td>
      <td>Number Change</td>
    </tr>
    <tr>
      <td>CLW</td>
      <td>Claimed Off Waivers</td>
    </tr>
    <tr>
      <td>PUR</td>
      <td>Purchase</td>
    </tr>
    <tr>
      <td>SGN</td>
      <td>Signed</td>
    </tr>
    <tr>
      <td>SFA</td>
      <td>Signed as Free Agent</td>
    </tr>
    <tr>
      <td>DR</td>
      <td>Drafted</td>
    </tr>
    <tr>
      <td>SE</td>
      <td>Selected</td>
    </tr>
    <tr>
      <td>CU</td>
      <td>Recalled</td>
    </tr>
    <tr>
      <td>RE</td>
      <td>Reinstated</td>
    </tr>
    <tr>
      <td>NC</td>
      <td>New Contract</td>
    </tr>
    <tr>
      <td>CP</td>
      <td>Contract Purchased</td>
    </tr>
    <tr>
      <td>CV</td>
      <td>Contract Void</td>
    </tr>
    <tr>
      <td>ARB</td>
      <td>Offered arbitration</td>
    </tr>
    <tr>
      <td>NOA</td>
      <td>Not offered Arbitration</td>
    </tr>
    <tr>
      <td>REF</td>
      <td>Refused Arbitration</td>
    </tr>
    <tr>
      <td>NTC</td>
      <td>Not Tendered Contract</td>
    </tr>
    <tr>
      <td>LON</td>
      <td>Loan</td>
    </tr>
    <tr>
      <td>RTN</td>
      <td>Returned</td>
    </tr>
    <tr>
      <td>AWD</td>
      <td>Awarded</td>
    </tr>
    <tr>
      <td>TRN</td>
      <td>Transferred</td>
    </tr>
    <tr>
      <td>OBT</td>
      <td>Obtained</td>
    </tr>
    <tr>
      <td>JUM</td>
      <td>Jumped</td>
    </tr>
    <tr>
      <td>R5</td>
      <td>Rule 5 Selection</td>
    </tr>
    <tr>
      <td>R5M</td>
      <td>Rule 5 Draft Minors</td>
    </tr>
  </tbody>
</table>

### Pitch Types

<table height=300px border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>code</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>FA</td>
      <td>Fastball</td>
    </tr>
    <tr>
      <td>FF</td>
      <td>Four-seam FB</td>
    </tr>
    <tr>
      <td>FT</td>
      <td>Two-seam FB</td>
    </tr>
    <tr>
      <td>FC</td>
      <td>Cutter</td>
    </tr>
    <tr>
      <td>FS</td>
      <td>Splitter</td>
    </tr>
    <tr>
      <td>FO</td>
      <td>Forkball</td>
    </tr>
    <tr>
      <td>SI</td>
      <td>Sinker</td>
    </tr>
    <tr>
      <td>ST</td>
      <td>Sweeper</td>
    </tr>
    <tr>
      <td>SL</td>
      <td>Slider</td>
    </tr>
    <tr>
      <td>CU</td>
      <td>Curveball</td>
    </tr>
    <tr>
      <td>KC</td>
      <td>Knuckle Curve</td>
    </tr>
    <tr>
      <td>SC</td>
      <td>Screwball</td>
    </tr>
    <tr>
      <td>GY</td>
      <td>Gyroball</td>
    </tr>
    <tr>
      <td>SV</td>
      <td>Slurve</td>
    </tr>
    <tr>
      <td>CS</td>
      <td>Slow Curve</td>
    </tr>
    <tr>
      <td>CH</td>
      <td>Changeup</td>
    </tr>
    <tr>
      <td>KN</td>
      <td>Knuckleball</td>
    </tr>
    <tr>
      <td>EP</td>
      <td>Eephus Pitch</td>
    </tr>
    <tr>
      <td>UN</td>
      <td>Unknown</td>
    </tr>
    <tr>
      <td>IN</td>
      <td>Intentional Ball</td>
    </tr>
    <tr>
      <td>PO</td>
      <td>Pitchout</td>
    </tr>
    <tr>
      <td>AB</td>
      <td>Automatic Ball</td>
    </tr>
    <tr>
      <td>AS</td>
      <td>Automatic Strike</td>
    </tr>
    <tr>
      <td>NP</td>
      <td>No Pitch</td>
    </tr>
  </tbody>
</table>

### Pitch Codes

<table height=300px border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>code</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>C</td>
      <td>Strike - Called</td>
    </tr>
    <tr>
      <td>B</td>
      <td>Ball - Called</td>
    </tr>
    <tr>
      <td>S</td>
      <td>Strike - Swinging</td>
    </tr>
    <tr>
      <td>V</td>
      <td>Ball - Automatic</td>
    </tr>
    <tr>
      <td>A</td>
      <td>Strike - Automatic</td>
    </tr>
    <tr>
      <td>H</td>
      <td>Ball - Hit by Pitch</td>
    </tr>
    <tr>
      <td>T</td>
      <td>Strike - Foul Tip</td>
    </tr>
    <tr>
      <td>F</td>
      <td>Strike - Foul</td>
    </tr>
    <tr>
      <td>K</td>
      <td>Strike - Unknown</td>
    </tr>
    <tr>
      <td>I</td>
      <td>Ball - Intentional</td>
    </tr>
    <tr>
      <td>P</td>
      <td>Ball - Pitchout</td>
    </tr>
    <tr>
      <td>*B</td>
      <td>Ball - Ball In Dirt</td>
    </tr>
    <tr>
      <td>W</td>
      <td>Strike - Swinging Blocked</td>
    </tr>
    <tr>
      <td>L</td>
      <td>Strike - Foul Bunt</td>
    </tr>
    <tr>
      <td>M</td>
      <td>Strike - Missed Bunt</td>
    </tr>
    <tr>
      <td>O</td>
      <td>Strike - Bunt Foul Tip</td>
    </tr>
    <tr>
      <td>R</td>
      <td>Strike - Foul on Pitchout</td>
    </tr>
    <tr>
      <td>Q</td>
      <td>Strike - Swinging on Pitchout</td>
    </tr>
    <tr>
      <td>X</td>
      <td>Hit Into Play - Out(s)</td>
    </tr>
    <tr>
      <td>E</td>
      <td>Hit Into Play - Run(s)</td>
    </tr>
    <tr>
      <td>D</td>
      <td>Hit Into Play - No Out(s)</td>
    </tr>
    <tr>
      <td>Y</td>
      <td>Pitchout Hit Into Play - Out(s)</td>
    </tr>
    <tr>
      <td>J</td>
      <td>Pitchout Hit Into Play - No Out(s)</td>
    </tr>
    <tr>
      <td>Z</td>
      <td>Pitchout Hit Into Play - Run(s)</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Pickoff Throw 1st - Pitcher</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Pickoff Throw 2nd - Pitcher</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Pickoff Throw 3rd - Pitcher</td>
    </tr>
    <tr>
      <td>+1</td>
      <td>Pickoff Throw 1st - Catcher</td>
    </tr>
    <tr>
      <td>+2</td>
      <td>Pickoff Throw 2nd - Catcher</td>
    </tr>
    <tr>
      <td>+3</td>
      <td>Pickoff Throw 3rd - Catcher</td>
    </tr>
    <tr>
      <td>N</td>
      <td>No Pitch</td>
    </tr>
    <tr>
      <td>VB</td>
      <td>Ball - Automatic (IBB)</td>
    </tr>
    <tr>
      <td>VC</td>
      <td>Ball - Automatic (Pitch Timer Violation - Catcher)</td>
    </tr>
    <tr>
      <td>VP</td>
      <td>Ball - Automatic (Pitch Timer Violation - Pitcher)</td>
    </tr>
    <tr>
      <td>VS</td>
      <td>Ball - Automatic (Shift Violation)</td>
    </tr>
    <tr>
      <td>AC</td>
      <td>Strike - Automatic (Pitch Timer Violation)</td>
    </tr>
    <tr>
      <td>AB</td>
      <td>Strike - Automatic (Batter Timeout Violation)</td>
    </tr>
    <tr>
      <td>PSO</td>
      <td>Pitcher Step Off</td>
    </tr>
    <tr>
      <td>.</td>
      <td>Non Pitch</td>
    </tr>
  </tbody>
</table>

### Event Statuses

<table height=300px border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>code</th>
      <th>detailed_state</th>
      <th>db_code</th>
      <th>abstract_game_state</th>
      <th>start_time_tbd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Scheduled</td>
      <td>S</td>
      <td>Preview</td>
      <td>False</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Scheduled (Time TBD)</td>
      <td>S</td>
      <td>Preview</td>
      <td>False</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Pre-Game</td>
      <td>P</td>
      <td>Preview</td>
      <td>False</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Delayed</td>
      <td>D</td>
      <td>Delayed</td>
      <td>False</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Cancelled</td>
      <td>C</td>
      <td>Cancelled</td>
      <td>False</td>
    </tr>
    <tr>
      <td>3</td>
      <td>In Progress</td>
      <td>I</td>
      <td>Live</td>
      <td>False</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Final</td>
      <td>F</td>
      <td>Final</td>
      <td>False</td>
    </tr>
    <tr>
      <td>110</td>
      <td>Unknown</td>
      <td>X</td>
      <td>Unknown</td>
      <td>False</td>
    </tr>
  </tbody>
</table>

### Positions

<table height=300px border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>short_name</th>
      <th>full_name</th>
      <th>code</th>
      <th>type</th>
      <th>formal_name</th>
      <th>outfield</th>
      <th>display_name</th>
      <th>fielder</th>
      <th>pitcher</th>
      <th>game_position</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Pitcher</td>
      <td>Pitcher</td>
      <td>1</td>
      <td>Pitcher</td>
      <td>Pitcher</td>
      <td>False</td>
      <td>Pitcher</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>Catcher</td>
      <td>Catcher</td>
      <td>2</td>
      <td>Catcher</td>
      <td>Catcher</td>
      <td>False</td>
      <td>Catcher</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>1st Base</td>
      <td>First Base</td>
      <td>3</td>
      <td>Infielder</td>
      <td>First Baseman</td>
      <td>False</td>
      <td>First Base</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>2nd Base</td>
      <td>Second Base</td>
      <td>4</td>
      <td>Infielder</td>
      <td>Second Baseman</td>
      <td>False</td>
      <td>Second Base</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>3rd Base</td>
      <td>Third Base</td>
      <td>5</td>
      <td>Infielder</td>
      <td>Third Baseman</td>
      <td>False</td>
      <td>Third Base</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>Shortstop</td>
      <td>Shortstop</td>
      <td>6</td>
      <td>Infielder</td>
      <td>Shortstop</td>
      <td>False</td>
      <td>Shortstop</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>Left Field</td>
      <td>Outfielder</td>
      <td>7</td>
      <td>Outfielder</td>
      <td>Left Fielder</td>
      <td>True</td>
      <td>Outfielder</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>Center Field</td>
      <td>Outfielder</td>
      <td>8</td>
      <td>Outfielder</td>
      <td>Center Fielder</td>
      <td>True</td>
      <td>Outfielder</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>Right Field</td>
      <td>Outfielder</td>
      <td>9</td>
      <td>Outfielder</td>
      <td>Right Fielder</td>
      <td>True</td>
      <td>Outfielder</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>Designated Hitter</td>
      <td>Designated Hitter</td>
      <td>10</td>
      <td>Hitter</td>
      <td>Designated Hitter</td>
      <td>False</td>
      <td>Designated Hitter</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>Pinch Hitter</td>
      <td>Pinch Hitter</td>
      <td>11</td>
      <td>Hitter</td>
      <td>Pinch Hitter</td>
      <td>False</td>
      <td>Pinch Hitter</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>Pinch Runner</td>
      <td>Pinch Runner</td>
      <td>12</td>
      <td>Runner</td>
      <td>Pinch Runner</td>
      <td>False</td>
      <td>Pinch Runner</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>Extra Hitter</td>
      <td>Extra Hitter</td>
      <td>13</td>
      <td>Hitter</td>
      <td>Extra Hitter</td>
      <td>False</td>
      <td>Extra Hitter</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>Base Runner</td>
      <td>Base Runner</td>
      <td>BR</td>
      <td>Runner</td>
      <td>Base Runner</td>
      <td>False</td>
      <td>Base Runner</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Outfield</td>
      <td>Outfield</td>
      <td>O</td>
      <td>Outfielder</td>
      <td>Outfield</td>
      <td>True</td>
      <td>Outfield</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Infield</td>
      <td>Infield</td>
      <td>I</td>
      <td>Infielder</td>
      <td>Infield</td>
      <td>False</td>
      <td>Infield</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Starting Pitcher</td>
      <td>Starting Pitcher</td>
      <td>S</td>
      <td>Pitcher</td>
      <td>Starting Pitcher</td>
      <td>False</td>
      <td>Starting Pitcher</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Relief Pitcher</td>
      <td>Relief Pitcher</td>
      <td>E</td>
      <td>Pitcher</td>
      <td>Relief Pitcher</td>
      <td>False</td>
      <td>Relief Pitcher</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Closer</td>
      <td>Closer</td>
      <td>C</td>
      <td>Pitcher</td>
      <td>Closer</td>
      <td>False</td>
      <td>Closer</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Utility</td>
      <td>Utility</td>
      <td>U</td>
      <td>Infielder</td>
      <td>Utility</td>
      <td>False</td>
      <td>Utility</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Utility Infielder</td>
      <td>Utility Infielder</td>
      <td>V</td>
      <td>Infielder</td>
      <td>Utility Infielder</td>
      <td>False</td>
      <td>Utility Infielder</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Utility Outfielder</td>
      <td>Utility Outfielder</td>
      <td>W</td>
      <td>Outfielder</td>
      <td>Utility Outfielder</td>
      <td>True</td>
      <td>Utility Outfielder</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Right-Handed Pitcher</td>
      <td>Right-Handed Pitcher</td>
      <td>K</td>
      <td>Pitcher</td>
      <td>Right-Handed Pitcher</td>
      <td>False</td>
      <td>Right-Handed Pitcher</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Left-Handed Pitcher</td>
      <td>Left-Handed Pitcher</td>
      <td>L</td>
      <td>Pitcher</td>
      <td>Left-Handed Pitcher</td>
      <td>False</td>
      <td>Left-Handed Pitcher</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Right-Handed Starter</td>
      <td>Right-Handed Starter</td>
      <td>M</td>
      <td>Pitcher</td>
      <td>Right-Handed Starter</td>
      <td>False</td>
      <td>Right-Handed Starter</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Left-Handed Starter</td>
      <td>Left-Handed Starter</td>
      <td>N</td>
      <td>Pitcher</td>
      <td>Left-Handed Starter</td>
      <td>False</td>
      <td>Left-Handed Starter</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Left-Handed Reliever</td>
      <td>Left-Handed Reliever</td>
      <td>G</td>
      <td>Pitcher</td>
      <td>Left-Handed Reliever</td>
      <td>False</td>
      <td>Left-Handed Reliever</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Right-Handed Reliever</td>
      <td>Right-Handed Reliever</td>
      <td>F</td>
      <td>Pitcher</td>
      <td>Right-Handed Reliever</td>
      <td>False</td>
      <td>Right-Handed Reliever</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Pitcher - Infielder</td>
      <td>Pitcher - Infielder</td>
      <td>A</td>
      <td>Two-Way Player</td>
      <td>Pitcher - Infielder</td>
      <td>False</td>
      <td>Pitcher - Infielder</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Pitcher - Outfielder</td>
      <td>Pitcher - Outfielder</td>
      <td>J</td>
      <td>Two-Way Player</td>
      <td>Pitcher - Outfielder</td>
      <td>True</td>
      <td>Pitcher - Outfielder</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Pitcher - Utility</td>
      <td>Pitcher - Utility</td>
      <td>Z</td>
      <td>Two-Way Player</td>
      <td>Pitcher - Utility</td>
      <td>False</td>
      <td>Pitcher - Utility</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Two-Way Player</td>
      <td>Two-Way Player</td>
      <td>Y</td>
      <td>Two-Way Player</td>
      <td>Two-Way Player</td>
      <td>False</td>
      <td>Two-Way Player</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Batter</td>
      <td>Batter</td>
      <td>10</td>
      <td>Batter</td>
      <td>Batter</td>
      <td>False</td>
      <td>Batter</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>Unknown</td>
      <td>X</td>
      <td>Unknown</td>
      <td>Unknown</td>
      <td>False</td>
      <td>Unknown</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Runner on First</td>
      <td>Runner on First</td>
      <td>R1</td>
      <td>Runner</td>
      <td>Runner on First</td>
      <td>False</td>
      <td>Runner on First</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Runner on Second</td>
      <td>Runner on Second</td>
      <td>R2</td>
      <td>Runner</td>
      <td>Runner on Second</td>
      <td>False</td>
      <td>Runner on Second</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>Runner on Third</td>
      <td>Runner on Third</td>
      <td>R3</td>
      <td>Runner</td>
      <td>Runner on Third</td>
      <td>False</td>
      <td>Runner on Third</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>

### Game Types

<table height=300px border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>id</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>S</td>
      <td>Spring Training</td>
    </tr>
    <tr>
      <td>R</td>
      <td>Regular Season</td>
    </tr>
    <tr>
      <td>F</td>
      <td>Wild Card</td>
    </tr>
    <tr>
      <td>D</td>
      <td>Division Series</td>
    </tr>
    <tr>
      <td>L</td>
      <td>League Championship Series</td>
    </tr>
    <tr>
      <td>W</td>
      <td>World Series</td>
    </tr>
    <tr>
      <td>C</td>
      <td>Championship</td>
    </tr>
    <tr>
      <td>N</td>
      <td>Nineteenth Century Series</td>
    </tr>
    <tr>
      <td>P</td>
      <td>Playoffs</td>
    </tr>
    <tr>
      <td>A</td>
      <td>All-Star Game</td>
    </tr>
    <tr>
      <td>I</td>
      <td>Intrasquad</td>
    </tr>
    <tr>
      <td>E</td>
      <td>Exhibition</td>
    </tr>
  </tbody>
</table>

### Situation Codes

<table height=300px border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>code</th>
      <th>sort_order</th>
      <th>navigation_menu</th>
      <th>description</th>
      <th>team</th>
      <th>batting</th>
      <th>fielding</th>
      <th>pitching</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>h</td>
      <td>1</td>
      <td>Game</td>
      <td>Home Games</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>a</td>
      <td>2</td>
      <td>Game</td>
      <td>Away Games</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>d</td>
      <td>3</td>
      <td>Game</td>
      <td>Day Games</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>n</td>
      <td>4</td>
      <td>Game</td>
      <td>Night Games</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>g</td>
      <td>5</td>
      <td>Game</td>
      <td>On Grass</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>t</td>
      <td>6</td>
      <td>Game</td>
      <td>On Turf</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>2</td>
      <td>20</td>
      <td>Month</td>
      <td>February</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>3</td>
      <td>21</td>
      <td>Month</td>
      <td>March</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>4</td>
      <td>22</td>
      <td>Month</td>
      <td>April</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>5</td>
      <td>23</td>
      <td>Month</td>
      <td>May</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>6</td>
      <td>24</td>
      <td>Month</td>
      <td>June</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>7</td>
      <td>25</td>
      <td>Month</td>
      <td>July</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>8</td>
      <td>26</td>
      <td>Month</td>
      <td>August</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>9</td>
      <td>27</td>
      <td>Month</td>
      <td>September</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>10</td>
      <td>28</td>
      <td>Month</td>
      <td>October</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>11</td>
      <td>29</td>
      <td>Month</td>
      <td>November</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>12</td>
      <td>30</td>
      <td>Month</td>
      <td>December</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>1</td>
      <td>31</td>
      <td>Month</td>
      <td>January</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>h0</td>
      <td>41</td>
      <td>Timeframe</td>
      <td>Season To Date</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>h1</td>
      <td>42</td>
      <td>Timeframe</td>
      <td>First Half</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>h2</td>
      <td>43</td>
      <td>Timeframe</td>
      <td>Second Half</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>preas</td>
      <td>44</td>
      <td>Timeframe</td>
      <td>Pre All-Star</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>posas</td>
      <td>45</td>
      <td>Timeframe</td>
      <td>Post All-Star</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>d1</td>
      <td>46</td>
      <td>Timeframe</td>
      <td>Yesterday</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>d7</td>
      <td>47</td>
      <td>Timeframe</td>
      <td>Last 7 Days</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>d30</td>
      <td>48</td>
      <td>Timeframe</td>
      <td>Last 30 Days</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>dmo</td>
      <td>51</td>
      <td>Day</td>
      <td>On Mondays</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>dtu</td>
      <td>52</td>
      <td>Day</td>
      <td>On Tuesdays</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>dwe</td>
      <td>53</td>
      <td>Day</td>
      <td>On Wednesdays</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>dth</td>
      <td>54</td>
      <td>Day</td>
      <td>On Thursdays</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>dfr</td>
      <td>55</td>
      <td>Day</td>
      <td>On Fridays</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>dsa</td>
      <td>56</td>
      <td>Day</td>
      <td>On Saturdays</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>dsu</td>
      <td>57</td>
      <td>Day</td>
      <td>On Sundays</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>vlg</td>
      <td>61</td>
      <td>Opponent</td>
      <td>vs. League</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vdv</td>
      <td>62</td>
      <td>Opponent</td>
      <td>vs. Division</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vt</td>
      <td>63</td>
      <td>Opponent</td>
      <td>vs. Team</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>val</td>
      <td>64</td>
      <td>Opponent</td>
      <td>vs. AL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>vnl</td>
      <td>65</td>
      <td>Opponent</td>
      <td>vs. NL</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>int</td>
      <td>66</td>
      <td>Opponent</td>
      <td>Interleague</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ven</td>
      <td>67</td>
      <td>Venue</td>
      <td>By Venue</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>l</td>
      <td>71</td>
      <td>At-Bat</td>
      <td>Batting Left</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r</td>
      <td>72</td>
      <td>At-Bat</td>
      <td>Batting Right</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl</td>
      <td>73</td>
      <td>At-Bat</td>
      <td>vs Left</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>vr</td>
      <td>74</td>
      <td>At-Bat</td>
      <td>vs Right</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>vls</td>
      <td>75</td>
      <td>At-Bat</td>
      <td>vs Left Handed Starter</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vrs</td>
      <td>76</td>
      <td>At-Bat</td>
      <td>vs Right Handed Starter</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vgo</td>
      <td>81</td>
      <td>At-Bat</td>
      <td>vs. Ground Ball Pitcher</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vao</td>
      <td>82</td>
      <td>At-Bat</td>
      <td>vs. Fly Ball Pitcher</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vb</td>
      <td>83</td>
      <td>At-Bat</td>
      <td>vs. Batter</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>vp</td>
      <td>84</td>
      <td>At-Bat</td>
      <td>vs. Pitcher</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>1r</td>
      <td>91</td>
      <td>Score</td>
      <td>One Run</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>sah</td>
      <td>92</td>
      <td>Score</td>
      <td>Team is ahead</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>sbh</td>
      <td>93</td>
      <td>Score</td>
      <td>Team is behind</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>sti</td>
      <td>94</td>
      <td>Score</td>
      <td>Score is tied</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>ex</td>
      <td>95</td>
      <td>Inning</td>
      <td>Extra Innnings</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>l10</td>
      <td>96</td>
      <td>Timeframe</td>
      <td>Last 10</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>twn</td>
      <td>101</td>
      <td>Result</td>
      <td>In games won by team</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>tls</td>
      <td>102</td>
      <td>Result</td>
      <td>In games lost by team</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>tti</td>
      <td>103</td>
      <td>Result</td>
      <td>In tie games</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>taw</td>
      <td>104</td>
      <td>Result</td>
      <td>In games following a win</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>tal</td>
      <td>105</td>
      <td>Result</td>
      <td>In games following a loss</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>tat</td>
      <td>106</td>
      <td>Result</td>
      <td>In games following a tie</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>b1</td>
      <td>111</td>
      <td>Order</td>
      <td>Batting First</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>b2</td>
      <td>112</td>
      <td>Order</td>
      <td>Batting Second</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>b3</td>
      <td>113</td>
      <td>Order</td>
      <td>Batting Third</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>b4</td>
      <td>114</td>
      <td>Order</td>
      <td>Batting Fourth</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>b5</td>
      <td>115</td>
      <td>Order</td>
      <td>Batting Fifth</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>b6</td>
      <td>116</td>
      <td>Order</td>
      <td>Batting Sixth</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>b7</td>
      <td>117</td>
      <td>Order</td>
      <td>Batting Seventh</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>b8</td>
      <td>118</td>
      <td>Order</td>
      <td>Batting Eighth</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>b9</td>
      <td>119</td>
      <td>Order</td>
      <td>Batting Ninth</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>lo</td>
      <td>120</td>
      <td>Runners</td>
      <td>Leading Off</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>p1</td>
      <td>121</td>
      <td>Position</td>
      <td>Pitcher</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>p2</td>
      <td>122</td>
      <td>Position</td>
      <td>Catcher</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>p3</td>
      <td>123</td>
      <td>Position</td>
      <td>First Base</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>p4</td>
      <td>124</td>
      <td>Position</td>
      <td>Second Base</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>p5</td>
      <td>125</td>
      <td>Position</td>
      <td>Third Base</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>p6</td>
      <td>126</td>
      <td>Position</td>
      <td>Shortstop</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>p7</td>
      <td>127</td>
      <td>Position</td>
      <td>Left Field</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>p8</td>
      <td>128</td>
      <td>Position</td>
      <td>Center Field</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>p9</td>
      <td>129</td>
      <td>Position</td>
      <td>Right Field</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pO</td>
      <td>130</td>
      <td>Position</td>
      <td>Outfield</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>sp</td>
      <td>131</td>
      <td>Pitching</td>
      <td>Starter</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>rp</td>
      <td>132</td>
      <td>Pitching</td>
      <td>Reliever</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pD</td>
      <td>133</td>
      <td>Position</td>
      <td>Designated Hitter</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pH</td>
      <td>134</td>
      <td>Position</td>
      <td>Pinch Hitter</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pR</td>
      <td>135</td>
      <td>Position</td>
      <td>Pinch Runner</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pX</td>
      <td>136</td>
      <td>Position</td>
      <td>Undefined (e.g. PH bats twice in an inning)</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>dr1</td>
      <td>141</td>
      <td>Pitching</td>
      <td>One Day of Rest</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>dr2</td>
      <td>142</td>
      <td>Pitching</td>
      <td>Two Days of Rest</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>dr3</td>
      <td>143</td>
      <td>Pitching</td>
      <td>Three Days of Rest</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>dr4</td>
      <td>144</td>
      <td>Pitching</td>
      <td>Four Days of Rest</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>dr5</td>
      <td>145</td>
      <td>Pitching</td>
      <td>Five Plus Days of Rest</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>fip</td>
      <td>146</td>
      <td>Pitching</td>
      <td>First Inning Pitched</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>fba</td>
      <td>147</td>
      <td>Pitching</td>
      <td>First Batter (RP Only)</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>i01</td>
      <td>151</td>
      <td>Inning</td>
      <td>First Inning</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>i02</td>
      <td>152</td>
      <td>Inning</td>
      <td>Second Inning</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>i03</td>
      <td>153</td>
      <td>Inning</td>
      <td>Third Inning</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>i04</td>
      <td>154</td>
      <td>Inning</td>
      <td>Fourth Inning</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>i05</td>
      <td>155</td>
      <td>Inning</td>
      <td>Fifth Inning</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>i06</td>
      <td>156</td>
      <td>Inning</td>
      <td>Sixth Inning</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>i07</td>
      <td>157</td>
      <td>Inning</td>
      <td>Seventh Inning</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>i08</td>
      <td>158</td>
      <td>Inning</td>
      <td>Eighth Inning</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>i09</td>
      <td>159</td>
      <td>Inning</td>
      <td>Ninth Inning</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>ix</td>
      <td>160</td>
      <td>Inning</td>
      <td>Extra Innings</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>ig01</td>
      <td>161</td>
      <td>Inning</td>
      <td>Innings One to Six</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>ig07</td>
      <td>162</td>
      <td>Inning</td>
      <td>Seventh or Later</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>ig08</td>
      <td>163</td>
      <td>Inning</td>
      <td>Eighth or Later</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>ig09</td>
      <td>164</td>
      <td>Inning</td>
      <td>Ninth or Later</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pi000</td>
      <td>171</td>
      <td>Pitch Count</td>
      <td>First 75 Pitches</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pi760</td>
      <td>172</td>
      <td>Pitch Count</td>
      <td>Pitches 76 and Later</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pi100</td>
      <td>173</td>
      <td>Pitch Count</td>
      <td>First 100 Pitches</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pi101</td>
      <td>174</td>
      <td>Pitch Count</td>
      <td>Pitches 101 and Later</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pi001</td>
      <td>175</td>
      <td>Pitch Count</td>
      <td>Pitches 1-15</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pi016</td>
      <td>176</td>
      <td>Pitch Count</td>
      <td>Pitches 16-30</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pi031</td>
      <td>177</td>
      <td>Pitch Count</td>
      <td>Pitches 31-45</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pi046</td>
      <td>178</td>
      <td>Pitch Count</td>
      <td>Pitches 46-60</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pi061</td>
      <td>179</td>
      <td>Pitch Count</td>
      <td>Pitches 61-75</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pi076</td>
      <td>180</td>
      <td>Pitch Count</td>
      <td>Pitches 76-90</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pi091</td>
      <td>181</td>
      <td>Pitch Count</td>
      <td>Pitches 91-105</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pi106</td>
      <td>182</td>
      <td>Pitch Count</td>
      <td>Pitches 106-120</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>pi121</td>
      <td>183</td>
      <td>Pitch Count</td>
      <td>Pitches 121 or Later</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>e</td>
      <td>192</td>
      <td>Runners</td>
      <td>Empty (Not Leadoff)</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>r0</td>
      <td>193</td>
      <td>Runners</td>
      <td>Bases Empty</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>r123</td>
      <td>194</td>
      <td>Runners</td>
      <td>Bases Loaded</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>r1</td>
      <td>195</td>
      <td>Runners</td>
      <td>Runner at 1st</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>r12</td>
      <td>196</td>
      <td>Runners</td>
      <td>Runners at 1st &amp; 2nd</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>r13</td>
      <td>197</td>
      <td>Runners</td>
      <td>Runners at 1st &amp; 3rd</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>r2</td>
      <td>198</td>
      <td>Runners</td>
      <td>Runner at 2nd</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>r23</td>
      <td>199</td>
      <td>Runners</td>
      <td>Runners at 2nd &amp; 3rd</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>r3</td>
      <td>200</td>
      <td>Runners</td>
      <td>Runner at 3rd</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>ron</td>
      <td>201</td>
      <td>Runners</td>
      <td>Runners On</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>ron2</td>
      <td>202</td>
      <td>Runners</td>
      <td>Runners On - 2 Outs</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>risp</td>
      <td>203</td>
      <td>Runners</td>
      <td>Scoring Position</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>risp2</td>
      <td>204</td>
      <td>Runners</td>
      <td>Scoring Position - 2 Outs</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>r3l2</td>
      <td>205</td>
      <td>Runners</td>
      <td>3rd, Less than 2 Outs</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>o0</td>
      <td>211</td>
      <td>Outs</td>
      <td>No Outs</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>o1</td>
      <td>212</td>
      <td>Outs</td>
      <td>One Out</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>o2</td>
      <td>213</td>
      <td>Outs</td>
      <td>Two Outs</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>lc</td>
      <td>214</td>
      <td>Score</td>
      <td>Late / Close</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>fp</td>
      <td>221</td>
      <td>Count</td>
      <td>First Pitch</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>ac</td>
      <td>222</td>
      <td>Count</td>
      <td>Ahead in Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>bc</td>
      <td>223</td>
      <td>Count</td>
      <td>Behind in Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>ec</td>
      <td>224</td>
      <td>Count</td>
      <td>Even Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>2s</td>
      <td>225</td>
      <td>Count</td>
      <td>Two Strikes</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>fc</td>
      <td>226</td>
      <td>Count</td>
      <td>Full Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>uc</td>
      <td>227</td>
      <td>Count</td>
      <td>Unknown or no Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>c00</td>
      <td>228</td>
      <td>Count</td>
      <td>0-0 Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>c01</td>
      <td>229</td>
      <td>Count</td>
      <td>0-1 Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>c02</td>
      <td>230</td>
      <td>Count</td>
      <td>0-2 Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>c10</td>
      <td>231</td>
      <td>Count</td>
      <td>1-0 Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>c11</td>
      <td>232</td>
      <td>Count</td>
      <td>1-1 Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>c12</td>
      <td>233</td>
      <td>Count</td>
      <td>1-2 Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>c20</td>
      <td>234</td>
      <td>Count</td>
      <td>2-0 Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>c21</td>
      <td>235</td>
      <td>Count</td>
      <td>2-1 Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>c22</td>
      <td>236</td>
      <td>Count</td>
      <td>2-2 Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>c30</td>
      <td>237</td>
      <td>Count</td>
      <td>3-0 Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>c31</td>
      <td>238</td>
      <td>Count</td>
      <td>3-1 Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>c32</td>
      <td>239</td>
      <td>Count</td>
      <td>3-2 Count</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <td>hh1</td>
      <td>301</td>
      <td>NaN</td>
      <td>Home Games - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ah1</td>
      <td>302</td>
      <td>NaN</td>
      <td>Away Games - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>dh1</td>
      <td>303</td>
      <td>NaN</td>
      <td>Day Games - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>nh1</td>
      <td>304</td>
      <td>NaN</td>
      <td>Night Games - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>gh1</td>
      <td>305</td>
      <td>NaN</td>
      <td>On Grass - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>th1</td>
      <td>306</td>
      <td>NaN</td>
      <td>On Turf - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>3h1</td>
      <td>311</td>
      <td>NaN</td>
      <td>March - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>4h1</td>
      <td>312</td>
      <td>NaN</td>
      <td>April - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>5h1</td>
      <td>313</td>
      <td>NaN</td>
      <td>May - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>6h1</td>
      <td>314</td>
      <td>NaN</td>
      <td>June - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>7h1</td>
      <td>315</td>
      <td>NaN</td>
      <td>July - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>8h1</td>
      <td>316</td>
      <td>NaN</td>
      <td>August - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>9h1</td>
      <td>317</td>
      <td>NaN</td>
      <td>September - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>10h1</td>
      <td>318</td>
      <td>NaN</td>
      <td>October - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>11h1</td>
      <td>319</td>
      <td>NaN</td>
      <td>November - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>12h1</td>
      <td>320</td>
      <td>NaN</td>
      <td>December - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>1h1</td>
      <td>321</td>
      <td>NaN</td>
      <td>January - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>2h1</td>
      <td>322</td>
      <td>NaN</td>
      <td>February - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vlgh1</td>
      <td>331</td>
      <td>NaN</td>
      <td>vs. League - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vdvh1</td>
      <td>332</td>
      <td>NaN</td>
      <td>vs. Division - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vth1</td>
      <td>333</td>
      <td>NaN</td>
      <td>vs. Team - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>1rh1</td>
      <td>341</td>
      <td>NaN</td>
      <td>One Run - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>exh1</td>
      <td>351</td>
      <td>NaN</td>
      <td>Extra Innnings - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>l10h1</td>
      <td>352</td>
      <td>NaN</td>
      <td>Last 10 - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vlsh1</td>
      <td>353</td>
      <td>NaN</td>
      <td>vs Left Handed Starter - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vrsh1</td>
      <td>354</td>
      <td>NaN</td>
      <td>vs Right Handed Starter - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>twnh1</td>
      <td>361</td>
      <td>NaN</td>
      <td>In games won by team - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>tlsh1</td>
      <td>362</td>
      <td>NaN</td>
      <td>In games lost by team - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ttih1</td>
      <td>363</td>
      <td>NaN</td>
      <td>In tie games - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>tawh1</td>
      <td>364</td>
      <td>NaN</td>
      <td>In games following a win - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>talh1</td>
      <td>365</td>
      <td>NaN</td>
      <td>In games following a loss - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>tath1</td>
      <td>366</td>
      <td>NaN</td>
      <td>In games following a tie - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>hh2</td>
      <td>401</td>
      <td>NaN</td>
      <td>Home Games - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ah2</td>
      <td>402</td>
      <td>NaN</td>
      <td>Away Games - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>dh2</td>
      <td>403</td>
      <td>NaN</td>
      <td>Day Games - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>nh2</td>
      <td>404</td>
      <td>NaN</td>
      <td>Night Games - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>gh2</td>
      <td>405</td>
      <td>NaN</td>
      <td>On Grass - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>th2</td>
      <td>406</td>
      <td>NaN</td>
      <td>On Turf - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>3h2</td>
      <td>411</td>
      <td>NaN</td>
      <td>March - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>4h2</td>
      <td>412</td>
      <td>NaN</td>
      <td>April - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>5h2</td>
      <td>413</td>
      <td>NaN</td>
      <td>May - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>6h2</td>
      <td>414</td>
      <td>NaN</td>
      <td>June - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>7h2</td>
      <td>415</td>
      <td>NaN</td>
      <td>July - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>8h2</td>
      <td>416</td>
      <td>NaN</td>
      <td>August - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>9h2</td>
      <td>417</td>
      <td>NaN</td>
      <td>September - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>10h2</td>
      <td>418</td>
      <td>NaN</td>
      <td>October - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>11h2</td>
      <td>419</td>
      <td>NaN</td>
      <td>November - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>12h2</td>
      <td>420</td>
      <td>NaN</td>
      <td>December - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>1h2</td>
      <td>421</td>
      <td>NaN</td>
      <td>January - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>2h2</td>
      <td>422</td>
      <td>NaN</td>
      <td>February - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vlgh2</td>
      <td>431</td>
      <td>NaN</td>
      <td>vs. League - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vdvh2</td>
      <td>432</td>
      <td>NaN</td>
      <td>vs. Division - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vth2</td>
      <td>433</td>
      <td>NaN</td>
      <td>vs. Team - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>1rh2</td>
      <td>441</td>
      <td>NaN</td>
      <td>One Run - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>exh2</td>
      <td>442</td>
      <td>NaN</td>
      <td>Extra Innnings - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>l10h2</td>
      <td>443</td>
      <td>NaN</td>
      <td>Last 10 - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vlsh2</td>
      <td>444</td>
      <td>NaN</td>
      <td>vs Left Handed Starter - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vrsh2</td>
      <td>445</td>
      <td>NaN</td>
      <td>vs Right Handed Starter - first half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>twnh2</td>
      <td>451</td>
      <td>NaN</td>
      <td>In games won by team - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>tlsh2</td>
      <td>452</td>
      <td>NaN</td>
      <td>In games lost by team - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ttih2</td>
      <td>453</td>
      <td>NaN</td>
      <td>In tie games - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>tawh2</td>
      <td>454</td>
      <td>NaN</td>
      <td>In games following a win - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>talh2</td>
      <td>455</td>
      <td>NaN</td>
      <td>In games following a loss - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>tath2</td>
      <td>456</td>
      <td>NaN</td>
      <td>In games following a tie - second half</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa</td>
      <td>501</td>
      <td>Pitch Type</td>
      <td>Fastball</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff</td>
      <td>502</td>
      <td>Pitch Type</td>
      <td>Four-seam FB</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft</td>
      <td>503</td>
      <td>Pitch Type</td>
      <td>Two-seam FB</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc</td>
      <td>504</td>
      <td>Pitch Type</td>
      <td>Cutter</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi</td>
      <td>505</td>
      <td>Pitch Type</td>
      <td>Sinker</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs</td>
      <td>506</td>
      <td>Pitch Type</td>
      <td>Splitter</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo</td>
      <td>507</td>
      <td>Pitch Type</td>
      <td>Forkball</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl</td>
      <td>508</td>
      <td>Pitch Type</td>
      <td>Slider</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu</td>
      <td>509</td>
      <td>Pitch Type</td>
      <td>Curveball</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc</td>
      <td>510</td>
      <td>Pitch Type</td>
      <td>Knuckle Curve</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc</td>
      <td>511</td>
      <td>Pitch Type</td>
      <td>Screwball</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy</td>
      <td>512</td>
      <td>Pitch Type</td>
      <td>Gyroball</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch</td>
      <td>513</td>
      <td>Pitch Type</td>
      <td>Changeup</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn</td>
      <td>514</td>
      <td>Pitch Type</td>
      <td>Knuckleball</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep</td>
      <td>515</td>
      <td>Pitch Type</td>
      <td>Eephus Pitch</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>zn01</td>
      <td>521</td>
      <td>NaN</td>
      <td>Pitches in Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>zn02</td>
      <td>522</td>
      <td>NaN</td>
      <td>Pitches in Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>zn03</td>
      <td>523</td>
      <td>NaN</td>
      <td>Pitches in Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>zn04</td>
      <td>524</td>
      <td>NaN</td>
      <td>Pitches in Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>zn05</td>
      <td>525</td>
      <td>NaN</td>
      <td>Pitches in Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>zn06</td>
      <td>526</td>
      <td>NaN</td>
      <td>Pitches in Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>zn07</td>
      <td>527</td>
      <td>NaN</td>
      <td>Pitches in Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>zn08</td>
      <td>528</td>
      <td>NaN</td>
      <td>Pitches in Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>zn09</td>
      <td>529</td>
      <td>NaN</td>
      <td>Pitches in Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>zn11</td>
      <td>531</td>
      <td>NaN</td>
      <td>Pitches in Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>zn12</td>
      <td>532</td>
      <td>NaN</td>
      <td>Pitches in Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>zn13</td>
      <td>533</td>
      <td>NaN</td>
      <td>Pitches in Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>zn14</td>
      <td>534</td>
      <td>NaN</td>
      <td>Pitches in Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa01</td>
      <td>601</td>
      <td>NaN</td>
      <td>Fastball Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa02</td>
      <td>602</td>
      <td>NaN</td>
      <td>Fastball Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa03</td>
      <td>603</td>
      <td>NaN</td>
      <td>Fastball Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa04</td>
      <td>604</td>
      <td>NaN</td>
      <td>Fastball Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa05</td>
      <td>605</td>
      <td>NaN</td>
      <td>Fastball Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa06</td>
      <td>606</td>
      <td>NaN</td>
      <td>Fastball Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa07</td>
      <td>607</td>
      <td>NaN</td>
      <td>Fastball Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa08</td>
      <td>608</td>
      <td>NaN</td>
      <td>Fastball Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa09</td>
      <td>609</td>
      <td>NaN</td>
      <td>Fastball Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa11</td>
      <td>611</td>
      <td>NaN</td>
      <td>Fastball Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa12</td>
      <td>612</td>
      <td>NaN</td>
      <td>Fastball Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa13</td>
      <td>613</td>
      <td>NaN</td>
      <td>Fastball Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfa14</td>
      <td>614</td>
      <td>NaN</td>
      <td>Fastball Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft01</td>
      <td>621</td>
      <td>NaN</td>
      <td>Two-seam FB Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft02</td>
      <td>622</td>
      <td>NaN</td>
      <td>Two-seam FB Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft03</td>
      <td>623</td>
      <td>NaN</td>
      <td>Two-seam FB Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft04</td>
      <td>624</td>
      <td>NaN</td>
      <td>Two-seam FB Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft05</td>
      <td>625</td>
      <td>NaN</td>
      <td>Two-seam FB Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft06</td>
      <td>626</td>
      <td>NaN</td>
      <td>Two-seam FB Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft07</td>
      <td>627</td>
      <td>NaN</td>
      <td>Two-seam FB Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft08</td>
      <td>628</td>
      <td>NaN</td>
      <td>Two-seam FB Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft09</td>
      <td>629</td>
      <td>NaN</td>
      <td>Two-seam FB Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft11</td>
      <td>631</td>
      <td>NaN</td>
      <td>Two-seam FB Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft12</td>
      <td>632</td>
      <td>NaN</td>
      <td>Two-seam FB Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft13</td>
      <td>633</td>
      <td>NaN</td>
      <td>Two-seam FB Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pft14</td>
      <td>634</td>
      <td>NaN</td>
      <td>Two-seam FB Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff01</td>
      <td>641</td>
      <td>NaN</td>
      <td>Four-seam Fastball Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff02</td>
      <td>642</td>
      <td>NaN</td>
      <td>Four-seam Fastball Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff03</td>
      <td>643</td>
      <td>NaN</td>
      <td>Four-seam Fastball Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff04</td>
      <td>644</td>
      <td>NaN</td>
      <td>Four-seam Fastball Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff05</td>
      <td>645</td>
      <td>NaN</td>
      <td>Four-seam Fastball Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff06</td>
      <td>646</td>
      <td>NaN</td>
      <td>Four-seam Fastball Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff07</td>
      <td>647</td>
      <td>NaN</td>
      <td>Four-seam Fastball Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff08</td>
      <td>648</td>
      <td>NaN</td>
      <td>Four-seam Fastball Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff09</td>
      <td>649</td>
      <td>NaN</td>
      <td>Four-seam Fastball Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff11</td>
      <td>651</td>
      <td>NaN</td>
      <td>Four-seam Fastball Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff12</td>
      <td>652</td>
      <td>NaN</td>
      <td>Four-seam Fastball Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff13</td>
      <td>653</td>
      <td>NaN</td>
      <td>Four-seam Fastball Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pff14</td>
      <td>654</td>
      <td>NaN</td>
      <td>Four-seam Fastball Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc01</td>
      <td>661</td>
      <td>NaN</td>
      <td>Cutter Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc02</td>
      <td>662</td>
      <td>NaN</td>
      <td>Cutter Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc03</td>
      <td>663</td>
      <td>NaN</td>
      <td>Cutter Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc04</td>
      <td>664</td>
      <td>NaN</td>
      <td>Cutter Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc05</td>
      <td>665</td>
      <td>NaN</td>
      <td>Cutter Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc06</td>
      <td>666</td>
      <td>NaN</td>
      <td>Cutter Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc07</td>
      <td>667</td>
      <td>NaN</td>
      <td>Cutter Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc08</td>
      <td>668</td>
      <td>NaN</td>
      <td>Cutter Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc09</td>
      <td>669</td>
      <td>NaN</td>
      <td>Cutter Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc11</td>
      <td>671</td>
      <td>NaN</td>
      <td>Cutter Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc12</td>
      <td>672</td>
      <td>NaN</td>
      <td>Cutter Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc13</td>
      <td>673</td>
      <td>NaN</td>
      <td>Cutter Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfc14</td>
      <td>674</td>
      <td>NaN</td>
      <td>Cutter Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs01</td>
      <td>681</td>
      <td>NaN</td>
      <td>Splitter Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs02</td>
      <td>682</td>
      <td>NaN</td>
      <td>Splitter Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs03</td>
      <td>683</td>
      <td>NaN</td>
      <td>Splitter Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs04</td>
      <td>684</td>
      <td>NaN</td>
      <td>Splitter Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs05</td>
      <td>685</td>
      <td>NaN</td>
      <td>Splitter Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs06</td>
      <td>686</td>
      <td>NaN</td>
      <td>Splitter Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs07</td>
      <td>687</td>
      <td>NaN</td>
      <td>Splitter Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs08</td>
      <td>688</td>
      <td>NaN</td>
      <td>Splitter Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs09</td>
      <td>689</td>
      <td>NaN</td>
      <td>Splitter Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs11</td>
      <td>691</td>
      <td>NaN</td>
      <td>Splitter Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs12</td>
      <td>692</td>
      <td>NaN</td>
      <td>Splitter Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs13</td>
      <td>693</td>
      <td>NaN</td>
      <td>Splitter Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfs14</td>
      <td>694</td>
      <td>NaN</td>
      <td>Splitter Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy01</td>
      <td>701</td>
      <td>NaN</td>
      <td>Gyroball Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy02</td>
      <td>702</td>
      <td>NaN</td>
      <td>Gyroball Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy03</td>
      <td>703</td>
      <td>NaN</td>
      <td>Gyroball Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy04</td>
      <td>704</td>
      <td>NaN</td>
      <td>Gyroball Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy05</td>
      <td>705</td>
      <td>NaN</td>
      <td>Gyroball Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy06</td>
      <td>706</td>
      <td>NaN</td>
      <td>Gyroball Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy07</td>
      <td>707</td>
      <td>NaN</td>
      <td>Gyroball Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy08</td>
      <td>708</td>
      <td>NaN</td>
      <td>Gyroball Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy09</td>
      <td>709</td>
      <td>NaN</td>
      <td>Gyroball Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy11</td>
      <td>711</td>
      <td>NaN</td>
      <td>Gyroball Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy12</td>
      <td>712</td>
      <td>NaN</td>
      <td>Gyroball Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy13</td>
      <td>713</td>
      <td>NaN</td>
      <td>Gyroball Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pgy14</td>
      <td>714</td>
      <td>NaN</td>
      <td>Gyroball Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch01</td>
      <td>721</td>
      <td>NaN</td>
      <td>Changeup Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch02</td>
      <td>722</td>
      <td>NaN</td>
      <td>Changeup Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch03</td>
      <td>723</td>
      <td>NaN</td>
      <td>Changeup Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch04</td>
      <td>724</td>
      <td>NaN</td>
      <td>Changeup Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch05</td>
      <td>725</td>
      <td>NaN</td>
      <td>Changeup Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch06</td>
      <td>726</td>
      <td>NaN</td>
      <td>Changeup Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch07</td>
      <td>727</td>
      <td>NaN</td>
      <td>Changeup Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch08</td>
      <td>728</td>
      <td>NaN</td>
      <td>Changeup Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch09</td>
      <td>729</td>
      <td>NaN</td>
      <td>Changeup Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch11</td>
      <td>731</td>
      <td>NaN</td>
      <td>Changeup Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch12</td>
      <td>732</td>
      <td>NaN</td>
      <td>Changeup Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch13</td>
      <td>733</td>
      <td>NaN</td>
      <td>Changeup Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pch14</td>
      <td>734</td>
      <td>NaN</td>
      <td>Changeup Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo01</td>
      <td>741</td>
      <td>NaN</td>
      <td>Forkball Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo02</td>
      <td>742</td>
      <td>NaN</td>
      <td>Forkball Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo03</td>
      <td>743</td>
      <td>NaN</td>
      <td>Forkball Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo04</td>
      <td>744</td>
      <td>NaN</td>
      <td>Forkball Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo05</td>
      <td>745</td>
      <td>NaN</td>
      <td>Forkball Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo06</td>
      <td>746</td>
      <td>NaN</td>
      <td>Forkball Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo07</td>
      <td>747</td>
      <td>NaN</td>
      <td>Forkball Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo08</td>
      <td>748</td>
      <td>NaN</td>
      <td>Forkball Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo09</td>
      <td>749</td>
      <td>NaN</td>
      <td>Forkball Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo11</td>
      <td>751</td>
      <td>NaN</td>
      <td>Forkball Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo12</td>
      <td>752</td>
      <td>NaN</td>
      <td>Forkball Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo13</td>
      <td>753</td>
      <td>NaN</td>
      <td>Forkball Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pfo14</td>
      <td>754</td>
      <td>NaN</td>
      <td>Forkball Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi01</td>
      <td>761</td>
      <td>NaN</td>
      <td>Sinker Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi02</td>
      <td>762</td>
      <td>NaN</td>
      <td>Sinker Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi03</td>
      <td>763</td>
      <td>NaN</td>
      <td>Sinker Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi04</td>
      <td>764</td>
      <td>NaN</td>
      <td>Sinker Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi05</td>
      <td>765</td>
      <td>NaN</td>
      <td>Sinker Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi06</td>
      <td>766</td>
      <td>NaN</td>
      <td>Sinker Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi07</td>
      <td>767</td>
      <td>NaN</td>
      <td>Sinker Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi08</td>
      <td>768</td>
      <td>NaN</td>
      <td>Sinker Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi09</td>
      <td>769</td>
      <td>NaN</td>
      <td>Sinker Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi11</td>
      <td>771</td>
      <td>NaN</td>
      <td>Sinker Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi12</td>
      <td>772</td>
      <td>NaN</td>
      <td>Sinker Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi13</td>
      <td>773</td>
      <td>NaN</td>
      <td>Sinker Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psi14</td>
      <td>774</td>
      <td>NaN</td>
      <td>Sinker Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl01</td>
      <td>781</td>
      <td>NaN</td>
      <td>Slider Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl02</td>
      <td>782</td>
      <td>NaN</td>
      <td>Slider Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl03</td>
      <td>783</td>
      <td>NaN</td>
      <td>Slider Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl04</td>
      <td>784</td>
      <td>NaN</td>
      <td>Slider Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl05</td>
      <td>785</td>
      <td>NaN</td>
      <td>Slider Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl06</td>
      <td>786</td>
      <td>NaN</td>
      <td>Slider Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl07</td>
      <td>787</td>
      <td>NaN</td>
      <td>Slider Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl08</td>
      <td>788</td>
      <td>NaN</td>
      <td>Slider Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl09</td>
      <td>789</td>
      <td>NaN</td>
      <td>Slider Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl11</td>
      <td>791</td>
      <td>NaN</td>
      <td>Slider Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl12</td>
      <td>792</td>
      <td>NaN</td>
      <td>Slider Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl13</td>
      <td>793</td>
      <td>NaN</td>
      <td>Slider Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psl14</td>
      <td>794</td>
      <td>NaN</td>
      <td>Slider Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu01</td>
      <td>801</td>
      <td>NaN</td>
      <td>Curveball Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu02</td>
      <td>802</td>
      <td>NaN</td>
      <td>Curveball Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu03</td>
      <td>803</td>
      <td>NaN</td>
      <td>Curveball Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu04</td>
      <td>804</td>
      <td>NaN</td>
      <td>Curveball Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu05</td>
      <td>805</td>
      <td>NaN</td>
      <td>Curveball Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu06</td>
      <td>806</td>
      <td>NaN</td>
      <td>Curveball Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu07</td>
      <td>807</td>
      <td>NaN</td>
      <td>Curveball Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu08</td>
      <td>808</td>
      <td>NaN</td>
      <td>Curveball Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu09</td>
      <td>809</td>
      <td>NaN</td>
      <td>Curveball Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu11</td>
      <td>811</td>
      <td>NaN</td>
      <td>Curveball Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu12</td>
      <td>812</td>
      <td>NaN</td>
      <td>Curveball Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu13</td>
      <td>813</td>
      <td>NaN</td>
      <td>Curveball Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pcu14</td>
      <td>814</td>
      <td>NaN</td>
      <td>Curveball Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc01</td>
      <td>821</td>
      <td>NaN</td>
      <td>Knuckle Curve Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc02</td>
      <td>822</td>
      <td>NaN</td>
      <td>Knuckle Curve Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc03</td>
      <td>823</td>
      <td>NaN</td>
      <td>Knuckle Curve Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc04</td>
      <td>824</td>
      <td>NaN</td>
      <td>Knuckle Curve Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc05</td>
      <td>825</td>
      <td>NaN</td>
      <td>Knuckle Curve Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc06</td>
      <td>826</td>
      <td>NaN</td>
      <td>Knuckle Curve Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc07</td>
      <td>827</td>
      <td>NaN</td>
      <td>Knuckle Curve Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc08</td>
      <td>828</td>
      <td>NaN</td>
      <td>Knuckle Curve Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc09</td>
      <td>829</td>
      <td>NaN</td>
      <td>Knuckle Curve Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc11</td>
      <td>831</td>
      <td>NaN</td>
      <td>Knuckle Curve Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc12</td>
      <td>832</td>
      <td>NaN</td>
      <td>Knuckle Curve Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc13</td>
      <td>833</td>
      <td>NaN</td>
      <td>Knuckle Curve Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkc14</td>
      <td>834</td>
      <td>NaN</td>
      <td>Knuckle Curve Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn01</td>
      <td>841</td>
      <td>NaN</td>
      <td>Knuckleball Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn02</td>
      <td>842</td>
      <td>NaN</td>
      <td>Knuckleball Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn03</td>
      <td>843</td>
      <td>NaN</td>
      <td>Knuckleball Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn04</td>
      <td>844</td>
      <td>NaN</td>
      <td>Knuckleball Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn05</td>
      <td>845</td>
      <td>NaN</td>
      <td>Knuckleball Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn06</td>
      <td>846</td>
      <td>NaN</td>
      <td>Knuckleball Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn07</td>
      <td>847</td>
      <td>NaN</td>
      <td>Knuckleball Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn08</td>
      <td>848</td>
      <td>NaN</td>
      <td>Knuckleball Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn09</td>
      <td>849</td>
      <td>NaN</td>
      <td>Knuckleball Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn11</td>
      <td>851</td>
      <td>NaN</td>
      <td>Knuckleball Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn12</td>
      <td>852</td>
      <td>NaN</td>
      <td>Knuckleball Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn13</td>
      <td>853</td>
      <td>NaN</td>
      <td>Knuckleball Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pkn14</td>
      <td>854</td>
      <td>NaN</td>
      <td>Knuckleball Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc01</td>
      <td>861</td>
      <td>NaN</td>
      <td>Screwball Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc02</td>
      <td>862</td>
      <td>NaN</td>
      <td>Screwball Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc03</td>
      <td>863</td>
      <td>NaN</td>
      <td>Screwball Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc04</td>
      <td>864</td>
      <td>NaN</td>
      <td>Screwball Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc05</td>
      <td>865</td>
      <td>NaN</td>
      <td>Screwball Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc06</td>
      <td>866</td>
      <td>NaN</td>
      <td>Screwball Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc07</td>
      <td>867</td>
      <td>NaN</td>
      <td>Screwball Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc08</td>
      <td>868</td>
      <td>NaN</td>
      <td>Screwball Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc09</td>
      <td>869</td>
      <td>NaN</td>
      <td>Screwball Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc11</td>
      <td>871</td>
      <td>NaN</td>
      <td>Screwball Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc12</td>
      <td>872</td>
      <td>NaN</td>
      <td>Screwball Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc13</td>
      <td>873</td>
      <td>NaN</td>
      <td>Screwball Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>psc14</td>
      <td>874</td>
      <td>NaN</td>
      <td>Screwball Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep01</td>
      <td>881</td>
      <td>NaN</td>
      <td>Eephus Pitch Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep02</td>
      <td>882</td>
      <td>NaN</td>
      <td>Eephus Pitch Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep03</td>
      <td>883</td>
      <td>NaN</td>
      <td>Eephus Pitch Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep04</td>
      <td>884</td>
      <td>NaN</td>
      <td>Eephus Pitch Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep05</td>
      <td>885</td>
      <td>NaN</td>
      <td>Eephus Pitch Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep06</td>
      <td>886</td>
      <td>NaN</td>
      <td>Eephus Pitch Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep07</td>
      <td>887</td>
      <td>NaN</td>
      <td>Eephus Pitch Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep08</td>
      <td>888</td>
      <td>NaN</td>
      <td>Eephus Pitch Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep09</td>
      <td>889</td>
      <td>NaN</td>
      <td>Eephus Pitch Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep11</td>
      <td>891</td>
      <td>NaN</td>
      <td>Eephus Pitch Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep12</td>
      <td>892</td>
      <td>NaN</td>
      <td>Eephus Pitch Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep13</td>
      <td>893</td>
      <td>NaN</td>
      <td>Eephus Pitch Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>pep14</td>
      <td>894</td>
      <td>NaN</td>
      <td>Eephus Pitch Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o001</td>
      <td>1001</td>
      <td>NaN</td>
      <td>No Outs Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o002</td>
      <td>1002</td>
      <td>NaN</td>
      <td>No Outs Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o003</td>
      <td>1003</td>
      <td>NaN</td>
      <td>No Outs Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o004</td>
      <td>1004</td>
      <td>NaN</td>
      <td>No Outs Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o005</td>
      <td>1005</td>
      <td>NaN</td>
      <td>No Outs Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o006</td>
      <td>1006</td>
      <td>NaN</td>
      <td>No Outs Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o007</td>
      <td>1007</td>
      <td>NaN</td>
      <td>No Outs Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o008</td>
      <td>1008</td>
      <td>NaN</td>
      <td>No Outs Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o009</td>
      <td>1009</td>
      <td>NaN</td>
      <td>No Outs Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o011</td>
      <td>1011</td>
      <td>NaN</td>
      <td>No Outs Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o012</td>
      <td>1012</td>
      <td>NaN</td>
      <td>No Outs Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o013</td>
      <td>1013</td>
      <td>NaN</td>
      <td>No Outs Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o014</td>
      <td>1014</td>
      <td>NaN</td>
      <td>No Outs Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o101</td>
      <td>1021</td>
      <td>NaN</td>
      <td>One Out Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o102</td>
      <td>1022</td>
      <td>NaN</td>
      <td>One Out Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o103</td>
      <td>1023</td>
      <td>NaN</td>
      <td>One Out Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o104</td>
      <td>1024</td>
      <td>NaN</td>
      <td>One Out Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o105</td>
      <td>1025</td>
      <td>NaN</td>
      <td>One Out Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o106</td>
      <td>1026</td>
      <td>NaN</td>
      <td>One Out Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o107</td>
      <td>1027</td>
      <td>NaN</td>
      <td>One Out Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o108</td>
      <td>1028</td>
      <td>NaN</td>
      <td>One Out Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o109</td>
      <td>1029</td>
      <td>NaN</td>
      <td>One Out Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o111</td>
      <td>1031</td>
      <td>NaN</td>
      <td>One Out Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o112</td>
      <td>1032</td>
      <td>NaN</td>
      <td>One Out Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o113</td>
      <td>1033</td>
      <td>NaN</td>
      <td>One Out Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o114</td>
      <td>1034</td>
      <td>NaN</td>
      <td>One Out Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o201</td>
      <td>1041</td>
      <td>NaN</td>
      <td>Two Outs Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o202</td>
      <td>1042</td>
      <td>NaN</td>
      <td>Two Outs Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o203</td>
      <td>1043</td>
      <td>NaN</td>
      <td>Two Outs Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o204</td>
      <td>1044</td>
      <td>NaN</td>
      <td>Two Outs Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o205</td>
      <td>1045</td>
      <td>NaN</td>
      <td>Two Outs Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o206</td>
      <td>1046</td>
      <td>NaN</td>
      <td>Two Outs Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o207</td>
      <td>1047</td>
      <td>NaN</td>
      <td>Two Outs Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o208</td>
      <td>1048</td>
      <td>NaN</td>
      <td>Two Outs Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o209</td>
      <td>1049</td>
      <td>NaN</td>
      <td>Two Outs Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o211</td>
      <td>1051</td>
      <td>NaN</td>
      <td>Two Outs Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o212</td>
      <td>1052</td>
      <td>NaN</td>
      <td>Two Outs Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o213</td>
      <td>1053</td>
      <td>NaN</td>
      <td>Two Outs Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>o214</td>
      <td>1054</td>
      <td>NaN</td>
      <td>Two Outs Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ac01</td>
      <td>1101</td>
      <td>NaN</td>
      <td>Ahead in Count Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ac02</td>
      <td>1102</td>
      <td>NaN</td>
      <td>Ahead in Count Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ac03</td>
      <td>1103</td>
      <td>NaN</td>
      <td>Ahead in Count Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ac04</td>
      <td>1104</td>
      <td>NaN</td>
      <td>Ahead in Count Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ac05</td>
      <td>1105</td>
      <td>NaN</td>
      <td>Ahead in Count Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ac06</td>
      <td>1106</td>
      <td>NaN</td>
      <td>Ahead in Count Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ac07</td>
      <td>1107</td>
      <td>NaN</td>
      <td>Ahead in Count Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ac08</td>
      <td>1108</td>
      <td>NaN</td>
      <td>Ahead in Count Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ac09</td>
      <td>1109</td>
      <td>NaN</td>
      <td>Ahead in Count Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ac11</td>
      <td>1111</td>
      <td>NaN</td>
      <td>Ahead in Count Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ac12</td>
      <td>1112</td>
      <td>NaN</td>
      <td>Ahead in Count Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ac13</td>
      <td>1113</td>
      <td>NaN</td>
      <td>Ahead in Count Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ac14</td>
      <td>1114</td>
      <td>NaN</td>
      <td>Ahead in Count Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>bc01</td>
      <td>1121</td>
      <td>NaN</td>
      <td>Behind in Count Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>bc02</td>
      <td>1122</td>
      <td>NaN</td>
      <td>Behind in Count Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>bc03</td>
      <td>1123</td>
      <td>NaN</td>
      <td>Behind in Count Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>bc04</td>
      <td>1124</td>
      <td>NaN</td>
      <td>Behind in Count Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>bc05</td>
      <td>1125</td>
      <td>NaN</td>
      <td>Behind in Count Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>bc06</td>
      <td>1126</td>
      <td>NaN</td>
      <td>Behind in Count Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>bc07</td>
      <td>1127</td>
      <td>NaN</td>
      <td>Behind in Count Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>bc08</td>
      <td>1128</td>
      <td>NaN</td>
      <td>Behind in Count Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>bc09</td>
      <td>1129</td>
      <td>NaN</td>
      <td>Behind in Count Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>bc11</td>
      <td>1131</td>
      <td>NaN</td>
      <td>Behind in Count Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>bc12</td>
      <td>1132</td>
      <td>NaN</td>
      <td>Behind in Count Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>bc13</td>
      <td>1133</td>
      <td>NaN</td>
      <td>Behind in Count Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>bc14</td>
      <td>1134</td>
      <td>NaN</td>
      <td>Behind in Count Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ec01</td>
      <td>1141</td>
      <td>NaN</td>
      <td>Even Count Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ec02</td>
      <td>1142</td>
      <td>NaN</td>
      <td>Even Count Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ec03</td>
      <td>1143</td>
      <td>NaN</td>
      <td>Even Count Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ec04</td>
      <td>1144</td>
      <td>NaN</td>
      <td>Even Count Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ec05</td>
      <td>1145</td>
      <td>NaN</td>
      <td>Even Count Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ec06</td>
      <td>1146</td>
      <td>NaN</td>
      <td>Even Count Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ec07</td>
      <td>1147</td>
      <td>NaN</td>
      <td>Even Count Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ec08</td>
      <td>1148</td>
      <td>NaN</td>
      <td>Even Count Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ec09</td>
      <td>1149</td>
      <td>NaN</td>
      <td>Even Count Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ec11</td>
      <td>1151</td>
      <td>NaN</td>
      <td>Even Count Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ec12</td>
      <td>1152</td>
      <td>NaN</td>
      <td>Even Count Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ec13</td>
      <td>1153</td>
      <td>NaN</td>
      <td>Even Count Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ec14</td>
      <td>1154</td>
      <td>NaN</td>
      <td>Even Count Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r001</td>
      <td>1161</td>
      <td>NaN</td>
      <td>Bases Empty Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r002</td>
      <td>1162</td>
      <td>NaN</td>
      <td>Bases Empty Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r003</td>
      <td>1163</td>
      <td>NaN</td>
      <td>Bases Empty Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r004</td>
      <td>1164</td>
      <td>NaN</td>
      <td>Bases Empty Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r005</td>
      <td>1165</td>
      <td>NaN</td>
      <td>Bases Empty Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r006</td>
      <td>1166</td>
      <td>NaN</td>
      <td>Bases Empty Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r007</td>
      <td>1167</td>
      <td>NaN</td>
      <td>Bases Empty Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r008</td>
      <td>1168</td>
      <td>NaN</td>
      <td>Bases Empty Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r009</td>
      <td>1169</td>
      <td>NaN</td>
      <td>Bases Empty Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r011</td>
      <td>1171</td>
      <td>NaN</td>
      <td>Bases Empty Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r012</td>
      <td>1172</td>
      <td>NaN</td>
      <td>Bases Empty Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r013</td>
      <td>1173</td>
      <td>NaN</td>
      <td>Bases Empty Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>r014</td>
      <td>1174</td>
      <td>NaN</td>
      <td>Bases Empty Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rbl01</td>
      <td>1181</td>
      <td>NaN</td>
      <td>Bases Loaded Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rbl02</td>
      <td>1182</td>
      <td>NaN</td>
      <td>Bases Loaded Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rbl03</td>
      <td>1183</td>
      <td>NaN</td>
      <td>Bases Loaded Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rbl04</td>
      <td>1184</td>
      <td>NaN</td>
      <td>Bases Loaded Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rbl05</td>
      <td>1185</td>
      <td>NaN</td>
      <td>Bases Loaded Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rbl06</td>
      <td>1186</td>
      <td>NaN</td>
      <td>Bases Loaded Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rbl07</td>
      <td>1187</td>
      <td>NaN</td>
      <td>Bases Loaded Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rbl08</td>
      <td>1188</td>
      <td>NaN</td>
      <td>Bases Loaded Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rbl09</td>
      <td>1189</td>
      <td>NaN</td>
      <td>Bases Loaded Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rbl11</td>
      <td>1191</td>
      <td>NaN</td>
      <td>Bases Loaded Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rbl12</td>
      <td>1192</td>
      <td>NaN</td>
      <td>Bases Loaded Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rbl13</td>
      <td>1193</td>
      <td>NaN</td>
      <td>Bases Loaded Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rbl14</td>
      <td>1194</td>
      <td>NaN</td>
      <td>Bases Loaded Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ron01</td>
      <td>1201</td>
      <td>NaN</td>
      <td>Runners On Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ron02</td>
      <td>1202</td>
      <td>NaN</td>
      <td>Runners On Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ron03</td>
      <td>1203</td>
      <td>NaN</td>
      <td>Runners On Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ron04</td>
      <td>1204</td>
      <td>NaN</td>
      <td>Runners On Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ron05</td>
      <td>1205</td>
      <td>NaN</td>
      <td>Runners On Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ron06</td>
      <td>1206</td>
      <td>NaN</td>
      <td>Runners On Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ron07</td>
      <td>1207</td>
      <td>NaN</td>
      <td>Runners On Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ron08</td>
      <td>1208</td>
      <td>NaN</td>
      <td>Runners On Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ron09</td>
      <td>1209</td>
      <td>NaN</td>
      <td>Runners On Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ron11</td>
      <td>1211</td>
      <td>NaN</td>
      <td>Runners On Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ron12</td>
      <td>1212</td>
      <td>NaN</td>
      <td>Runners On Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ron13</td>
      <td>1213</td>
      <td>NaN</td>
      <td>Runners On Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>ron14</td>
      <td>1214</td>
      <td>NaN</td>
      <td>Runners On Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rsp01</td>
      <td>1221</td>
      <td>NaN</td>
      <td>Scoring Position Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rsp02</td>
      <td>1222</td>
      <td>NaN</td>
      <td>Scoring Position Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rsp03</td>
      <td>1223</td>
      <td>NaN</td>
      <td>Scoring Position Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rsp04</td>
      <td>1224</td>
      <td>NaN</td>
      <td>Scoring Position Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rsp05</td>
      <td>1225</td>
      <td>NaN</td>
      <td>Scoring Position Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rsp06</td>
      <td>1226</td>
      <td>NaN</td>
      <td>Scoring Position Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rsp07</td>
      <td>1227</td>
      <td>NaN</td>
      <td>Scoring Position Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rsp08</td>
      <td>1228</td>
      <td>NaN</td>
      <td>Scoring Position Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rsp09</td>
      <td>1229</td>
      <td>NaN</td>
      <td>Scoring Position Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rsp11</td>
      <td>1231</td>
      <td>NaN</td>
      <td>Scoring Position Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rsp12</td>
      <td>1232</td>
      <td>NaN</td>
      <td>Scoring Position Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rsp13</td>
      <td>1233</td>
      <td>NaN</td>
      <td>Scoring Position Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>rsp14</td>
      <td>1234</td>
      <td>NaN</td>
      <td>Scoring Position Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl01</td>
      <td>1241</td>
      <td>NaN</td>
      <td>vs Left Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl02</td>
      <td>1242</td>
      <td>NaN</td>
      <td>vs Left Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl03</td>
      <td>1243</td>
      <td>NaN</td>
      <td>vs Left Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl04</td>
      <td>1244</td>
      <td>NaN</td>
      <td>vs Left Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl05</td>
      <td>1245</td>
      <td>NaN</td>
      <td>vs Left Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl06</td>
      <td>1246</td>
      <td>NaN</td>
      <td>vs Left Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl07</td>
      <td>1247</td>
      <td>NaN</td>
      <td>vs Left Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl08</td>
      <td>1248</td>
      <td>NaN</td>
      <td>vs Left Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl09</td>
      <td>1249</td>
      <td>NaN</td>
      <td>vs Left Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl11</td>
      <td>1251</td>
      <td>NaN</td>
      <td>vs Left Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl12</td>
      <td>1252</td>
      <td>NaN</td>
      <td>vs Left Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl13</td>
      <td>1253</td>
      <td>NaN</td>
      <td>vs Left Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vl14</td>
      <td>1254</td>
      <td>NaN</td>
      <td>vs Left Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vr01</td>
      <td>1261</td>
      <td>NaN</td>
      <td>vs Right Zone 1</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vr02</td>
      <td>1262</td>
      <td>NaN</td>
      <td>vs Right Zone 2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vr03</td>
      <td>1263</td>
      <td>NaN</td>
      <td>vs Right Zone 3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vr04</td>
      <td>1264</td>
      <td>NaN</td>
      <td>vs Right Zone 4</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vr05</td>
      <td>1265</td>
      <td>NaN</td>
      <td>vs Right Zone 5</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vr06</td>
      <td>1266</td>
      <td>NaN</td>
      <td>vs Right Zone 6</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vr07</td>
      <td>1267</td>
      <td>NaN</td>
      <td>vs Right Zone 7</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vr08</td>
      <td>1268</td>
      <td>NaN</td>
      <td>vs Right Zone 8</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vr09</td>
      <td>1269</td>
      <td>NaN</td>
      <td>vs Right Zone 9</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vr11</td>
      <td>1271</td>
      <td>NaN</td>
      <td>vs Right Zone 11</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vr12</td>
      <td>1272</td>
      <td>NaN</td>
      <td>vs Right Zone 12</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vr13</td>
      <td>1273</td>
      <td>NaN</td>
      <td>vs Right Zone 13</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>vr14</td>
      <td>1274</td>
      <td>NaN</td>
      <td>vs Right Zone 14</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>

### Play Event Types

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ACTION</td>
    </tr>
    <tr>
      <td>PITCH</td>
    </tr>
    <tr>
      <td>PICKOFF</td>
    </tr>
    <tr>
      <td>NO_PITCH</td>
    </tr>
    <tr>
      <td>STEPOFF</td>
    </tr>
  </tbody>
</table>