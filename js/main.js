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

var reqUrl = "https://api.hibai.cn/api/index/index";

function searchPlaylist() {
	var url = $('#playlistUrl').val();
	var searchButton = $('#searchBtn');
	var loadingText = '<i class="fa fa-circle-o-notch fa-spin"></i> 获取中...';

	changeButtonText(searchButton, loadingText);

	if (url.includes("music.163.com/#/playlist?id=")) {
		let index = url.indexOf("=");
		var playlistId = url.substring(index + 1);

		var postContent = {
			"TransCode": "020111", // change to support more
			"OpenId": "123456789",
			"Body": {
				"SongListId": playlistId.toString()
			}
		};

		$.ajax(reqUrl, {
			data: JSON.stringify(postContent),
			contentType: 'application/json',
			type: 'POST',
			accept: 'application/json',
			beforeSend: function () {},
			complete: function () {
				resetButtonText(searchButton);
			},
			success: function (data) {
				console.log(data);

				if (data.ErrCode != "OK") {

				} else {
					let body = data.Body;
					var playlist_name = body.name;
					var tracks = body.songs;

					let res = [];

					tracks.forEach(track => {
						var title = track.title;
						var artist = track.author;

						res.push(title + '-' + artist);
					});
					res = res.join('\n');
					$('#playlistName').text(playlist_name)
					$('#playlistContent').val(res)
				}
			}
		})
	} else {
		// input error
		$('#playlistUrl').val("");
		$('#playlistUrl').css("background", "pink");
		shakeElement($('#urlContainer'));
	}
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