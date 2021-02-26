function codeAddress() {
    var lat = document.getElementById("lat_num").innerHTML;
    lat=parseFloat(lat);

    var lon = document.getElementById("lon_num").innerHTML;
    lon=parseFloat(lon);
    var H;
    var V;
    if(lat<0){
        document.getElementById('latitude').innerHTML = "S";
        document.getElementById('lat_num').innerHTML = Math.abs(lat);
    }else{
        document.getElementById('latitude').innerHTML = "N";
        
    }
    if(lon<0){
        document.getElementById('longitude').innerHTML = "W";
        document.getElementById('lon_num').innerHTML = Math.abs(lon);
    }else{
        document.getElementById('longitude').innerHTML = "E";
    }
    
}
window.onload = codeAddress;

