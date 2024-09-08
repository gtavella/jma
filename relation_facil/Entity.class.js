


class Entity {

    constructor(entity, action, symbols) {
    
        this.sing = entity[0];
        this.plur = entity[1];
        
        if (Array.isArray(action)) {
            this.action_sing = action[0];
            this.action_plur = action[1];
        }
        else {
            this.action_sing = action;
            this.action_plur = action;
        }
        this.symbols = symbols;
    }

}




class EntityManager {

    constructor() {
        this.entities = [];
        this.rels = [];
    }

    set_symbols(symb) {
        this.symbols = symb;
    }

    new_entity(name, action) {
        let ent = new Entity(name, action, this.symbols);
        this.entities.push(ent);
        return ent;
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
    _generate_matrix(entityA, entityB) {

        var row1 = [
            entityA.symbols["one"],
            entityA.sing,
            entityA.action_sing,
            entityB.symbols["one"],
            entityB.sing,
            1,
            "1A->1B"
        ];

        var row2 = [
            entityA.symbols["one"],
            entityA.sing,
            entityA.action_sing,
            entityB.symbols["many"],
            entityB.plur,
            2,
            "1A->NB"
        ];

        var row3 = [
            entityB.symbols["one"],
            entityB.sing,
            entityB.action_sing,
            entityA.symbols["one"],
            entityA.sing,
            3,
            "1B->1A"
        ];

        var row4 = [
            entityB.symbols["one"],
            entityB.sing,
            entityB.action_sing,
            entityA.symbols["many"],
            entityA.plur,
            4,
            "1B->NA"
        ];

        var ret =  [row1, row2, row3, row4];

        return ret;

    }

    generate_phrases() {
        let [entA, entB] = this.entities;
        let matrix = this._generate_matrix(entA, entB);
        let ret = [];

        matrix.forEach((row) => {
            // exlude last 2 columns
            let el = {
                "phrase": row.slice(0, -2).join(" ").trim(),
                "id": row.at(-2),
                "rel": row.at(-1)
            };
            ret.push(el);
        });
        
        return ret;
    }

    // empty the entities list
    empty() {
        this.entities = [];
    }

    _get_entities(full_rel) {
        return full_rel.split("->");
    }

    _switch_L(L) {
        return L == "A" ? "B" : "A";
    }

    // Q can be assumed to mean quantity
    _switch_Q(Q) {
        return Q == "1" ? "N": "1"; 
    }

    /**
     * example 1
     * in:
     * 1A->1B
     * out:
     * 1B->1A
     * 
     * example 2:
     * in:
     * 1A->NB
     * out:
     * 1B->NA
     * 
     */
    _get_complement(full_rel) {
        let [ent1, ent2] = this._get_entities(full_rel);
        let [Q1, L1] = ent1;
        let [Q2, L2] = ent2;
        // letters are different 
        if (L1 !== L2) {
            // switch letters only now
            L1 = this._switch_L(L1);
            L2 = this._switch_L(L2);
            if (Q1 == Q2) {
                // Q1 and Q2 are equal to 1, so no switch
                if (Q1 == "1") {
                    return `1${L1}->1${L2}`;
                } 
                else {
                    throw new Error("relation of the form NX->NX not supported for now");
                }
            } 
            // Q are different, which means either 1 and N, or N and 1,
            // so switch
            else {
                Q1 = this._switch_Q(Q2);
                Q2 = this._switch_Q(Q1);
                return `${Q1}${L1}->${Q2}${L2}`;
            }
        } 
        else {
            throw new Error("relation of the form X->X not supported for now");
        }

    }

    // when I have 1A->1B and then I have
    // 1A -> NB, then this last one wins
    _upgrade() {
        // CONTINUE HERE
    }

    // compute the relationship between the two entities
    compute_rels(curr_rel) {

        console.log(this._get_complement(curr_rel));

        // only do something if this relation is
        // not already present
        // if (!this.rels.includes(curr_rel)) {

        //     this.rels.push(curr_rel);
        // }
    }

}

