$(document).ready(function() {
				$("#box1").addClass("hide");
				$("#box2").addClass("hide");
				$("#box3").addClass("hide");


				$("#univesal-search-form1").addClass("hide");

				$("#usfmsc21").addClass("hide");

				$("#discounts-tab-content1").addClass("hide");
				$("#discounts-tab-content2").addClass("hide");
				$("#discounts-tab-content3").addClass("hide");
				$("#discounts-tab-content4").addClass("hide");
				$("#discounts-tab-content5").addClass("hide");

				for (i=1;i<18;i++){
				$("#content1_"+i).addClass("hide");
				}	;
				for (i=1;i<18;i++){
				$("#content2_"+i).addClass("hide");
				}	;



				$("#picture1").addClass("hide");
				$("#picture2").addClass("hide");
				$("#picture3").addClass("hide");
				$("#picture4").addClass("hide");
				$("#picture5").addClass("hide");



				});
(function($) {



$(function() {


				$('ul.tabs').delegate('li:not(.current)', 'click', function() {



		$(this).addClass('current').siblings().removeClass('current');

			tourstype=$(this).children("a").attr("tourstype");
			var country=$(this).children("a").attr("country");
			jQuery.ajax({'type':'POST','beforeSend':function(){

			$("#scroll-wrap").empty();
			$("#scroll-wrap").addClass("loading");
			//alert (tourstype);

         },'complete':function(){
            $("#scroll-wrap").removeClass("loading");
            $("#scroll-wrap").fadeTo(0, 0);
            $("#scroll-wrap").fadeTo(800, 1);

        },'url':'/index.php?r=ajax/loadshapkatours','cache':false,'data':'type='+tourstype+'&country='+country,'success':function(html){

        	jQuery("#scroll-wrap").html(html);

        	$('.scroll-pane').jScrollPane({showArrows: false, verticalDragMinHeight: 20, verticalDragMaxHeight: 20});
        	if (shapkaopen) $('.header-content-block-dopinfo').animate({opacity: 'show', height: ['toggle', 'swing']}, 'slow');
	        $('#tourscontainer ul.scroll-pane').delegate('li:not(.current)', 'click', function() {
			$(this).addClass('current').siblings().removeClass('current');
			tourid=$(this).attr("tourid");
			imgid=$(this).attr("imgid");
			jQuery.ajax({'type':'POST','beforeSend':function(){

			$("#picture0").empty();
			$("#picture0").addClass("headpict_loading");

         },'complete':function(){
            $("#picture0").removeClass("headpict_loading");
           $("#picture0").fadeTo(0, 0);
           $("#picture0").fadeTo(800, 1);
        },'url':'/index.php?r=ajax/loadhottour','cache':false,'data':'tourid='+tourid+'&imgid='+imgid+'','success':function(html){jQuery("#picture0").html(html)}});return false;});


        	$('.mainpage-header-content-big ul.scroll-pane').unbind('click');

        	$('.mainpage-header-content-big ul.scroll-pane').find("li").each(function(){
					if ($(this).hasClass('current')) $(this).removeClass('current').addClass('oldcurrent');
					$(this).click(function() {
					window.location = $(this).attr("rel");
					return false;
					});
				});

        	i=0;
        	$('.mainpage-header-content ul.scroll-pane').find("li").each(function(){

					if (i==0) $(this).click();

					i++;
				});
        	//alert (i);
        	}});

        	return false;

   	});




	$('ul.universal-search-form-menu').delegate('li:not(.first-level-current)', 'click', function() {

			$(this).addClass('first-level-current').siblings().removeClass('first-level-current');

				$("#univesal-search-form0").addClass("hide");
				$("#univesal-search-form1").addClass("hide");
				fuck="#univesal-search-form"+$(this).index();
				$(fuck).removeClass("hide");

	})
	$('ul.universal-search-form-menu-sublevel').delegate('li:not(.first-level-current) > input', 'click', function() {

                //alert (123);
               	ind=$(this).parent().index()-1;
				fuck="#usfmsc"+ind;
				for (i=0;i<6;i++){
				$("#usfmsc"+i).addClass("hide");
				}
				$(fuck).removeClass("hide");

	})
	$('ul.universal-search-form-menu-sublevel2').delegate('li:not(.first-level-current)', 'click', function() {


				fuck="#usfmsc2"+$(this).index();
				$("#usfmsc20").addClass("hide");
				$("#usfmsc21").addClass("hide");
				$(fuck).removeClass("hide");

	})

/* Discounts - Bonuses - Gifts */
	$('ul.discounts-tab-menu_tabs').delegate('li:not(.current)', 'click', function() {

			$(this).addClass('current').siblings().removeClass('current');

				$("#discounts-tab-content0").addClass("hide");
				$("#discounts-tab-content1").addClass("hide");
				$("#discounts-tab-content2").addClass("hide");
				$("#discounts-tab-content3").addClass("hide");
				$("#discounts-tab-content4").addClass("hide");
				$("#discounts-tab-content5").addClass("hide");
				fuck="#discounts-tab-content"+$(this).index();
				$(fuck).removeClass("hide");

	})

/* Destinations */
	$('ul.dest_menu1').delegate('li:not(.current)', 'click', function() {

			$(this).addClass('current').siblings().removeClass('current');
				for (i=0;i<18;i++){
				$("#content1_"+i).addClass("hide");
				}
				fuck="#content1_"+$(this).index();
				$(fuck).removeClass("hide");

	})
	$('ul.dest_menu2').delegate('li:not(.current)', 'click', function() {

			$(this).addClass('current').siblings().removeClass('current');
				for (i=0;i<18;i++){
				$("#content2_"+i).addClass("hide");
				}
				fuck="#content2_"+$(this).index();
				$(fuck).removeClass("hide");

	})

/* Main page BIG PICTURE BLOCK */
		$('.mainpage-header-content ul.scroll-pane').delegate('li:not(.current)', 'click', function() {
			$(this).addClass('current').siblings().removeClass('current');
			tourid=$(this).attr("tourid");
			imgid=$(this).attr("imgid");
			jQuery.ajax({'type':'POST','beforeSend':function(){

			$("#picture0").empty();
			$("#picture0").addClass("headpict_loading");
			//alert (idd);

         },'complete':function(){
            $("#picture0").removeClass("headpict_loading");
           // $("#picture0").fadeOut('fast');
           $("#picture0").fadeTo(0, 0);
           $("#picture0").fadeTo(800, 1);
        },'url':'/index.php?r=ajax/loadhottour','cache':false,'data':'tourid='+tourid+'&imgid='+imgid+'','success':function(html){jQuery("#picture0").html(html)}});return false;});

   })


})(jQuery)
