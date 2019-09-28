<?php

include('MyDB.php');
error_reporting(E_ERROR);
ini_set("memory_limit", -1);
$db = new MyDB();

$query = '﻿CREATE TABLE Match_Player_Attributes (`match_id`	INTEGER PRIMARY KEY,';
for ($i = 1; $i < 23; $i++) {
    $sub = $i < 12 ? 'home' : 'away';
    $p = $i < 12 ? $i : ($i - 11);
    $query .= '`overall_rating_' . $p . '_' . $sub . '`	INTEGER,
	`potential_' . $p . '_' . $sub . '`	INTEGER,
	`attacking_work_rate_' . $p . '_' . $sub . '`	TEXT,
	`defensive_work_rate_' . $p . '_' . $sub . '`	TEXT,
	`crossing_' . $p . '_' . $sub . '`	INTEGER,
	`finishing_' . $p . '_' . $sub . '`	INTEGER,
	`heading_accuracy_' . $p . '_' . $sub . '`	INTEGER,
	`short_passing_' . $p . '_' . $sub . '`	INTEGER,
	`volleys_' . $p . '_' . $sub . '`	INTEGER,
	`dribbling_' . $p . '_' . $sub . '`	INTEGER,
	`curve_' . $p . '_' . $sub . '`	INTEGER,
	`free_kick_accuracy_' . $p . '_' . $sub . '`	INTEGER,
	`long_passing_' . $p . '_' . $sub . '`	INTEGER,
	`ball_control_' . $p . '_' . $sub . '`	INTEGER,
	`acceleration_' . $p . '_' . $sub . '`	INTEGER,
	`sprint_speed_' . $p . '_' . $sub . '`	INTEGER,
	`agility_' . $p . '_' . $sub . '`	INTEGER,
	`reactions_' . $p . '_' . $sub . '`	INTEGER,
	`balance_' . $p . '_' . $sub . '`	INTEGER,
	`shot_power_' . $p . '_' . $sub . '`	INTEGER,
	`jumping_' . $p . '_' . $sub . '`	INTEGER,
	`stamina_' . $p . '_' . $sub . '`	INTEGER,
	`strength_' . $p . '_' . $sub . '`	INTEGER,
	`long_shots_' . $p . '_' . $sub . '`	INTEGER,
	`aggression_' . $p . '_' . $sub . '`	INTEGER,
	`interceptions_' . $p . '_' . $sub . '`	INTEGER,
	`positioning_' . $p . '_' . $sub . '`	INTEGER,
	`vision_' . $p . '_' . $sub . '`	INTEGER,
	`penalties_' . $p . '_' . $sub . '`	INTEGER,
	`marking_' . $p . '_' . $sub . '`	INTEGER,
	`standing_tackle_' . $p . '_' . $sub . '`	INTEGER,
	`sliding_tackle_' . $p . '_' . $sub . '`	INTEGER,
	`gk_diving_' . $p . '_' . $sub . '`	INTEGER,
	`gk_handling_' . $p . '_' . $sub . '`	INTEGER,
	`gk_kicking_' . $p . '_' . $sub . '`	INTEGER,
	`gk_positioning_' . $p . '_' . $sub . '`	INTEGER,
	`gk_reflexes_' . $p . '_' . $sub . '`	INTEGER,';
}
$query = substr($query, 0, strlen($query) - 1);
$query .= ')';

//Add new table to DB
if ($db->exec(trim($query)) == false) {
    echo $query . "-->" . $db->lastErrorMsg() . PHP_EOL;
}

