@extends('layouts.default')
@section('content')
<div class="row">
    <div class="col-md-4">
        <div class="card card-chart">
            <div class="card-header card-header-icon card-header-rose">
                <div class="card-icon">
                    <i class="material-icons">pie_chart</i>
                </div>
                <h4 class="card-title">Current Instances</h4>
            </div>
            <div class="card-body">
                <div id="chartPreferences" class="ct-chart"></div>
            </div>
            <div class="card-footer">
                <div class="row">
                    <div class="col-md-12">
                        <h6 class="card-category">Legend</h6>
                    </div>
                    <div class="col-md-12">
                        <i class="fa fa-circle text-success"></i> Running
                        <i class="fa fa-circle text-warning"></i> Pending
                        <i class="fa fa-circle text-danger"></i> Crashed
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-8">
        <div class="card">
            <div class="card-header card-header-icon card-header-rose">
                <div class="card-icon">
                    <i class="material-icons">insert_chart</i>
                </div>
                <h4 class="card-title">Instances Performance
                    <small>- Running vs Crashes</small>
                </h4>
            </div>
            <div class="card-body">
                <div id="multipleBarsChart" class="ct-chart"></div>
            </div>
        </div>
    </div>
</div>

<div class="row">
    <div class="col-md-12">
        <div class="card">
            <div class="card-header card-header-rose card-header-icon">
                <div class="card-icon">
                    <i class="material-icons">assignment</i>
                </div>
                <h4 class="card-title">Instances Overview</h4>

            </div>

            <div class="card-body">
                <div class="table-responsive">
                    <table class="table">
                        <thead class="text-primary">
                        <tr>
                            <th>ID</th>
                            <th>Service</th>
                            <th>Backend</th>
                            <th>Since</th>
                            <th class="text-right">Actions</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>92</td>
                            <td>Spark</td>
                            <td>Kubernetes</td>
                            <td><i class="fa fa-circle text-danger"></i> 26 days</td>
                            <td class="td-actions text-right">
                                <button type="button" rel="tooltip" class="btn btn-info" data-original-title="" title="">
                                    <i class="material-icons">info</i>
                                    <div class="ripple-container"></div></button>
                                <button type="button" rel="tooltip" class="btn btn-success" data-original-title="" title="">
                                    <i class="material-icons">history</i>
                                    <div class="ripple-container"></div></button>
                                <button type="button" rel="tooltip" class="btn btn-danger" data-original-title="" title="">
                                    <i class="material-icons">close</i>
                                    <div class="ripple-container"></div></button>
                            </td>
                        </tr>
                        <tr>
                            <td>62</td>
                            <td>Custom_LabCC2</td>
                            <td>OpenStack</td>
                            <td><i class="fa fa-circle text-warning"></i> 156 days</td>
                            <td class="td-actions text-right">
                                <button type="button" rel="tooltip" class="btn btn-info" data-original-title="" title="">
                                    <i class="material-icons">info</i>
                                    <div class="ripple-container"></div></button>
                                <button type="button" rel="tooltip" class="btn btn-success" data-original-title="" title="">
                                    <i class="material-icons">history</i>
                                    <div class="ripple-container"></div></button>
                                <button type="button" rel="tooltip" class="btn btn-danger" data-original-title="" title="">
                                    <i class="material-icons">close</i>
                                    <div class="ripple-container"></div></button>
                            </td>
                        </tr>
                        <tr>
                            <td>62</td>
                            <td>Hurtle</td>
                            <td>OpenStack</td>
                            <td><i class="fa fa-circle text-danger"></i> 256 days</td>
                            <td class="td-actions text-right">
                                <button type="button" rel="tooltip" class="btn btn-info" data-original-title="" title="">
                                    <i class="material-icons">info</i>
                                    <div class="ripple-container"></div></button>
                                <button type="button" rel="tooltip" class="btn btn-success" data-original-title="" title="">
                                    <i class="material-icons">history</i>
                                    <div class="ripple-container"></div></button>
                                <button type="button" rel="tooltip" class="btn btn-danger" data-original-title="" title="">
                                    <i class="material-icons">close</i>
                                    <div class="ripple-container"></div></button>
                            </td>
                        </tr>
                        <tr>
                            <td>43</td>
                            <td>Elastest</td>
                            <td>Docker</td>
                            <td><i class="fa fa-circle text-success"></i> 20 seconds</td>
                            <td class="td-actions text-right">
                                <button type="button" rel="tooltip" class="btn btn-info" data-original-title="" title="">
                                    <i class="material-icons">info</i>
                                    <div class="ripple-container"></div></button>
                                <button type="button" rel="tooltip" class="btn btn-success" data-original-title="" title="">
                                    <i class="material-icons">history</i>
                                    <div class="ripple-container"></div></button>
                                <button type="button" rel="tooltip" class="btn btn-danger" data-original-title="" title="">
                                    <i class="material-icons">close</i>
                                    <div class="ripple-container"></div></button>
                            </td>
                        </tr>
                        <tr>
                            <td>31</td>
                            <td>Cyclops</td>
                            <td>Unikernel</td>
                            <td><i class="fa fa-circle text-success"></i> 2 hours</td>
                            <td class="td-actions text-right">
                                <button type="button" rel="tooltip" class="btn btn-info" data-original-title="" title="">
                                    <i class="material-icons">info</i>
                                    <div class="ripple-container"></div></button>
                                <button type="button" rel="tooltip" class="btn btn-success" data-original-title="" title="">
                                    <i class="material-icons">history</i>
                                    <div class="ripple-container"></div></button>
                                <button type="button" rel="tooltip" class="btn btn-danger" data-original-title="" title="">
                                    <i class="material-icons">close</i>
                                    <div class="ripple-container"></div></button>
                            </td>
                        </tr>
                        <tr>
                            <td>51</td>
                            <td>Wordpress</td>
                            <td>Openshift</td>
                            <td><i class="fa fa-circle text-success"></i> 106 days</td>
                            <td class="td-actions text-right">
                                <button type="button" rel="tooltip" class="btn btn-info" data-original-title="" title="">
                                    <i class="material-icons">info</i>
                                    <div class="ripple-container"></div></button>
                                <button type="button" rel="tooltip" class="btn btn-success" data-original-title="" title="">
                                    <i class="material-icons">history</i>
                                    <div class="ripple-container"></div></button>
                                <button type="button" rel="tooltip" class="btn btn-danger" data-original-title="" title="">
                                    <i class="material-icons">close</i>
                                    <div class="ripple-container"></div></button>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

</div>
@stop