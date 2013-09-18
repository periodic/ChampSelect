'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
  .controller('GameController', ['$scope', 'Game', function($scope, Game) {
      $scope.createGame = function () {
          console.log("Saving game.", $scope.game);
          var game = Game.create($scope.game);
      };
      $scope.deleteGame = function () {
          console.log("Delete game.", $scope.game);
      };
  }])
  .controller("ChampSelectController", ['$scope', '$routeParams', 'Game', function ($scope, $routeParams, Game) {
      $scope.game = Game.get({gameId: $routeParams.game_id});
  }]);
