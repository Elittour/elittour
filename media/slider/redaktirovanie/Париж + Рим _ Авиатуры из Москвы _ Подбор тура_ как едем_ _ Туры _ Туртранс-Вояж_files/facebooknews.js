jQuery('a.facebook_news_next').live('click', function() {
	var link=jQuery(this);
	//alert (link.attr('href'));
	link.parents('.right_item').addClass('FBloading');
  	jQuery.getJSON(link.attr('href')+"&jsoncallback=?", function(data) {
				link.parents('.right_module').append(data.news);				
				link.parents('.right_item').remove();        
    });
				
    return false;
});


