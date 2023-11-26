(function() {
	// Annoying hack to prevent map overlap due to the top bar on Android
	function fixHeight() {
		document.documentElement.style.setProperty("--dvh", `${window.innerHeight}px`);
	}
	window.addEventListener("resize", fixHeight);
	fixHeight();
})();