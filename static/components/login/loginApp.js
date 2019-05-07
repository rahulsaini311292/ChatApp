angular.module('chatAppLogin',[
    'ngAnimate',
    'toastr',
    'ngCookies'
])


// Sending CSRF token with all requests
.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}])

.factory('myHttpInterceptor', function($q,$cookies,$injector) {
    return {
        // optional method
        'request': function(config) {
        // do something on success
        config.headers = config.headers || {};
        var jwtToken = $cookies.get('jwt')

        if (jwtToken != null){
            config.headers.Authorization = 'JWT ' + jwtToken;
        }


        return config;
        },

        // optional method
        'requestError': function(rejection) {
        // do something on error

        if (canRecover(rejection)) {
        return responseOrNewP
        // do something on successromise
        }
        return $q.reject(rejection);
        },

        // optional method
        'response': function(response) {
        return response;
        },

        // optional method
        'responseError': function(res) {
        // do something on error
        var toastr = $injector.get('toastr');
        if(res.data.detail== "Authentication credentials were not provided."){
            toastr.error('You are not logged in ! Please Login to continue');
                $cookies.remove('jwt');
                setTimeout(function(){
                location.href = '/';
            }, 3000);
        }
        else if(res.data.detail== "Signature has expired."){
            toastr.error('Session has expired! Redirecting to login page');
                $cookies.remove('jwt');
                setTimeout(function(){
                location.href = '/';
            }, 3000);
        }


        return $q.reject(res)
        // if (canRecover(rejection)) {
        // return responseOrNewPromise
        // }
        // return $q.reject(rejection);
        }



    };
})

.config(function($httpProvider){
    $httpProvider.interceptors.push('myHttpInterceptor')
})

//toastr

.config(function(toastrConfig) {
    angular.extend(toastrConfig, {
        autoDismiss: false,
        containerId: 'toast-container',
        maxOpened: 0,
        newestOnTop: true,
        positionClass: 'toast-bottom-right',
        preventDuplicates: false,
        preventOpenDuplicates: false,
        target: 'body'
    });
})

.controller('loginController',['$scope','$http','toastr','$cookies','$window', function($scope,$http,toastr,$cookies,$window){

    $scope.user = {}

    $scope.loginUser = function(user){

        var success = function(response){
            console.log(response)
            $window.localStorage.setItem('jwt', response.data.token);
            window.location.href="index"
        }

        var failure = function(error){
            console.log(error.data.non_field_errors[0])
            var error_msg = error.data.non_field_errors[0]
            toastr.error(error_msg)
        }

        console.log(user)
        $http.post('/api-token-auth/',user).then(success,failure)

    }

    $scope.registerUser = function(user){

        var success = function(response){
            console.log(response)
            toastr.success("User Registered Successfully !")
        }

        var failure = function(error){
            console.log(error)

            if(error.data.error=="Username Already Exists."){
                toastr.error("User Already Exists!")
            }

            else{
                toastr.error("An error occurred while registering User !")
            }
        }

        console.log(user)

        $http.post('/api/register/user',user).then(success,failure)
    }

}])