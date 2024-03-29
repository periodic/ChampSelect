'use strict';

/* Services */

// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('myApp.services', ['ngResource'])
    .value('version', '0.1')
    .factory('Game', function ($resource) {
        return $resource('game/:id.json', {}, {
            create: {method: "POST", params: {id: 'create'}},
        });
    });
