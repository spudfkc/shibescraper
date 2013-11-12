var MAX_DOGES = 10;

var dogeRaster = new Raster('doge');
dogeRaster.position = view.center;
dogeRaster.rotate(45);

doges = [];
for (var i = 0; i < MAX_DOGES; i++) {
    var randomDoge = new Raster('doge');
    randomDoge.position = Point.random() * view.size;
    doges.push(randomDoge);
}

function onResize(event) {
    dogeRaster.position = view.center;
}

function onFrame(event) {
    /*for (var i = 0; i < doges.length; i++) {
        doges[i].rotate(5);
    }*/
    dogeRaster.rotate(3);
}

/*************/
/** Drawing **/
/*************/

var path;
var drawTool = new Tool();
tool.onMouseDown = function(event) {
    path = new Path();
    path.strokeColor = 'black';
    path.add(event.point);
}

tool.onMouseDrag = function(event) {
    path.add(event.point);
}
