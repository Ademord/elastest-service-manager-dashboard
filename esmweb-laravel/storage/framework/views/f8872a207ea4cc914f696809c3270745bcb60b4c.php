<?php $__env->startSection('content'); ?>
<h2>Services Overview</h2>
<?php
$services = [
    ['name' => 'Wordpress',     'image_path' => "../assets/img/" .  "wordpress"   . "-icon.png"],
    ['name' => 'Kubernetes',    'image_path' => "../assets/img/" .  "kubernetes" . "-icon.png"],
    ['name' => 'OpenStack',     'image_path' => "../assets/img/" .  "openstack"  . "-icon.png"],
    ['name' => 'Redis',         'image_path' => "../assets/img/" .  "redis"      . "-icon.png"],
    ['name' => 'Elastest',      'image_path' => "../assets/img/" .  "elastest"   . "-icon.png"],
    ['name' => 'Spark',         'image_path' => "../assets/img/" .  "spark"      . "-icon.png"],
    ['name' => 'OpenShift',     'image_path' => "../assets/img/" .  "openshift"  . "-icon.png"],
    ['name' => 'Postgres',      'image_path' => "../assets/img/" .  "postgres"   . "-icon.png"],
    ['name' => 'Cyclops',       'image_path' => "../assets/img/" .  "cyclops"    . "-icon.png"],
    ['name' => 'Hurtle',        'image_path' => "../assets/img/" .  "hurtle"     . "-icon.png"]
];
?>

<div class="flex-container container-plan pr-3">

    <?php $__currentLoopData = $services; $__env->addLoop($__currentLoopData); foreach($__currentLoopData as $service): $__env->incrementLoopIndices(); $loop = $__env->getLastLoop(); ?>
        <?php echo $__env->make('includes.service_card', $service, array_except(get_defined_vars(), array('__data', '__path')))->render(); ?>
    <?php endforeach; $__env->popLoop(); $loop = $__env->getLastLoop(); ?>
    <?php echo $__env->make('includes.service_card_icon', ['name' => 'Custom', 'icon' => 'dashboard'], array_except(get_defined_vars(), array('__data', '__path')))->render(); ?>

</div>
<?php $__env->stopSection(); ?>

<!---->
<!--<div class="col-md-6">-->
<!--    <div class="table-responsive table-sales">-->
<!--        <table class="table">-->
<!--            <tbody>-->
<!--            <tr>-->
<!--                <td>-->
<!--                    <div class="flag">-->
<!--                        <i class="material-icons">dashboard</i>-->
<!--                    </div>-->
<!--                </td>-->
<!--                <td>Wordpress Service</td>-->
<!--                <td class="text-right"> Small</td>-->
<!--                <td class="text-right"> 2 Cores</td>-->
<!--                <td class="text-right action">-->
<!--                    <a class="nav-link" href="/catalog/1">-->
<!--                        <button type="button" class="btn btn-default btn-link" rel="tooltip" data-placement="bottom" title="Modify Service">-->
<!--                            <i class="material-icons">edit</i>-->
<!--                        </button>-->
<!--                    </a>-->
<!--                </td>-->
<!--            </tr>-->
<!--            <tr>-->
<!--                <td>-->
<!--                    <div class="flag">-->
<!--                        <i class="material-icons">dashboard</i>-->
<!--                    </div>-->
<!--                </td>-->
<!--                <td>Wordpress Service</td>-->
<!--                <td class="text-right"> Medium</td>-->
<!--                <td class="text-right"> 4 Cores</td>-->
<!--                <td class="text-right action">-->
<!--                    <a class="nav-link" href="/catalog/2">-->
<!--                        <button type="button" class="btn btn-default btn-link" rel="tooltip" data-placement="bottom" title="Modify Service">-->
<!--                            <i class="material-icons">edit</i>-->
<!--                        </button>-->
<!--                    </a>-->
<!--                </td>-->
<!--            </tr>-->
<!--            <tr>-->
<!--                <td>-->
<!--                    <div class="flag">-->
<!--                        <i class="material-icons">dashboard</i>-->
<!--                    </div>-->
<!--                </td>-->
<!--                <td>Wordpress Service</td>-->
<!--                <td class="text-right"> Big</td>-->
<!--                <td class="text-right"> 8 Cores</td>-->
<!--                <td class="text-right action">-->
<!--                    <a class="nav-link" href="/catalog/3">-->
<!--                        <button type="button" class="btn btn-default btn-link" rel="tooltip" data-placement="bottom" title="Modify Service">-->
<!--                            <i class="material-icons">edit</i>-->
<!--                        </button>-->
<!--                    </a>-->
<!--                </td>-->
<!--            </tr>-->
<!--            </tbody>-->
<!--        </table>-->
<!--    </div>-->
<!--</div>-->
<!--<div class="col-md-6 ml-auto mr-auto">-->
<!--    <div id="worldMap" style="height: 300px;"></div>-->
<!--</div>-->
<?php echo $__env->make('layouts.default', array_except(get_defined_vars(), array('__data', '__path')))->render(); ?>