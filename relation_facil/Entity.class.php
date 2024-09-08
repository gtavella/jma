<?php

class Entity
    {
        static $symbols = [];

        function __construct(array $entity, array|string $action)
        {

            $this->sing = $entity[0];
            $this->plur = $entity[1];

            if (is_array($action)) {
                $this->action_sing = $action[0];
                $this->action_plur = $action[1];
            } 
            else {
                $this->action_sing = $action;
                $this->action_plur = $action;
            }
        
        }

        static function set_symbols(array $symbols): void
        {
            self::$symbols = $symbols;
        }

        /**
         * @example
         * 1 book can be published by 1 publisher
         * 1 book can be published by many publishers
         * 1 publisher can publish 1 book
         * 1 publisher can publish many books
         * 
         * formally:
         *  symbol1   entity1    action  symbol2   entity2    
         *  ------------------------------------------------   
         *  |  1      |  A   |      A   |   1     |   B    |   1A-1B
         *  |  1      |  A   |      A   |  many   |   B    |   1A-manyB
         *  |  1      |  B   |      B   |   1     |   A    |   1B-1A 
         *  |  1      |  B   |      B   |  many   |   A    |   1B-manyA
         * 
         */
        private static function generate_matrix(Entity $entityA, Entity $entityB): array 
        {

            $row1 = [
                self::$symbols["one"],
                $entityA->sing,
                $entityA->action_sing,
                self::$symbols["one"],
                $entityB->sing,
                1,
                "1A-1B"
            ];

            $row2 = [
                self::$symbols["one"],
                $entityA->sing,
                $entityA->action_sing,
                self::$symbols["many"],
                $entityB->plur,
                2,
                "1A-manyB"
            ];

            $row3 = [
                self::$symbols["one"],
                $entityB->sing,
                $entityB->action_sing,
                self::$symbols["one"],
                $entityA->sing,
                3,
                "1B-1A"
            ];

            $row4 = [
                self::$symbols["one"],
                $entityB->sing,
                $entityB->action_sing,
                self::$symbols["many"],
                $entityA->plur,
                4,
                "1B-manyA"
            ];

            $ret =  [$row1, $row2, $row3, $row4];

            return $ret;
        }

        static function generate_phrases(Entity $entityA, Entity $entityB): array 
        {
            $matrix = self::generate_matrix($entityA, $entityB);
            $ret = [];

            foreach($matrix as $row) {
                // exlude last 2 columns
                $phrase = implode(" ", array_slice($row, 0, -2));
                $ret[] = trim($phrase);
            } 
            return $ret;
        }    

    }



// USAGE
// Entity::set_symbols([
//     "one" => "1",
//     "many" => "many"
// ]);

// $entityA = new Entity(["book", "books"], "can be published by");
// $entityB = new Entity(["publisher", "publishers"], "can publish");

// $phrases = Entity::generate_phrases($entityA, $entityB);
