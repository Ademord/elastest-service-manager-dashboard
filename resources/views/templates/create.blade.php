<!-- Modal -->
<div class="modal fade" id="createManifestModal" role="dialog">
    <div class="modal-dialog modal-lg">
        <!-- Modal content-->
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">&times;</button>
                <h2>Deploy Service</h2>
            </div>
            <div class="modal-body">
                    <div id="accordion">
                        <div class="card">
                            <div class="card-header card-header-deploy" data-background-color="orange" id="headingOne">
                                <h4 class="title mb-0">
                                    <button class="btn btn-lg btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                        Service Details
                                    </button>
                                </h4>
                            </div>

                            <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
                                <div class="card-body">
                                        Wordpress Service
                                    <br>
                                    Service to deploy a Wordpress application.
                                </div>
                            </div>
                        </div>
                        <div class="card">
                            <div class="card-header" id="headingTwo">
                                <h4 class="mb-0">
                                    <button class="btn btn-lg btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                                        Plan Details
                                    </button>
                                </h4>
                            </div>
                            <div id="collapseTwo" class="collapse show" aria-labelledby="headingTwo" data-parent="#accordion">
                                <div class="card-body">
                                    <p>
                                        Windows 10 <br>
                                        2 GB RAM <br>
                                        2 CPU <br>
                                        16 GB SSD Storage
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div class="card">
                            <div class="card-header" id="headingThree">
                                <h4 class="mb-0">
                                    <button class="btn btn-lg btn-link collapsed" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                                        Template Details
                                    </button>
                                </h4>
                            </div>
                            <div id="collapseThree" class="collapse show" aria-labelledby="headingThree" data-parent="#accordion">
                                <div class="card-body">
                                    Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
                                    <div class="dropdown">
                                        <button class="btn btn-sm btn-secondary btn-block dropdown-toggle template-input-background" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                            Select Backend
                                        </button>
                                        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                            <a class="dropdown-item" href="#">Docker</a>
                                            <a class="dropdown-item" href="#">Kubernetes</a>
                                            <a class="dropdown-item" href="#">Openshift</a>
                                        </div>
                                    </div>
                                    <textarea class="form-control template-input " placeholder="Insert Template File here..." rows="10" id="comment"></textarea>

                                </div>
                            </div>
                        </div>
                    </div>

                <form role="form">


<!--                    <button type="submit" class="btn btn-danger btn-default pull-left" data-dismiss="modal"><span class="glyphicon glyphicon-remove"></span> Cancel</button>-->
<!--                    <button type="submit" class="btn btn-success pull-right"><span class="glyphicon glyphicon-off"></span> Launch</button>-->
                </form>
            </div>

        </div>
    </div>
</div>
<!--<p class="card-category">Last Campaign Performance</p>-->
<!--<button class="btn btn-default">Default</button>-->
<!--<button class="btn btn-info">Info</button>-->
<!--<button class="btn btn-success">Success</button>-->
<!--<button class="btn btn-warning">Warning</button>-->
<!--<button class="btn btn-danger">Danger</button>-->
