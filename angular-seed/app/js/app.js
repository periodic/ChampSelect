'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', ['myApp.filters', 'myApp.services', 'myApp.directives', 'myApp.controllers']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/new', {templateUrl: 'partials/partial1.html', controller: 'GameController'});
    $routeProvider.when('/game/:game_id', {templateUrl: 'partials/partial2.html', controller: 'ChampSelectController'});
    $routeProvider.otherwise({redirectTo: '/new'});
  }]);
