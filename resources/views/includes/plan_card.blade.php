<div class="col-lg-3 col-md-6 col-sm-6 flex-item-plan">
    <div class="card card-stats">
        <div class="card-header {{ $color }} card-header-icon" data-header-animation="true">
            <div class="card-icon">
                <h2>{{ $name }} </h2>
            </div>
        </div>
        <div class="card-body card-body-plan">
            <div class="card-actions-plan ">
                <button type="button" class="btn btn-danger btn-link fix-broken-card" rel="tooltip" data-placement="bottom" title="Fix Header">
                    <i class="material-icons">build</i>
                </button>
                <button id="launch" type="button" class="btn btn-info btn-link btn-plan" rel="tooltip" data-placement="bottom" title="Launch Service">
                    <i class="material-icons">launch</i>
                </button>
                <button id="edit" type="button" class="btn btn-default btn-link btn-plan" rel="tooltip" data-placement="bottom" title="Edit Plan">
                    <i class="material-icons">edit</i>
                </button>
            </div>
<!--            <h3 class="card-title card-title-plan">{{ $name }} <br> Service </h3>-->
            <h3 class="card-title card-title-plan"> {!! nl2br($description) !!} </h3>
        </div>
        <div class="card-footer">
            <div class="stats">
                <i class="material-icons">access_time</i> plan created 2 days ago
            </div>
        </div>
    </div>
</div>
