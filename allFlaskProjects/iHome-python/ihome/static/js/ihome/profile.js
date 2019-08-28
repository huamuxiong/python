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
    // 上传头像
    $('#form-avatar').submit(function (e) {
        // 阻止表单的默认行为
        e.preventDefault();
        // 表单异步提交
        $(this).ajaxSubmit({
            url: '/api/v1.0/users/avatar',
            type: 'post',
            dataType: 'json',
            headers: {
                'X-CSRFToken': getCookie('csrf_token')
            },
            success: function (resp) {
                if (resp.errno == '0') {
                    var avatarUrl = resp.data.avatar_url;
                    $('#user-avatar').attr('src', avatarUrl);
                } else {
                    alert(resp.errmsg);
                }
            }
        });
    });

    // 获取用户信息
    $.get('/api/v1.0/user', function (resp) {
        if (resp.errno == '4104') {
            // 未登录，跳转到登陆界面
            location.href = '/login.html'
        } else if(resp.errno == '0') {
            // 有获取到用户信息
            $('#user-name').val(resp.data.name);
            if (resp.data.avatar) {
                $('#user-avatar').attr('src', resp.data.avatar);
            }
        }
    }, "json");
    
    // 修改用户名
    $('#form-name').submit(function (e) {
        // 阻止form表单的默认行为
        e.preventDefault();
        // 获取name值
        var name = $('#user-name').val();
        // 判断用户名是否为空
        if (!name) {
            alert('用户名不能为空！');
            return
        }
        // ajax 提交用户名
        $.ajax({
            url: '/api/v1.0/users/name',
            data: JSON.stringify({'name': name}),
            type: 'PUT',
            contentType: 'application/json',
            dataType: 'json',
            headers: {
                "X-CSRFToken": getCookie('csrf_token')
            },
            success: function (data) {
                if (data.errno == '0') {
                    $('.error-msg').hide();
                    showSuccessMsg();
                } else if (data.errno == '4001') {
                    $('.error-msg').show();
                } else if (data.errno == '4101') {
                    location.href = '/login.html';
                }
            }
        });

    });
});

