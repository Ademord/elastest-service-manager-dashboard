@extends('layouts.default')
@section('content')
<h2>Wordpress Service</h2>
<div id="modal-background"></div>

<div class="row">
    <div class="col-lg-8 col-md-12 col-sm-12">
        <div class="card">
            <div class="card-header card-header-text card-header-warning">
                <div class="card-text">
                    <h4 class="card-title">Service Preview</h4>
                </div>
            </div>

            <div class="card-body">
                <img class="img-fluid" src="/assets/img/wordpress-dashboard.png" alt="Wordpress Interface Preview">
            </div>
        </div>
    </div>
    <div class="col-lg-4 col-md-12 col-sm-12">
        <div class="card">
            <div class="card-header card-header-text card-header-rose">
                <div class="card-text">
                    <h4 class="card-title">Example Variables</h4>
                </div>
            </div>
            <div class="card-body table-responsive">
                <table class="table table-hover">
                    <thead class="text-rose">
                        <th>Variable</th>
                        <th>Value</th>
                    </tr></thead>
                    <tbody>
                    <tr>
                        <td>Endpoint:</td>
                        <td>http://192.168.0.1/wp-login</td>
                    </tr>
                    <tr>
                        <td>Username:</td>
                        <td>admin</td>
                    </tr>
                    <tr>
                        <td>Password:</td>
                        <td>admin</td>
                    </tr>

                    </tbody>
                </table>
            </div>
        </div>
    </div>

</div>
<div class="row">

    @include('includes.plan_card', ['name' => 'Tiny', 'description' => '2 Cores <br> 2 GB RAM', 'color' => 'card-header-success'])
    @include('includes.plan_card', ['name' => 'Small', 'description' => '4 Cores <br> 4 GB RAM', 'color' => 'card-header-info'])
    @include('includes.plan_card', ['name' => 'Medium', 'description' => '8 Cores <br> 8 GB RAM', 'color' => 'card-header-warning'])
    @include('includes.plan_card', ['name' => 'Big', 'description' => '16 Cores <br> 16 GB RAM', 'color' => 'card-header-rose'])

</div>



@include('templates.create')

@stop

<!--<div class="card-body ">-->
<!--    <div class="row">-->
<!--        <div class="col-md-6">-->
<!--            <div class="table-responsive">-->
<!--                <table class="table">-->
<!--                    <tbody>-->
<!--                    <tr>-->
<!--                        <td>-->
<!--                            <div class="flag">-->
<!--                                <i class="material-icons">dashboard</i>-->
<!--                            </div>-->
<!--                        </td>-->
<!--                        <td>Wordpress Service</td>-->
<!--                        <td class="text-right"> Small</td>-->
<!--                        <td class="text-right"> 2 Cores</td>-->
<!--                        <td class="text-right action">-->
<!--                            <a class="nav-link" href="/catalog/1">-->
<!--                                <button type="button" class="btn btn-default btn-link" rel="tooltip" data-placement="bottom" title="Modify Service">-->
<!--                                    <i class="material-icons">edit</i>-->
<!--                                </button>-->
<!--                            </a>-->
<!--                        </td>-->
<!--                    </tr>-->
<!--                    <tr>-->
<!--                        <td>-->
<!--                            <div class="flag">-->
<!--                                <i class="material-icons">dashboard</i>-->
<!--                            </div>-->
<!--                        </td>-->
<!--                        <td>Wordpress Service</td>-->
<!--                        <td class="text-right"> Medium</td>-->
<!--                        <td class="text-right"> 4 Cores</td>-->
<!--                        <td class="text-right action">-->
<!--                            <a class="nav-link" href="/catalog/2">-->
<!--                                <button type="button" class="btn btn-default btn-link" rel="tooltip" data-placement="bottom" title="Modify Service">-->
<!--                                    <i class="material-icons">edit</i>-->
<!--                                </button>-->
<!--                            </a>-->
<!--                        </td>-->
<!--                    </tr>-->
<!--                    <tr>-->
<!--                        <td>-->
<!--                            <div class="flag">-->
<!--                                <i class="material-icons">dashboard</i>-->
<!--                            </div>-->
<!--                        </td>-->
<!--                        <td>Wordpress Service</td>-->
<!--                        <td class="text-right"> Big</td>-->
<!--                        <td class="text-right"> 8 Cores</td>-->
<!--                        <td class="text-right action">-->
<!--                            <a class="nav-link" href="/catalog/3">-->
<!--                                <button type="button" class="btn btn-default btn-link" rel="tooltip" data-placement="bottom" title="Modify Service">-->
<!--                                    <i class="material-icons">edit</i>-->
<!--                                </button>-->
<!--                            </a>-->
<!--                        </td>-->
<!--                    </tr>-->
<!--                    </tbody>-->
<!--                </table>-->
<!--            </div>-->
<!--        </div>-->
<!--    </div>-->
<!---->
<!--</div>-->
