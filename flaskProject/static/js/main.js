// create AudioPlayer constructor
function AudioPlayer(el) {
	this.artistElem = el.getElementsByClassName('artist')[0];
	this.titleElem = el.getElementsByClassName('title')[0];
	this.progressBar = el.getElementsByClassName('progress-bar')[0];
	this.progress = el.getElementsByClassName('progress')[0];
	this.currentDuration = el.getElementsByClassName('current-duration')[0];
	this.duration = el.getElementsByClassName('duration')[0];
	this.volume = el.getElementsByClassName('volume')[0];
	this.prevBtn = el.getElementsByClassName('prev')[0];
	this.playBtn = el.getElementsByClassName('play')[0];
	this.pauseBtn = el.getElementsByClassName('pause')[0];
	this.nextBtn = el.getElementsByClassName('next')[0];
	this.listBtn = el.getElementsByClassName('list-btn')[0];
	this.listElem = el.getElementsByClassName('playlist')[0];
	this.activeItem = el.getElementsByClassName('active')[0] || this.listElem.firstElementChild;
	this.currentTime = 0;
	this.durationTime = 0;
	this.audio;
	this.song;
	this.setList();
	this.initAudio(this.activeItem);
	var thisPlayer = this;
	this.prevBtn.addEventListener('click', function(e) {
		thisPlayer.setPrevAudio();
	});
	this.playBtn.addEventListener('click', function(e) {
		thisPlayer.playAudio();
	});
	this.pauseBtn.addEventListener('click', function(e) {
		thisPlayer.pauseAudio();
	});
	this.nextBtn.addEventListener('click', function(e) {
		thisPlayer.setNextAudio();
	});
	this.listElem.addEventListener('click', function(e) {
		thisPlayer.setClickAudio(e.target);
	});
	this.progressBar.addEventListener('click', function(e) {
		thisPlayer.setProgress(e);
	});
	//Volume control
	this.volume.addEventListener('mousedown', function(e) {
		this.addEventListener('mousemove', function(e) {
			thisPlayer.audio.volume = parseFloat(this.value / 100);
		});
	});
	//Playlist visible/invisible
	this.listBtn.addEventListener('click', function(e) {
		if (getComputedStyle(thisPlayer.listElem).display == "none" || thisPlayer.listElem.style.display == "none") thisPlayer.listElem.style.display = "inline-block";
		else thisPlayer.listElem.style.display = "none";
	});
};

// add initAudio method for AudioPlayer prototype
AudioPlayer.prototype.initAudio = function(element){
	element.classList.add("active");
	this.song = element.getAttribute("data-song");
	var songName = element.innerHTML;
	this.artistElem.innerHTML = songName.split('-')[0];
	this.titleElem.innerHTML = songName.split('-')[1];
	//Create audio object
	this.audio = new Audio('../static/media/'+ this.song);
	this.audio.volume = parseFloat(this.volume.value / 100);
};

// add playAudio method for AudioPlayer prototype
AudioPlayer.prototype.playAudio = function(){
	this.playBtn.style.display = "none";
	this.pauseBtn.style.display = "inline-block";
	this.initAudio(this.activeItem);
	this.audio.play();
	this.audio.currentTime = this.currentTime;
	this.showDuration();
};

// add pauseAudio method for AudioPlayer prototype
AudioPlayer.prototype.pauseAudio = function(){
	this.pauseBtn.style.display = "none";
	this.playBtn.style.display = "inline-block";
	this.currentTime = this.audio.currentTime;
	this.audio.pause();
};

// add setPrevAudio method for AudioPlayer prototype
AudioPlayer.prototype.setPrevAudio = function(){
	this.activeItem.classList.remove("active");
	if (this.audio != undefined) this.audio.pause();
	var prev = this.activeItem.previousElementSibling;
	if (prev == null) prev = this.listElem.lastElementChild;
	this.activeItem = prev;
	this.playAudio();
	this.audio.currentTime = 0;
};

// add setNextAudio method for AudioPlayer prototype
AudioPlayer.prototype.setNextAudio = function(){
	this.activeItem.classList.remove("active");
	if (this.audio != undefined) this.audio.pause();
	var next = this.activeItem.nextElementSibling;
	if (next == null) next = this.listElem.firstElementChild;
	this.activeItem = next;
	this.playAudio();
	this.audio.currentTime = 0;
};

// add setClickAudio method for AudioPlayer prototype
AudioPlayer.prototype.setClickAudio = function(target){
	if (target == this.activeItem) return;
	this.activeItem.classList.remove("active");
	if (this.audio != undefined) this.audio.pause();
	this.activeItem = target;
	this.playAudio();
	this.audio.currentTime = 0;
};

// add initAudio method for AudioPlayer prototype
AudioPlayer.prototype.showDuration = function(){
	var thisPlayer = this;
	this.audio.addEventListener('timeupdate', function(){
		thisPlayer.durationTime = thisPlayer.audio.duration;
		thisPlayer.duration.innerHTML = readTime(thisPlayer.audio.duration);
		thisPlayer.currentDuration.innerHTML = readTime(thisPlayer.audio.currentTime);
		var value = 0;
		if (thisPlayer.audio.currentTime > 0) value = (100 / thisPlayer.audio.duration) * thisPlayer.audio.currentTime;
		thisPlayer.progress.style.width = value +"%";
		if (thisPlayer.audio.currentTime == thisPlayer.audio.duration) thisPlayer.setNextAudio();
	});
	//Get hours and minutes
	function readTime(time) {
		var s = parseInt(time % 60);
		var m = parseInt(time / 60) % 60;
		if (s < 10) s = '0'+s;
		var str = m + ':'+ s;
		return str;
	};
};

// add setProgress method for AudioPlayer prototype
AudioPlayer.prototype.setProgress = function(e){
	var fieldCoords = this.progressBar.getBoundingClientRect();
	var left = e.clientX - fieldCoords.left;
	var per = (left/parseFloat(getComputedStyle(this.progressBar).width)).toFixed(3);
	this.progress.style.width = per*100 + '%';
	this.currentTime = this.durationTime*per;
	this.audio.currentTime = this.durationTime*per;
};

// add setList method for AudioPlayer prototype
AudioPlayer.prototype.setList = function(){
	var elements = this.listElem.children;
	for (var i=0; i<elements.length; i++) {
		var songName = elements[i].getAttribute("data-song").split('.')[0];
		elements[i].innerHTML = splitString(songName);
	}
	function splitString(str) {
		var substr = str.split('_');
		var resultStr = "";
		for (var j=0; j<substr.length; j++) {
			resultStr += substr[j] + " ";
		}
		return resultStr;
	}
;};







// ==================================================================================

// Document ready
document.addEventListener("DOMContentLoaded", function() {
	var playerEl = document.documentElement.getElementsByClassName('audio-player')[0];
	var player1 = new AudioPlayer(playerEl);
});