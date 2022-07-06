function defpopup(element) {
	var word = element.innerHTML;
	document.getElementById("ModalLabel").innerHTML = word;
	
	translate = 'https://translate.google.com/?hl=en&sl=en&tl=en&op=translate&text='+word;
	image = 'https://www.google.com/search?q='+word+'&tbm=isch';
	linguee = 'https://www.linguee.fr/francais-anglais/search?source=anglais&query='+word;
	youtube = 'https://www.youtube.com/results?search_query='+word;
	definition = 'https://www.dictionary.com/browse/'+word
	document.getElementById("ModalBody").innerHTML = `<p class="word d-flex justify-content-center">
														<a href=${translate} target="_blank"><i class="fa fa-language"></i></a>&nbsp; &nbsp;
														<a href=${image} target="_blank"><i class="fa fa-image"></i></a>&nbsp; &nbsp;
														<a href=${linguee} target="_blank"><i class="fa fa-quote-right"></i></a>&nbsp; &nbsp;
														<a href=${youtube} target="_blank"><i class="fa fa-youtube"></i></a>&nbsp; &nbsp;
														<a href=${definition} target="_blank"><i class="fa fa-comment"></i></a>&nbsp; &nbsp;
													</p>`;
	
	var search = word.replace(" ","%20").replace("/","%20");
	}
