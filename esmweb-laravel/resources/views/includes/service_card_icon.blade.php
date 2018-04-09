<div class="col-lg-3 col-md-6 col-sm-6 flex-item">
    <div class="card card-stats">
        <div class="card-header card-header-warning card-header-icon" data-header-animation="true">
            <div class="card-icon">
                <i class="material-icons">{{ $icon }}</i>
            </div>
        </div>
        <div class="card-body card-body-plan">
            <div class="card-actions-service ">
                <button type="button" class="btn btn-danger btn-link fix-broken-card" rel="tooltip" data-placement="bottom" title="Fix Header">
                    <i class="material-icons">build</i>
                </button>
                <a class="nav-link" href="/catalog/1">
                    <button type="button" class="btn btn-info btn-link" rel="tooltip" data-placement="bottom" title="Inspect Service">
                        <i class="material-icons">search</i>
                    </button>
                </a>
            </div>
            <h3 class="card-title card-title-plan">{{ $name }} <br> Service </h3>
        </div>
        <br>
    </div>
</div>
