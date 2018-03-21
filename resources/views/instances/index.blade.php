@extends('layouts.default')
@section('content')
    <div class="row">
    <div class="col-md-12">
        <div class="card ">
            <div class="card-header card-header-success card-header-icon">
                <div class="card-icon">
                    <i class="material-icons">access_time</i>
                </div>
                <h4 class="card-title">Instances Overview</h4>
            </div>

            <div class="card-body ">
                <div class="row">
                    <div class="col-md-6">
                        <div class="table-responsive table-sales">
                            <table class="table">
                                <tbody>
                                <tr>
                                    <td>
                                        <div class="flag">
                                            <img src="../assets/img/flags/US.png"
                                        </div>
                                    </td>
                                    <td>Wordpress_Service_122130192857</td>
                                    <td class="text-right">12 hours <i class="material-icons">access_time</i></td>
                                </tr>
                                <tr>
                                    <td>
                                        <div class="flag">
                                            <img src="../assets/img/flags/US.png"
                                        </div>
                                    </td>
                                    <td>Wordpress_Service_122130192857</td>
                                    <td class="text-right">2 hours <i class="material-icons">access_time</i></td>
                                </tr>
                                <tr>
                                    <td>
                                        <div class="flag">
                                            <img src="../assets/img/flags/US.png"
                                        </div>
                                    </td>
                                    <td>Wordpress_Service_122130192857</td>
                                    <td class="text-right">24 hours <i class="material-icons">access_time</i></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div class="col-md-6 ml-auto mr-auto">
                        <div id="worldMap" style="height: 300px;"></div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</div>
@stop