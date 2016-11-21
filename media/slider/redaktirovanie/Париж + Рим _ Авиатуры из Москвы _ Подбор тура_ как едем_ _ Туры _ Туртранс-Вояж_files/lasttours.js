jQuery('a.last_tours_next').live('click', function() {
	var link=jQuery(this);
	var prevList=link.parent('.next').prev('ul.offers_list');
	//alert (link.attr('href'));
	jQuery('ul.offers_list').animate({left: -800}, 'slow');	
	link.parents('.last-tours').append('<div class="FBloading"></div>');	
  	jQuery.getJSON(link.attr('href')+"&jsoncallback=?", function(data) {  				
  				link.parents('.last-tours').find('.prev').remove();
				prevList.after(data.tours);									   
				link.parents('.last-tours').find('.FBloading').remove();  								
				link.parent('.next').remove();  
				prevList.remove();
    });
				
    return false;
});

jQuery('a.last_tours_prev').live('click', function() {
	var link=jQuery(this);
	var prevList=link.parent('.prev').next('ul.offers_list');
	var pagenum=parseInt(link.attr('page'));
	
	if (pagenum==lasttourslastPageNum) {
		//alert(lasttourslastPageCount);  width: 640px;
		prevList.animate({left: (lasttourslastPageCount)*160 + 10*(lasttourslastPageCount)+30}, 'slow');
	}
	else prevList.animate({left: +800}, 'slow');
	//alert (link.attr('href'));
	
	link.parents('.last-tours').append('<div class="FBloading"></div>');	
  	jQuery.getJSON(link.attr('href')+"&jsoncallback=?", function(data) {
  				link.parents('.last-tours').find('.next').remove();
				prevList.before(data.tours);									   
				link.parents('.last-tours').find('.FBloading').remove();  								
				link.parent('.prev').remove();   
				if (pagenum!=lasttourslastPageNum) prevList.remove();

    });
				
    return false;
});


