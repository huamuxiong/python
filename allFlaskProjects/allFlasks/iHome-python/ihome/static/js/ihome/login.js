function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function() {
    $("#mobile").focus(function(){
        $("#mobile-err").hide();
    });
    $("#password").focus(function(){
        $("#password-err").hide();
    });
    $(".form-login").submit(function(e){
        e.preventDefault();
        mobile = $("#mobile").val();
        passwd = $("#password").val();
        if (!mobile) {
            $("#mobile-err span").html("请填写正确的手机号！");
            $("#mobile-err").show();
            return;
        } 
        if (!passwd) {
            $("#password-err span").html("请填写密码!");
            $("#password-err").show();
            return;
        }
        // 将数据放到data中
        var data = {
            mobile: mobile,
            password: passwd
        };
        // 将data转换成json格式
        var jsonData = JSON.stringify(data);
        // 发起ajax请求
        $.ajax({
            url: '/api/v1.0/sessions',
            type: 'post',
            data: jsonData,
            contentType: 'application/json',
            dataType: 'json',
            headers: {
                'X-CSRFToken': getCookie('csrf_token')
            },
            success: function (resp) {
                if (resp.errno == '0') {
                    location.href = 'index.html'
                } else {
                    $("#password-err span").html(resp.errmsg);
                    $("#password-err").show();
                }
            }
            
        });
    });
});