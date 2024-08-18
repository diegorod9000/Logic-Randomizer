const pickRandomInstrument = () => {
    try {
        const randomLine = ALL_ALCHEMY[Math.floor(Math.random() * ALL_ALCHEMY.length)];
		return randomLine
    } catch (err) {
        console.error('Error reading the file:', err);
        return null;
    }
}

const scales = ["G Flat", "D Flat", "A Flat", "E Flat", "B Flat", "F", "C", "G", "D", "A", "E", "B"]
const onRandomizeClick = () =>{
	let instrument = pickRandomInstrument()
	let scale = scales[Math.floor(Math.random() * scales.length)]
	let module = Math.floor((Math.random() * 8) + 1)
	let randomColor;

	let instText = document.getElementById("rnd_inst");
	instText.textContent = "Instrument: " + instrument;
	randomColor = `rgb(${Math.floor(Math.random() * 256)}, 
	${Math.floor(Math.random() * 256)}, 
	${Math.floor(Math.random() * 256)})`;
	instText.style.color = randomColor;

	let scaleText = document.getElementById("rnd_scale")
	scaleText.textContent = "Scale: " + scale
	randomColor = `rgb(${Math.floor(Math.random() * 256)}, 
	${Math.floor(Math.random() * 256)}, 
	${Math.floor(Math.random() * 256)})`;
	scaleText.style.color = randomColor;

	let modText = document.getElementById("rnd_mod")
	modText.textContent = "Module : " + module
	randomColor = `rgb(${Math.floor(Math.random() * 256)}, 
	${Math.floor(Math.random() * 256)}, 
	${Math.floor(Math.random() * 256)})`;
	modText.style.color = randomColor;
}

let button = document.getElementById("rand_btn")
button.onclick = () => onRandomizeClick()


