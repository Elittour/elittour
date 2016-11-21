
		var shapkaopen=false;


		jQuery('#header_arrow.header_arrow_left').live('click',function() {
			 var tourscontainer=$('#tourscontainer');
			$(this).animate({left: '0'}, { queue:false, duration:1000 }).removeClass('header_arrow_left').addClass('header_arrow_right');
			$('.mainpage-header-big-picture').animate({
			    width: 'toggle'
			  }, 1000, function() {
			    $(this).hide();
			    $('.scroll-pane').jScrollPane({showArrows: false, verticalDragMinHeight: 20, verticalDragMaxHeight: 20});
			  });
			$('#logo').fadeTo(500, 0, function(){
				$(this).hide();
			});
			tourscontainer.animate({
			    width: '973'
			  }, { queue:false, duration:1000 }, function() {
			    // Animation complete.
			  }).removeClass('mainpage-header-content').addClass('mainpage-header-content-big');

			/*$('.scroll-wrap').animate({width: '100%'}, 990);
			$('.jspScrollable').animate({width: '100%'}, 990);
            $('.jspContainer').animate({width: '100%'}, 990);
            $('.jspPane').animate({width: '100%'}, 990);*/

            $('.scroll-wrap').width('100%');
			$('.jspScrollable').width('100%');
            $('.jspContainer').width('100%');
            $('.jspPane').width('100%');

			$('ul.scroll-pane').unbind('click');
           	$('.header-content-block-dopinfo').animate({opacity: 'show', height: ['toggle', 'swing']}, 'slow');
  			$('.mainpage-header-content-big ul.scroll-pane').find("li").each(function(){
					if ($(this).hasClass('current')) $(this).removeClass('current').addClass('oldcurrent');
					$(this).click(function() {
					window.location = $(this).attr("rel");
					return false;
					});
				});
			shapkaopen=true;
			//alert (scroll);

			return false;
		});

		jQuery('#header_arrow.header_arrow_right').live('click',function() {
			 var tourscontainer=$('#tourscontainer');
			$(this).animate({left: '701'}, { queue:false, duration:1000 }).removeClass('header_arrow_right').addClass('header_arrow_left');
			$('.mainpage-header-big-picture').animate({
			    width: 'toggle'
			  }, { queue:false, duration:1000 }, function() {
			    // Animation complete.
			  });
			$('#logo').fadeTo(1000, 1, function(){});
			tourscontainer.animate({
			    width: '256'
			    //top: '0',
			    //left: '0'
			  }, 950, function() {
			    //alert(123);
			    tourscontainer.removeClass('mainpage-header-content-big').addClass('mainpage-header-content');
			    $('.scroll-pane').jScrollPane({showArrows: false, verticalDragMinHeight: 20, verticalDragMaxHeight: 20});
			  }).removeAttr("style");
           	$('.header-content-block-dopinfo').animate({opacity: 'hide', height: ['toggle', 'swing']}, 'slow');
			$('ul.scroll-pane').find("li").each(function(){
					$(this).unbind('click');
					if ($(this).hasClass('oldcurrent')) $(this).removeClass('oldcurrent').addClass('current');
				});
            $('ul.scroll-pane').delegate('li:not(.current)', 'click', function() {
            });
            shapkaopen=false;
			return false;
		});