function defpopup(element) {
	var word = element.innerHTML;
	var search_word = word.replace(" ","%20").replace("'","%20");
	var search = search_word.split("/")[0]
	//var url = "https://www.merriam-webster.com/dictionary/"+search;
	var url = "https://www.wordhippo.com/what-is/the-meaning-of-the-word/"+search+".html"
	var translate = 'https://translate.google.com/?hl=en&sl=en&tl=fr&text='+search+'&op=translate';
	var image = 'https://www.google.com/search?q='+search+'&tbm=isch';
	var linguee = 'https://www.linguee.fr/francais-anglais/search?source=anglais&query='+search;
	var youtube = 'https://www.youtube.com/results?search_query='+search;
	var definition = 'https://www.dictionary.com/browse/'+search;
	document.getElementById("ModalLabel").innerHTML = `<div><p class="word d-flex justify-content-center">
														<a href=${translate} target="_blank"><i class="fa fa-language"></i></a>&nbsp; &nbsp;
														<a href=${image} target="_blank"><i class="fa fa-image"></i></a>&nbsp; &nbsp;
														<a href=${linguee} target="_blank"><i class="fa fa-quote-right"></i></a>&nbsp; &nbsp;
														<a href=${youtube} target="_blank"><i class="fa fa-youtube"></i></a>&nbsp; &nbsp;
														<a href=${definition} target="_blank"><i class="fa fa-comment"></i></a>&nbsp; &nbsp;
													</p></div>
													<div><p id="word-definition" class="word"></p></div>`;
	fetch(url)
		.then((result) => { return result; })
		.then((content) => {
		const parser = new DOMParser();
		const doc = parser.parseFromString(content, "text/html");
		var word_definition = "<h3>"+word+"</h3>";
		for (let i = 0; i < 5; i++) {
			try{
				//var wordType = doc.getElementsByClassName("important-blue-link")[i].outerHTML;
				//var relatedWords = doc.getElementById("dictionary-entry-"+String(i+1)).outerHTML;
				var wordType = doc.getElementsByClassName("defv2wordtype")[i].outerHTML;
				var relatedWords = doc.getElementsByClassName("defv2relatedwords")[i].outerHTML;
				console.log(wordType);
				console.log(relatedWords);
				word_definition += wordType;
				word_definition += relatedWords;
				word_definition += "<br>";
			}catch{
				break;
			}
		}
		document.getElementById("ModalBody").innerHTML = word_definition;
	});
}