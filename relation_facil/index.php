<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.2.3/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

    <div class="container">
        <div class="row mt-3">
            <h3>Fill in data</h3>
        </div>
        <div class="row">

                <div class="container">
                    <div class="row">
                        <form onsubmit="event.preventDefault(); find_relationship(this);" id="form" method="get">
                            <div class="container">
                                <div class="row">

                                    <!-- add next row here -->

                                    <!-- COL 1 -->
                                    <div class="col-12 col-lg-2">
                                        <div class="row mt-2">
                                            <div class="col-12 mt-2">
                                                <p>Symbol</p>
                                            </div>
                                            <div class="col-12 mt-2">
                                                <input type="text"
                                                    name="symbol_one"
                                                    class="form-control"
                                                    value="1"
                                                    onkeyup="when_key_up()"
                                                    placeholder='symbol for "one"'>                    
                                            </div>
                                            <div class="col-12 mt-2">
                                                <input type="text"
                                                    name="symbol_many" 
                                                    class="form-control"
                                                    value="many"
                                                    onkeyup="when_key_up()"
                                                    placeholder='symbol for "many"'> 
                                            </div>
                                        </div>
                                    </div>

                                      <!-- COL 2 -->
                                    <div class="col-12 col-lg-2">
                                        <div class="row mt-2">
                                            <div class="col-12 mt-2">
                                                <p>Entity</p>
                                            </div>
                                            <!-- entity A name singular -->
                                            <div class="col-12 mt-2">
                                                <input type="text"
                                                    name="entityA_sing"
                                                    id="entityA_sing"
                                                    class="form-control"
                                                    onkeyup="when_key_up()"
                                                    placeholder="singular">
                                            </div>
                                            <!-- entity A name plural -->
                                            <div class="col-12 mt-2">
                                                <input type="text"
                                                    name="entityA_plur" 
                                                    id="entityA_plur"
                                                    class="form-control"
                                                    onkeyup="when_key_up()"
                                                    placeholder="plural"> 
                                            </div>
                                            <!-- checkbox same -->
                                            <div class="col-12 mt-2">
                                                <div class="form-check">
                                                    <input class="form-check-input"
                                                            type="checkbox"
                                                            onchange="toggle_input('entityA_plur', 'entityA_sing'); when_key_up();">
                                                    <label class="form-check-label">same</label>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- COL 3 -->
                                    <div class="col-12 col-lg-2">
                                        <!-- occupies all row -->
                                        <div class="row mt-2">
                                            <div class="col-12 mt-2">
                                                <p>Relation</p>
                                            </div>
                                            <!-- entity A action singular -->
                                            <div class="col-12 mt-2">
                                                <input type="text"
                                                    name="entityA_action_sing"
                                                    id="entityA_action_sing"
                                                    class="form-control"
                                                    onkeyup="when_key_up()"
                                                    placeholder="singular">
                                            </div>
                                        </div>

                                    </div>

                                    <!-- COL 4 -->
                                    <div class="col-12 col-lg-2">
                                        <div class="row mt-2">
                                            <div class="col-12 mt-2">
                                                <p>Entity</p>
                                            </div>
                                            <!-- entity A name singular -->
                                            <div class="col-12 mt-2">
                                                <input type="text"
                                                    name="entityB_sing"
                                                    id="entityB_sing"
                                                    class="form-control"
                                                    onkeyup="when_key_up()"
                                                    placeholder="singular">
                                            </div>
                                            <!-- entity A name plural -->
                                            <div class="col-12 mt-2">
                                                <input type="text"
                                                    name="entityB_plur" 
                                                    id="entityB_plur"
                                                    class="form-control"
                                                    onkeyup="when_key_up()"
                                                    placeholder="plural"> 
                                            </div>
                                            <!-- checkbox same -->
                                            <div class="col-12 mt-2">
                                                <div class="form-check">
                                                    <input class="form-check-input"
                                                            type="checkbox"
                                                            onchange="toggle_input('entityB_plur', 'entityB_sing'); when_key_up()">
                                                    <label class="form-check-label">same</label>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- COL 5 -->
                                    <div class="col-12 col-lg-2">
                                        <!-- occupies all row -->
                                        <div class="row mt-2">
                                            <div class="col-12 mt-2">
                                                <p>Relation</p>
                                            </div>
                                            <!-- entity A action singular -->
                                            <div class="col-12 mt-2">
                                                <input type="text"
                                                    name="entityB_action_sing"
                                                    id="entityB_action_sing"
                                                    class="form-control"
                                                    onkeyup="when_key_up()"
                                                    placeholder="singular">
                                            </div>
                                        </div>
                                    </div>

                                    <!-- add next row here -->

                                </div>

                                <!-- button row -->
                                <!-- <div class="row mt-2">
                                    <div class="col w-100">
                                        <button type="submit" 
                                                class="btn btn-primary">compute</button>
                                    </div>
                                </div> -->

                            </div>
                        </form>
                    </div>
                </div>


               

        </div>
        <div class="row mt-3">
            <h3>Choose relationships</h3>
            <div class="row">
                <ul id="list_relationships">
                    
                </ul>
            </div>
        </div>
        <div class="row">
            <h3>Results</h3>
        </div>
        <div class="row">

        </div>
    </div>



