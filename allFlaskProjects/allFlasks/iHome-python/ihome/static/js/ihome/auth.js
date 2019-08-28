function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$(document).ready(function () {
    // 查询用户的实名信息
    $.get('/api/v1.0/users/auth', function (resp) {
        // 判断是否登陆，4101表示未登录
        if(resp.errno == '4101'){
            location.href = '/login.html'
        }else if(resp.errno == '0') {
            // 已经登陆，如果返回的real_name与id_card不为null，表示用户有填写实名信息
            if (resp.data.real_name && resp.data.id_card){
                // 将实名信息填写到页面中，并不再可以修改，同时隐藏按钮
                $('#real-name').val(resp.data.real_name);
                $('#id-card').val(resp.data.id_card);
                $('#real-name').prop('disabled', true);
                $('#id-card').prop('disabled', true);
                $('#form-auth>input[type=submit]').hide();
            }
        }
    }, "json");

    // 用户实名信息的提交行为
    $('#form-auth').submit(function (e) {
        // 阻止表单的默认提交行为
        e.preventDefault();
        // 获取实名信息
        var real_name = $('#real-name').val();
        var id_card = $('#id-card').val();
        // 判断是否为空
        if (real_name == "" || id_card == ""){
            $('.error-msg').show();
        }
        // 将数据转换成json格式
        var data = {
            "real_name": real_name,
            "id_card": id_card
        };
        var json_data = JSON.stringify(data);
        // ajax提交，保存实名认证信息
        $.ajax({
            url: '/api/v1.0/users/auth',
            data: json_data,
            dataType: 'json',
            type: 'post',
            contentType: 'application/json',
            headers: {
                'X-CSRFToken': getCookie('csrf_token')
            },
            success: function (resp) {
                if (resp.errno == '0'){
                    $('.error-msg').hide();
                    showSuccessMsg();
                    $('#real-name').prop('disabled', true);
                    $('#id-card').prop('disabled', true);
                    $('#form-auth>input[type=submit]').hide();
                }else{
                    alert(resp.errmsg);
                }
            }
        });

    });
});


