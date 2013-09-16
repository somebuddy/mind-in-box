/* Scripts for bitstarter page */




/* Animate elements from queue */
function AnimateNext(arr) {
    console.log($(arr[0]));
	return function () {
		$(arr[0]).animate({opacity: 1}, 300, AnimateNext(arr.slice(1)));
	}
};

/* Mission Section Scroll Fade animation */
var MissionAnimateQueue = [
    '#mission > label',
    '#mission > .slogan',
    '#carousel-mission .indicator.position-1',
    '#carousel-mission .indicator.position-2',
    '#carousel-mission .indicator.position-3',
    '#carousel-mission .indicator.position-4',
    '#carousel-mission .indicator.position-5',
    '#carousel-mission .item-box',
    '#carousel-mission .background',
    '#carousel-mission .item .caption',
    '#carousel-mission .item .comment',
    ];

function HideElements (arr) {
	for (i = 0; i < arr.length; ++i) {
		$(arr[i]).css({opacity: 0});
	}
}

/* Document ready section */
$(document).ready(function () {

	$('section').waypoint(function () {
		console.log(this);
		$(this).animate({opacity: 1}, 1500);	
	}, {offset: '95%'});

	HideElements(MissionAnimateQueue);

	$('#mission > label').waypoint( function () {
		AnimateNext(MissionAnimateQueue)();
	}, {offset: '50%'});
});
