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
        <!-- Results content here -->
    </div>
</div>
