"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var angular_1 = require("@uirouter/angular");
var authentication_service_1 = require("app/services/authentication.service");
var LoginComponent = /** @class */ (function () {
    function LoginComponent(stateService, authService) {
        this.stateService = stateService;
        this.authService = authService;
    }
    LoginComponent.prototype.ngOnInit = function () {
        if (localStorage.getItem('user')) {
            this.stateService.go('scrumboard');
        }
    };
    LoginComponent.prototype.login = function (username, password) {
        var _this = this;
        this.authService.loginUser({ "username": username.value, "password": password.value })
            .subscribe(function () {
            localStorage.setItem('user', username.value);
            _this.stateService.go('scrumboard');
        }, function () {
            _this.invalid_message = "INVALID USERNAME OR PASSWORD";
        });
    };
    LoginComponent.prototype.authenticate = function () {
        if (!localStorage.getItem('user')) {
            this.stateService.go('login');
        }
    };
    LoginComponent = __decorate([
        core_1.Component({
            selector: 'app-login',
            templateUrl: './login.component.html',
            styleUrls: ['./login.component.scss']
        }),
        __metadata("design:paramtypes", [angular_1.StateService,
            authentication_service_1.AuthenticationService])
    ], LoginComponent);
    return LoginComponent;
}());
exports.LoginComponent = LoginComponent;
//# sourceMappingURL=login.component.js.map