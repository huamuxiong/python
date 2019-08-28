$(document).ready(function(){
    // 对于发布房源，只有认证后的用户才可以，所以需要先进行判断用户的额实名认证状态
    $.get("/api/v1.0/users/auth", function (resp) {
        if (resp.errno == '4101') {
            // 未登录
            location.href = '/login.html';
        } else if (resp.errno == '0') {
            // 未认证的用户，在页面中显示“去认证”的按钮
            if (!(resp.data.real_name && resp.data.id_card)) {
                $(".auth-warn").show();
                return;
            }
            // 已认证的用户，请求发布的房源信息
            $.get("/api/v1.0/user/houses", function (resp) {
                if (resp.errno == '0') {
                    $("#houses-list").html(template("houses-list-tmpl", {houses: resp.data.houses}));
                } else {
                    $("#houses-list").html(template("houses-list-tmpl", {houses: []}));
                }
            });
        }
    });
});