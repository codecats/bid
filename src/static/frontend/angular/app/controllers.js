'use strict';

bidApp.controllers.bid = angular.module('bidControllers', []);
/* Ctrl */

bidApp.controllers.bid.
    controller('MainCtrl', ['$scope', '$http',
        function($scope, $http) {
            var body            = angular.element('body'),
                btnAddProduct   = angular.element('#add-product');
            body.addClass('loading')
            $scope.title = 'Bid'
            //events
            btnAddProduct.bind('click', function () {
                btnAddProduct.addClass('loading');
                var removeMask = function () {
                    btnAddProduct.removeClass('loading');
                };
                $scope.$broadcast('onAddProduct', removeMask)
            });

            body.removeClass('loading')
        }]);

bidApp.controllers.bid.
    controller(
        'ModalController', ['$scope', '$http', '$sce', 'ModalService', 'ComponentService',
        function ($scope, $http, $sce, modalService, componentService) {
            $scope.createComponent = componentService.createComponent;
            $scope.renderClass  = function (btn) {
                return (typeof btn.class !== 'undefined') ? btn.class : 'btn-primary';
            };
            $scope.getFunction  = function (btn, me) {
                var func = (typeof btn.function !== 'undefined') ? btn.function : function () {};
                return func(btn, me);
            };
            modalService['ctrl']     = $scope;
            modalService['_ctrl']    = this;
    }]);