/* Scripts for bitstarter page */




/* Animate elements from queue */
function AnimateNext(arr) {
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

/* Twitter SDK */

!function(d,s,id) {
var js,fjs=d.getElementsByTagName(s)[0];
if(!d.getElementById(id)){
	js=d.createElement(s);js.id=id;
	js.src="https://platform.twitter.com/widgets.js";
	fjs.parentNode.insertBefore(js,fjs);
}}(document,"script","twitter-wjs");

/* Document ready section */
$(document).ready(function () {

	$('section').waypoint(function () {
		$(this).animate({opacity: 1}, 1500);	
	}, {offset: '95%'});

	HideElements(MissionAnimateQueue);

	$('#mission > label').waypoint( function () {
		AnimateNext(MissionAnimateQueue)();
	}, {offset: '50%'});
});
