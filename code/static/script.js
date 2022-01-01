function ff(){
    $.ajax({
        url:"http://api.navasan.tech/latest/?api_key=8hElQpXSTGLqqX76Y38c0faKd3FPShnH",
        method:"GET",
        onsuccess:function(res){
            console.log(res);
        }
    })
}