 $(function(){
 	$(".progressBar").width("0%");
 	let progress = 0; 
 	$('#btnfirst').on('click', function() {
 		if (progress > 99) progress = 0;
 		$('.progressBar').css ("width", progress + 1 + "%").text (progress + 1 + "%");
 	progress++; 
 	
 	}); 
 

$(function(){ 
 	$('#btnsecond').on('click', function() {
 		if (progress > 99) progress = 0;
 		$('.progressBar').css ("width", progress + 3 + "%").text (progress + 3 + "%");
 	progress += 3;  
 	}); 
 });

$(function(){ 
 	$('#btnthird').on('click', function() {
 		if (progress > 99) progress = 0;
 		$('.progressBar').css ("width", progress + 7 + "%").text (progress + 7 + "%");
 	progress +=7; 
 	}); 
 });
});