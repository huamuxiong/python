$(function () {
    $('.zhiding').on('click', function () {
        layer.open({
            type: 2,
            title: '指定购房页面',
            shadeClose: true,
            shade: 0.8,
            area: ['580px', '90%'],
            content: '/zhiding/' //iframe的url
        });
    });

});

function fabu() {
        layer.open({
            type: 2,
            title: '发布',
            shadeClose: true,
            shade: 0.8,
            area: ['100%', '100%'],
            content: '/fabu/',
        });
    }

