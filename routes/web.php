<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});


Route::get('/catalog', function () {
    return view('catalog.index');
});
Route::get('/catalog2', function () {
    return view('catalog.index2');
});
Route::get('/catalog/1', function () {
    return view('catalog.show1');
});
Route::get('/catalog/2', function () {
    return view('catalog.show2');
});
Route::get('/catalog/3', function () {
    return view('catalog.show3');
});



Route::get('/instances', function () {
    return view('instances.index');
});
Route::get('/test', function () {
    return view('test');
});
//Route::resource('lugar', 'LugarController');
//Route::resource('miembro', 'MiembroController', ['except' => ['edit', 'destroy', 'create', 'update', 'store'] ]);
//Route::get('matricula/get/{filename}', [
//    'as' => 'getentry', 'uses' => 'MatriculaController@get']);
//Route::get('/db', function(){
//    return DB::table('lugar')->insertGetId(['nombre' => 'UPSA2']);
//});
//Route::get('/reportes/coincidencias/lugar', 'ReportsController@coincidenciasPorLugar');
//Route::get('/reportes/fake-propietarios', ['as' => 'reportes.fake_propietarios', 'uses' => 'ReportsController@fakePropietarios']);
