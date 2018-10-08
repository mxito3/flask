$(document).ready(function($) {
    //给列表项定高
    var width=$('.cell').width();
    var bodyWidth=$('body').width();
    console.log(bodyWidth);
    if(bodyWidth>768)
    {
    	console.log("大于");
    	var height=$('.innerItem').height(3*width/5);
    }
    // $('.cell').height(height/3);
    // console.log("宽度是"+width);
    // console.log("长度是"+height);
    var video = $("video");
    // console.log(video.length);

    for (let i = 0; i < video.length; i++) {
        video[i].addEventListener('play', function() {
            console.log("点击了");
            var index = $(this).attr("index");
            // console.log(index);
            // console.log($(this).attr("id"));
            video[i].pause();
            var id = 'video' + index;
            var videoHref = $('#' + id + " source").attr('src');
            var videoTitle = $('#videoTitle' + index).html()
            //跳转到播放页面

            // console.log(videoHref)
            // console.log(videoTitle)
            var videoNeedPlay = []
            videoNeedPlay.push(videoHref)
            videoNeedPlay.push(videoTitle)
            // console.log($("video[i] source").src)
            console.log(videoNeedPlay);
            $.cookie('needPlayVideoHref', videoHref);
            $.cookie('needPlayVideoTitle', videoTitle);
            location.href = '/play';
        });
    }


});