var myApp = angular.module('myApp', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});
function RankingCtrl($scope, $http, $timeout){
    $scope.anyone = false;
    $scope.gamers = [];
    $scope.onTimeout = function(){
        $scope.gamers = [];
        $http.get('getsorted/').success(function(data){
            $scope.gamers=data;
            if(data != 0){
                $scope.anyone = true;
            }
        });
        $timeout($scope.onTimeout, 30000); /*30 sekund*/
    };
    $scope.onTimeout();
}
