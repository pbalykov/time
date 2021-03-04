function tim()
{
	var time = new Date();
	var sob = document.getElementById("time"),   a = [time.getHours().toString(), time.getMinutes().toString(), time.getSeconds().toString()];
	for (var i = 0; i < a.length; i++)
		if (a[i].length == 1)
			a[i] = '0' +  a[i];

	sob.innerHTML = a.join(':');
	requestAnimationFrame(tim);
}
tim();
