function defpopup(element) {
	var word = element.innerHTML;
	var search = word.replace(" ","%20").replace("'","%20");
	search = search.split("/")[0]
	var url = "https://www.merriam-webster.com/dictionary/"+search;
	var translate = 'https://translate.google.com/?hl=en&sl=en&tl=en&op=translate&text='+word;
	var image = 'https://www.google.com/search?q='+word+'&tbm=isch';
	var linguee = 'https://www.linguee.fr/francais-anglais/search?source=anglais&query='+word;
	var youtube = 'https://www.youtube.com/results?search_query='+word;
	var definition = 'https://www.dictionary.com/browse/'+word
	document.getElementById("ModalLabel").innerHTML = `<div><p class="word d-flex justify-content-center">${word} &nbsp; | &nbsp; &nbsp;
														<a href=${translate} target="_blank"><i class="fa fa-language"></i></a>&nbsp; &nbsp;
														<a href=${image} target="_blank"><i class="fa fa-image"></i></a>&nbsp; &nbsp;
														<a href=${linguee} target="_blank"><i class="fa fa-quote-right"></i></a>&nbsp; &nbsp;
														<a href=${youtube} target="_blank"><i class="fa fa-youtube"></i></a>&nbsp; &nbsp;
														<a href=${definition} target="_blank"><i class="fa fa-comment"></i></a>&nbsp; &nbsp;
													</p></div>
													<div><p id="word-definition" class="word"></p></div>`;
	fetch(url)
		.then((result) => { return result.text(); })
		.then((content) => { 
		const parser = new DOMParser();
		const doc = parser.parseFromString(content, "text/html");
		var word_definition = "";
		for (let i = 0; i < 11; i++) {
			try{
				console.log("dictionary-entry-" + String(i))
				var hword = doc.getElementsByClassName("hword")[i].outerHTML;
				var fl = doc.getElementsByClassName("fl")[i].outerHTML;
				var entry = doc.getElementById("dictionary-entry-" + String(i+1)).outerHTML;
				word_definition += hword;
				word_definition += fl;
				word_definition += entry;
				word_definition += "<br>";
			}catch{
				break;
			}
			
		}
		document.getElementById("ModalBody").innerHTML = word_definition;
	});
	
}

