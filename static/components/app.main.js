angular.module('chat.mainApp',[
    'ui.router',
//    'ngCookies',
//    'ngSanitize',
//    'ngStorage'
])


.config(['$stateProvider', '$urlRouterProvider',], function($stateProvider, $urlRouterProvider){

    $urlRouterProvider.otherwise('/');

    $stateProvider
    .state('app', {
//        abstract: true,
        url: '/',
        templateUrl: '/static/components/index.html',
        controller:'mainController',
        controllerAs:'mainCtrl'
    })



})