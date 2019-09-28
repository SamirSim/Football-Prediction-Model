<?php

/**
 * Description of BD
 *  
 * @author emanud
 */
class MyDB extends SQLite3 {

    function __construct() {
        $this->open('../Data/database.sqlite');
    }

}
