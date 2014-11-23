'use strict'

bidApp.services.bid = angular.module('bidServices', []);

bidApp.services.bid
.factory('ModalService', [function () {
        var service = this;

        this['ctrl']        = null;
        this['view']        = angular.element('#modal');
        this['scope']       = this;
        this['setContent']  = function (contentObjects) {
            for (var i in contentObjects) {
                this.ctrl[i] = contentObjects[i];
            }
        };
        this['setBody']     = function (body) {
            this.setContent({'body': body});
        }
        this['setTitle']    = function (title) {
            this.setContent({'title': title});
        };
        this['show']        = function (callback) {
            if (typeof callback === 'undefined') callback = function () {};
            service.view.modal();
            callback.call(service, arguments);
            service.ctrl.$apply();
        };
        return service;
    }
]);