
function adjustHeight(){
	if(h<780 && $("body").hasClass("hwindow")){
		$("body").removeClass("hwindow");
	}else if(h>=780 && !$("body").hasClass("hwindow")){
		$("body").addClass("hwindow");
	}else{}
}
function getTotalHeight(){ 
	if($.browser.msie){ 
		return document.compatMode == "CSS1Compat"? document.documentElement.clientHeight : document.body.clientHeight; 
	} 
	else { 
		return self.innerHeight; 
	} 
} 
function getTotalWidth (){ 
	if($.browser.msie){ 
		return document.compatMode == "CSS1Compat"? document.documentElement.clientWidth : document.body.clientWidth; 
	} 
	else{ 
		return self.innerWidth; 
	} 
} 
function hideUnnecessaryDiv(){
	if($("div.loadmodules_div")){
		var e = $("div.loadmodules_div").each(function(i, val){
			if($(val).children().length == 0){
				$(val).remove();
			}
		})
	}
}
function hideUnnecessaryMenu(){
	if($("ul#top_sub_menu")){
		var e = $("ul#top_sub_menu").children().each(function(i, val){
			if(!$(val).hasClass("active")){
				$(val).remove();
			}
		})
	}
}
function formalizeTopMenu(){
	if($("ul#index-top-menu")){
		var ul = $("ul#jsddm");
		$("ul#index-top-menu").children("li").each(function(i, val){
			var li=$('<li></li>');
			var cls = '';
			$(val).children("a").each(function(m, aval){
				cls = $(aval).attr('class');
				$(aval).attr('id',cls);
				$(aval).attr('class','top-link');
				li.append($(aval));
			});
			ul.append(li);
			if($("div#d_"+cls+"-div")){
				$(val).children("ul").children("li").each(function(j, subval){
					$("div#d_"+cls+"-div").append($(subval).children("a"));
				});
			}
		})
		$("ul#index-top-menu").remove();
	}
}
function formalizeExpressMenu(){
	if($("ul#express-menu")){
		var div = $("div#quick-links");
		$("ul#express-menu").children("li").each(function(i, val){
			var dl=$('<dl class="dl-horizontal"></dl>');
			var dt=$('<dt></dt>');
			var dd=$('<dd></dd>');
			dt.append($(val).children("a"));
			$(val).children("ul").children("li").each(function(j, subval){
				dd.append($(subval).children("a"));
			});
			dl.append(dt,dd);
			div.append(dl);
		})
		$("ul#express-menu").remove();
	}
}
function fixEventListPage(){
	if($("div#jevents_header")){
		$("div#jevents_header").remove();
	}
	
	if($("p.event-time") ){
		$("p.event-time").each(function(i, val){
			if( $(val).text() == ' - ')
				$(val).remove();
		});
	}
	// if($("div#jevents_body")){
	// 	$("div#jevents_body").attr("id","jevents_body_fix")
	// }
}
function formalizeFontSize(){
	if($("div.article-content")){
		$("div.article-content").find("[style]").each(function(i, val){
			if($(val).attr("style").indexOf("font-size")!=-1){
				// $(val).css("font-size","1em");
			}
		})
	}
}
function adjustSearchForm(){
	if($("form#searchForm")){
		var o;
		if($("div.btn-toolbar")){
			o = $("input[name='searchword']").addClass("input-xlarge").parent();
			o.addClass("input-append");
			o.append($("button[name='Search']").addClass("btn").append("&nbsp;"));
		}
		if($("fieldset.phrases")){
			$("fieldset.phrases").find("label").addClass("inline");
			$("div.phrases-box").addClass("pull-left")
			$("div.ordering-box").addClass("form-inline").addClass("pull-right");
		}
		if($("fieldset.only")){
			$("fieldset.only").find("label").addClass("inline");
		}
		if($("div.form-limit")){
			o = $('<legend></legend>');
			$("div.form-limit").addClass("form-inline").css("margin-top","20px").before(o);
			o.append($("div.form-limit"));
		}
		if($("dl.search-results")){
			$("dl.search-results").find("dd.result-category").remove();
		}

	}
}
function listenSearchEnter(){
	$('input#search-input').keydown(function(e){
		if(e.keyCode==13){
		    doSearch();
		}
	});

}
function doSearch(){
	var s = mytrim($("input#search-input").val());
	if(s!=''){
		window.location.href = $("input#search-url").val() + "?searchword="+s+"&ordering=newest&searchphrase=all";
	}else{
		window.location.href = $("input#search-url").val();
	}

}
function fixPageBreaker(){
	if($("div.article-index")){

		var obj = $('<div style="text-align:center;"><ul class="article-index-pager inline" style="margin:20px 0;font-size:10px;"></ul></div>');
		$("div.article-content").append(obj);
		$("div.article-index").find("li").each(function(i, val){
			if($(val).hasClass("toclink")){
				$(val).children("a").html("1");
			}
			$("ul.article-index-pager").append($(val));
		})
		$("div.article-content").find("div.pager").each(function(i, val){
			$(val).remove();
		})
		$("div.article-content").find("div.pagenavcounter").each(function(i, val){
			$(val).remove();
		})
	}
}

function mytrim(str){
    for(var  i  =  0  ;  i<str.length  &&  str.charAt(i)==" "  ;  i++  )  ;
    for(var  j  =str.length;  j>0  &&  str.charAt(j-1)==" "  ;  j--)  ;
    if(i>j)  return  "";  
    return  str.substring(i,j);  
}



var h = 0;



$(document).ready(function() {
	
	h = getTotalHeight();
	adjustHeight();
	hideUnnecessaryDiv();
	formalizeExpressMenu();
	formalizeTopMenu();
	formalizeFontSize();
	fixEventListPage();
	adjustSearchForm();
	listenSearchEnter();
	fixPageBreaker();
});

$(window).resize(function(){
    h = getTotalHeight();
    adjustHeight();
});

if (window.ActiveXObject) {
	var ua = navigator.userAgent.toLowerCase();
	var ie=ua.match(/msie ([\d.]+)/)[1]

	if(ie==6.0){
		alert("您的浏览器版本过低，在本系统中不能达到良好的视觉效果，建议升级到IE7以上，推荐使用Chrome、Firefox浏览器，或最新版本IE浏览器。或者您可以访问旧版网站。");
		window.close();
	}
}