function tim()
{
	var time = new Date();
	var sob = document.getElementById("time");
	var a = [time.getHours().toString(), time.getMinutes().toString(), 
		 time.getSeconds().toString()];
	var col = document.getElementById("colr");
	for (var i = 0; i < a.length; i++)
		if (a[i].length == 1)
			a[i] = '0' +  a[i];

	sob.innerHTML = a.join(':');
	col.innerHTML = '#' + a.join('');
	document.body.style.backgroundColor = "#" + a.join('');
}

setInterval(tim, 4);