$results = $db->query("SELECT Match.id as MatchId,* FROM Match JOIN League ON Match.league_id=League.id JOIN Country ON League.country_id=Country.id WHERE Country.name='Italy' AND Match.date>='2008'");
while ($row = $results->fetchArray()) {
    for ($i = 1; $i < 23; $i++) {
        $sub = $i < 12 ? 'home_' : 'away_';
        $p = $i < 12 ? $i : ($i - 11);
        $player_match = $row[$sub . 'player_' . $p];
        if (!is_null($player_match)) {
            if (is_null($playersAttributes[$player_match])) {
                $player = $db->query("SELECT * FROM Player_Attributes");

                while ($playerAttributes = $player->fetchArray()) {
                    $playersAttributes[$playerAttributes['player_api_id']][$playerAttributes['id']] = $playerAttributes;
                }
            }
            $distances = array();
            foreach ($playersAttributes[$player_match] as $key => $playerAttributes) {
                $distance['val'] = abs(strtotime($row['date']) - strtotime($playerAttributes['date']));
                $distance['id'] = $playerAttributes['id'];
                array_push($distances, $distance);
            }
            sort($distances);
            $player = $db->query("SELECT * FROM Player_Attributes WHERE id=" . $distances[0]['id'] . "");
            $playerAttributes = $player->fetchArray();

            if ($playerAttributes != false) {
                writePlayerAttributes($p, substr($sub, 0, -1), $playerAttributes, $row['MatchId'], $db);
            }
        }
    }
}

function writePlayerAttributes($index, $home_away, $playerAttributes, $match_id, $db) {

    $player = $db->query("SELECT * FROM Match_Player_Attributes WHERE match_id=" . $match_id . "");
    if ($player == false) {
        echo $query . "-->" . $db->lastErrorMsg() . PHP_EOL;
    }
    $playerAttributesCheck = $player->fetchArray();

    if ($playerAttributesCheck == false) {
        $query = "INSERT INTO Match_Player_Attributes (match_id) VALUES(" . $match_id . ")";
        file_put_contents("sql.update", $query . ";" . PHP_EOL, FILE_APPEND);

        if ($db->exec($query) == false) {
            echo $query . "-->" . $db->lastErrorMsg() . PHP_EOL;
        }
    }
    foreach ($playerAttributes as $key => $value) {
        if (is_int($key)) {
            unset($playerAttributes[$key]);
        }
    }
    unset($playerAttributes['id'], $playerAttributes['date'], $playerAttributes['player_fifa_api_id'], $playerAttributes['player_api_id'], $playerAttributes['preferred_foot']);
    foreach ($playerAttributes as $key => $value) {
        $content[$key . "_" . $index . "_" . $home_away] = $value;
    }
    $query = creat_update('Match_Player_Attributes', array('match_id' => $match_id), $content);
    echo $match_id . PHP_EOL . randomThien(rand(0, 4)) . PHP_EOL;
    file_put_contents("sql.update", $query . ";" . PHP_EOL, FILE_APPEND);
    if ($db->exec($query) == false) {
        echo $query . "-->" . $db->lastErrorMsg() . PHP_EOL;
    }
}

function creat_update($table_name, $table_index, $content, $limit = 1) {
    $query = "UPDATE " . $table_name . " SET ";
    $i = 1;
    foreach ($content as $key => $value) {
        if (strlen($value) > 0) {
            $query .= $key . "='" . mysql_escape_string(trim($value)) . "'";
        } else {
            $query .= $key . "=NULL";
        }
        count($content) > $i ? $query .= ',' : '';
        $i++;
    }
    $i = 1;
    $query .= " WHERE ";
    foreach ($table_index as $key => $value) {
        if ($value == NULL) {
            $query .= $key . " IS NULL";
        } else {
            $query .= $key . "='" . mysql_escape_string($value) . "'";
        }
        count($table_index) > $i ? $query .= ' AND ' : '';
        $i++;
    }
    return $query;
}

function randomThien($index) {
    switch ($index) {
        case 0: return 'Is this wine?';
            break;
        case 1: return 'Can I drink it?';
            break;
        case 2: return 'Is this a Mercedes?';
            break;
        case 3: return 'Rum first, peach after!';
            break;
        case 4: return 'It\'s 4am! Wake up go go!!';
            break;
    }
}
