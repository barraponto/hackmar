app.controller('marController', ['$scope', '$window', '$http', '$location', '$filter', function ($scope, $window, $http, $location, $filter ) {

  
    
    $http.get('../acervo.json').
    //$http.get('scripts/services/objects.json').
      then(function(response) {
        // when the response is available
        $scope.dados = response.data;
        //console.log($scope.dados);
        $scope.acervo = [];
        for (elem in $scope.dados) {
            $scope.acervo.push($scope.dados[elem]);
        }
        //ok
        return $scope.acervo;
      }, function(response) {
        // error.
        
      });
    
    //número de elementos no loop    
    
    
        
    //console.log($scope.showEvent.length);
      
    


}]);