<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.2.3/js/bootstrap.bundle.min.js"></script>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="/project/assets/js/Entity.class.js"></script>

<script>

    var entity_manager = new EntityManager();

    /**
     * 
     */
    function toggle_input(input_id_toggle, input_id_truth) {
        // hide/show the input to toggle
        $("#"+input_id_toggle).toggle();
        // fill the input to toggle with the value 
        // from the source input
        // for example, if you want to toggle the 
        // plural fields, you now make the plural 
        // field the same as the singular field
        $("#"+input_id_toggle).val($("#"+input_id_truth).val());

    }

    /**
     * Show phrases in the UI
     */
    function show_phrases(phrases) {

        function make_checkbox(rel) {
            let is_checked = false;
            if (rel == "1A->1B" || rel == "1B->1A") {
                is_checked = true;
                entity_manager.compute_rels(rel);
            }
            return `
                <input type="checkbox" value="${rel}" ${is_checked ? 'checked' : ''} onchange='show_result(this)'>
            `;
        }

        var items = phrases.map(function(phrase) {
            return `
                <li>${phrase.phrase} ${make_checkbox(phrase.rel)}</li>
            `;
        }).join("");

        $("#list_relationships").html(items);

        
    }


    function show_result(html_checkbox) {
        // current relationship
        let curr_rel = $(html_checkbox).val()
        let res = entity_manager.compute_rels(curr_rel);
         
    }

    function compute_relationship(html_checkbox) {
        console.log(html_checkbox);
    }



    function when_key_up() {
        find_relationship(document.getElementById("form"));
    }

    function find_relationship(html_form) {
        var $form = $(html_form);
        const formData = new FormData(html_form);
        // let areFieldsFilled = formData.has("commerciale") && formData.has("mese");
        
        // check if the user has not provided
        // a commerciale
        // if (!areFieldsFilled) {
        //     alert("Inserisci tutti i campi");
        //     return;
        // }

        // make an object with key value pairs
        // like the form
        var form = {};
        formData.forEach((value, key) => {
            form[key] = value;
        });
        
        var symbols = {
            "one": form["symbol_one"],
            "many": form["symbol_many"]
        };

        var entityA_name = [
            form["entityA_sing"],
            form["entityA_plur"]
        ];

        var entityB_name = [
            form["entityB_sing"],
            form["entityB_plur"]
        ];

        var entityA_action = [
            form["entityA_action_sing"],
            // not using the plural of action
            form["entityA_action_plur"]
        ];

        var entityB_action = [
            form["entityB_action_sing"],
            // not using the plural of action
            form["entityB_action_plur"]
        ];

        entity_manager.empty();

        entity_manager.set_symbols(symbols);

        var entityA = entity_manager.new_entity(entityA_name, entityA_action);
        var entityB = entity_manager.new_entity(entityB_name, entityB_action);

        var phrases = entity_manager.generate_phrases();

        show_phrases(phrases);

    }



</script>

</body>
</html>
