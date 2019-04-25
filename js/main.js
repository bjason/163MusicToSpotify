// AOS
AOS.init({
	duration: 500,
})

jQuery(document).ready(function ($) {
	'use strict';


	// Animsition
	$(".animsition").animsition();

	// Scrollax
	$.Scrollax();

	// Smooth scroll
	var $root = $('html, body');

	$('a.js-smoothscroll[href^="#"]').click(function () {
		$root.animate({
			scrollTop: $($.attr(this, 'href')).offset().top - 40
		}, 500);

		return false;
	});

	// Owl
	$('.wide-slider').owlCarousel({
		loop: true,
		autoplay: true,
		margin: 10,
		animateOut: 'fadeOut',
		animateIn: 'fadeIn',
		nav: true,
		autoplayHoverPause: false,
		items: 1,
		autoheight: true,
		navText: ["<span class='ion-chevron-left'></span>", "<span class='ion-chevron-right'></span>"],
		responsive: {
			0: {
				items: 1,
				nav: false
			},
			600: {
				items: 1,
				nav: false
			},
			1000: {
				items: 1,
				nav: true
			}
		}
	});

	// Window Resize
	$(window).resize(function () {
		var searchButton = $(this);
		$('.js-templateux-menu li').removeClass('staggard');
		$('.js-toggle-menu').removeClass('is-active');
		if (searchButton.width() > 768) {
			$('body').removeClass('menu-open');
			$('.js-templateux-menu').css('display', 'block');

		} else {
			if (searchButton.width() < 768) {
				$('.js-templateux-menu').css('display', 'none');
			}
		}
	});
});


function searchPlaylist() {
	var url = $('#playlistUrl').val();

	if (url.includes("music.163.com/#/playlist?id=")) {
		let index = url.indexOf("=");
		var playlistId = url.substring(index + 1);

		getPlaylistInfo(playlistId, "020111");
	} else if (url.includes("y.qq.com/n/yqq/playlist/")) {
		let start = url.indexOf('playlist/');
		let end = url.indexOf('.html');
		var playlistId = url.substring(start + 9, end);

		getPlaylistInfo(playlistId, "020331");
	} else {
		// input error
		$('#playlistUrl').val("");
		$('#playlistUrl').css("background", "pink");
		shakeElement($('#urlContainer'));
	}
}

function getPlaylistInfo(playlistId, TransCode) {
	var reqUrl = "https://api.hibai.cn/api/index/index";
	var postContent = {
		"TransCode": TransCode,
		//"020111 for 163
		// 020221 for kugou
		// 020331 for qq music
		"OpenId": "123456789",
		"Body": {
			"SongListId": playlistId
		}
	};
	var searchButton = $('#searchBtn');
	var loadingText = '<i class="fa fa-circle-o-notch fa-spin"></i> 获取中...';

	changeButtonText(searchButton, loadingText);

	$.ajax(reqUrl, {
		data: JSON.stringify(postContent),
		contentType: 'application/json',
		type: 'POST',
		accept: 'application/json',
		complete: function () {
			var searchButton = $('#searchBtn');
			resetButtonText(searchButton);
		},
		success: function (data) {
			if (data.ErrCode != "OK") {
				let err_info = $("#errInfo");
				switch (data.ErrCode) {
					case "1001":
						err_info.html("网易云歌单ID不存在");
						break;
					case "1003":
						err_info.html("网易云音乐歌单不存在");
						break;
					case "3001":
						err_info.html("QQ音乐歌单ID不存在");
						break;
					case "3003":
						err_info.html("QQ音乐歌单不存在");
						break;
					default:
						err_info.html("出错了！")
						break;
				}

				fadeoutError();
			} else {
				let body = data.Body;

				if (TransCode == "020331") { // QQMUSIC
					$("#plname").html("歌单ID");
					var playlist_name = playlistId;
					var tracks = body;
				} else {
					$("#plname").html("歌单名");
					var playlist_name = body.name;
					var tracks = body.songs;
				}

				let res = [];

				tracks.forEach(track => {
					var title = track.title;
					var artist = track.author;

					res.push(title + '-' + artist);
				});
				res = res.join('\n');
				$('#playlistName').text(playlist_name);
				$('#playlistContent').val(res);

				$('html, body').animate({
					scrollTop: $($("#next2")).offset().top - 40
				}, 500);

				return false;
			}
		},
		error: function (request) {
			let err_info = $("#errInfo");
			err_info.html("连接错误，请稍后重试");

			fadeoutError();
		}
	})
}

function fadeoutError() {
	setTimeout(() => {
		$("#errInfo").fadeOut();
	}, 3000);
}

function shakeElement(element) {
	element.addClass('shake');
	setTimeout(function () {
		element.removeClass('shake');
		$('#playlistUrl').focus();
		$('#playlistUrl').addClass('animationColorFade');

		setTimeout(() => {
			$('#playlistUrl').css("background", "#f6f6f6");
			$('#playlistUrl').removeClass('animationColorFade')
		}, 1000);
	}, 800);
};

function clickToCopy() {
	var content = $('#playlistContent');
	var btn = $('#copyBtn');
	var CopyText = '√ 已复制';

	content.select();
	document.execCommand('copy');

	changeButtonText(btn, CopyText);
	setTimeout(() => {
		resetButtonText(btn);
	}, 2000);
}

function changeButtonText(button, text) {
	if (button.html() !== text) {
		button.data('original-text', button.html());
		button.html(text);
	}
}

function resetButtonText(button) {
	button.html(button.data('original-text'));
}