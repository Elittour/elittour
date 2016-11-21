var declOfNum=function(number, titles){
	var cases = [2, 0, 1, 1, 1, 2];
	number=Math.abs(number);
	return number+" "+titles[ (number%100>4 && number%100<20)? 2 : cases[Math.min(number%10, 5)] ];
}

var getUrlVars=function (urlString) {
    var vars = {}
    var hash;
    if (!urlString) window.location.href;
    var hashes = urlString.slice(urlString.indexOf('?') + 1).split('&');
    for (var i = 0; i < hashes.length; i++) {
        hash = hashes[i].split('=');
        //vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}

jQuery('.docs_send_form ._button.big.gray').live('click',function() {

			$(this).parents('.docs_send_form').find(".DocsSendForm_files").each(function() {
							if ($(this).attr('checked', true));
						});	
			$("#viza-docs-form").submit();
			
			return false;
		});	

jQuery('.docs_send_form ._button.big.green').live('click',function() {
			$("#viza-docs-form").submit();
			
			return false;
		});	
		
		
jQuery('.DocsSendForm_files').live('click',function() {
			
			var count=0;
			$(".DocsSendForm_files").each(function() {
							if ($(this).attr('checked')) count++;
						});			
						
			if (count)
				$(this).parents('.docs_send_form').find('._button.big').removeClass('gray').addClass('green');
			else
				$(this).parents('.docs_send_form').find('._button.big').removeClass('green').addClass('gray');

		});	
		
jQuery('.why_pricemenu ul li a').live('click',function() {
			$(this).parent('li').addClass('active').siblings().removeClass('active');
			$('#tour_why_price_type_'+$(this).attr('rel')).show().siblings('.why_pricemenu_content').hide();
			$.fancybox.update();
			return false;
		});	
		
jQuery('.dates-list-4 a.date_info__date').live('click',function() {	
			if ($(this).hasClass('date_seats_no')) return false;
			
			var dateId=$(this).attr('date_id');
			var linktop=$(this).offset().top;
			var h=$(this).parents('.date4-month-price-tr').height();
			var trtop=$(this).parents('.date4-month-price-tr').offset().top;
			console.log(linktop, trtop, h);

			$('.dates-list-4 .date_info').removeClass('date4-active');
			$(this).parents('.date_info').addClass('date4-active');
			
			var container=$(this).parents('tr').nextAll('tr.date4-content-tr').first().children('td').children('.date4-content');
			container.parent('td').addClass('td-opened');
			
			if (h > 45 && linktop-trtop < h-6) {
				var margin=(linktop-trtop)-h+39;
				container.css({'margin-top':margin});	
			}
			else container.css({'margin-top':0});
			
			container.show().parents('.date4-content-tr').siblings('.date4-content-tr').children('td').children('.date4-content').hide().empty().parent('td').removeClass('td-opened');
			var NMen = 0;
			var accTypesArr={};
			console.log(container);
			jQuery.ajax({
				type:"GET",
				url:$(this).attr('href'),
				beforeSend: function() {
					container.addClass('FBloading');
					 },
				success:function(html){
					container.removeClass('FBloading');
					container.html(html);
					getData({r: 'tours/dateInfo', id:dateId}).success(function(data){
						console.log(data);						
						var ul = container.find('.date4-room-types-list').first();
						for (var i in data.accTypes){
							var accType=data.accTypes[i];
							accTypesArr[accType.price.PriceKey]=accType;
							var li=$('<li class="date4-room-types-list-item"/>').addClass(accType.model.CSSclass);
							li.append('<label><input type="radio" value="'+accType.price.PriceKey+'" price-key="'+accType.price.PriceKey+'" class="acc-type-select" name="date4-room-types-input"><span><i class="date4-room-types-name">'+accType.model.type_name+'</i>&nbsp;<div class="tooltip2"><img src="/images/wtf.png"><div class="tooltip2_body-top"><div class="tooltip2_text">'+accType.model.descr+'</div></div></div></span></label>');
							li.find('input').click(function(){
								console.log(accTypesArr);
								var accType=accTypesArr[$(this).attr('price-key')];
								var priceBox=$('.date4-price');
								saveSeats($(this).attr('price-key'), []);
								$('.bus-scheme__bus .place_Seat').removeClass('disabled').removeClass('active');
								NMen = 0;
								priceBox.hide();
								$('.date4-order_button.order_button .agency-bron-link').attr('href', accType.links.agency);
								$('.date4-order_button.order_button .tourist-bron-link').attr('href', accType.links.tourist);										
								getData({r: 'tours/getAcctypeServices', PriceKey:$(this).attr('price-key')}).success(function(data){
									console.log("/ajax/convertPrice?val="+accType.price.master_price+"&currency="+accType.price.currency+"&jsoncallback=?");								
									NMen=data.result[0].NMen;
									jQuery.getJSON("/ajax/convertPrice?val="+accType.price.master_price+"&currency="+accType.price.currency+"&jsoncallback=?", function(data){										
										priceBox.children('.date4-price-single').html(data.val+'&nbsp;'+data.currency);
										priceBox.children('.date4-price-nmen').html(NMen);
										priceBox.children('.date4-price-full').html((data.val*NMen)+'&nbsp;'+data.currency);										
										priceBox.show();
									});
								});
							});
							ul.append(li);
							
						}
						container.find('.date4-room-types-list').first().find('input').first().click();
					});

				},
				"cache":false
			});
			
			return false;
		});	
		
jQuery('.dates-list-4 a.date4-content-close').live('click',function() {		
	$(this).parents('.date4-content').empty().hide().css({'margin-top':0}).parent('td').removeClass('td-opened').parent().prev('.date4-month-price-tr').find('.date4-active').removeClass('date4-active');
	return false;
});	

jQuery('.bus-scheme__info-header a').live('click',function() {		
	$(this).parent().next().animate({opacity: 'toggle', height: ['toggle', 'swing']}, 'slow');
	return false;
});	


function saveSeats(priceKey, arr) {
   	var val=JSON.stringify(arr);
   	jQuery.getJSON("/ajax/SaveBusSeatsSelect?priceKey="+priceKey+"&val="+val+"&jsoncallback=?", function(data){	});
}

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}

function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

var seatsValidate={
	seats : [],
	countSelected : 0,
	setSeats : function(){
		var arr=[];
		$('.bus-scheme__bus .place_Seat').each(function(){
			var name=$(this).html();			
			reg = /(\d+)(\D+)/i;
			found = name.match(reg);
			var letter=found ? found[2] : null;
			arr.push({
				name:$(this).html(),				
				ryad:found ? parseInt(found[1]) : null,
				letter:letter,
				placeYes : $(this).hasClass('place_yes'),
				active : $(this).hasClass('active'),
				disabled : $(this).hasClass('disabled'),
				type:letter=='A' || letter=='D' ? 'window' : 'path',
				obj:$(this),
				PizduiSuda:false,
			});
		});
		var ryadArr=[];
		for (var i in arr){
			if (!ryadArr[arr[i].ryad]) ryadArr[arr[i].ryad]=[];
			ryadArr[arr[i].ryad].push(arr[i]);
		}
		//console.log(ryadArr, arr);
		this.seats=ryadArr;
	},	
	checkSingle : function(seat){
		var that=this;
		var seats=that.seats;
		console.log(seats);
		var countSingleWindow=0;
		for (var ryad in seats){
			var b=0;
			for (var i in seats[ryad]){
				if (seats[ryad][b].type=='window' && (!seats[ryad][b].placeYes || seats[ryad][b].active)){
					var nextPath=seats[ryad][b+1]!=undefined ? seats[ryad][b+1] : seats[ryad][b-1];					
					if (nextPath){
						if (seat==nextPath.name) return true;
						if (nextPath.placeYes && !nextPath.active){
							nextPath.PizduiSuda=true;
							countSingleWindow++;
						}
					}
					
				}
				b++;
			}
		}
		console.log(countSingleWindow);
		return countSingleWindow < 2;
	},
	checkDouble : function(seat, NMen){
		var that=this;
		var seats=that.seats;
		console.log(seats);
		var selected=[];
		var countWindow=0;
		var countPath=0;
		var currentSeat;
		for (var ryad in seats){
			for (var i in seats[ryad]){
				if (seats[ryad][i].active){
					selected.push(seats[ryad][i]);
					if (seats[ryad][i].type=='window') countWindow++;
					else countPath++;
				}
				if (seats[ryad][i].name==seat) currentSeat=seats[ryad][i];
			}
		}
		that.countSelected=selected.length;
		
		var setPizdui=function(type){
			for (var ryad in seats){
				for (var i in seats[ryad]){
					if (seats[ryad][i].type==type && seats[ryad][i].placeYes && !seats[ryad][i].active){						
						seats[ryad][i].PizduiSuda=true;
					}
				}
			}
		}
		console.log(countWindow, countPath, NMen/2)
		if (countWindow >= NMen/2 && currentSeat.type=='window'){
			setPizdui('path');
			return false;
		}
		if (countPath >= NMen/2 && currentSeat.type=='path'){
			setPizdui('window');
			return false;
		}			
		return true;
	},
	showError : function(){
		var that=this;
		var seats=that.seats;
		alert('Выбор этого места не возможен. Просим выбрать другое место согласно правилам рассадки.');
		for (var ryad in seats){
			for (var i in seats[ryad]){
				if (!seats[ryad][i].PizduiSuda){
					seats[ryad][i].obj.addClass('disabled');
					seats[ryad][i].disabled=true;
				}
			}
		}
	},
	validate : function(seat, NMen){
		var that=this;
		that.setSeats();
		var seats=that.seats;
		
		var selected=[];
		for (var ryad in seats){
			for (var i in seats[ryad]){
				if (seats[ryad][i].active){
					selected.push(seats[ryad][i]);			
					if (seat==seats[ryad][i].name) return true;
				}
			}
		}
		that.countSelected=selected.length;
		
		if (NMen==1 && !that.checkSingle(seat)){
			that.showError();
			return false;
		}
		if (NMen>1 && NMen%2==0 && !that.checkDouble(seat, NMen) && that.countSelected < NMen){
			that.showError();
			return false;
		}
		if (NMen>1 && NMen%2!=0 && that.countSelected < NMen){
			var a=NMen%2;
			var res1=that.countSelected < NMen-a ? that.checkDouble(seat, NMen-a) : true;
			var res2=true;
			if (res1 && that.countSelected==NMen-a){
				res2=that.checkSingle(seat);
			}			
			if (!res1 || !res2){
				that.showError();
				return false;
			}
		}
		return true;
	}
};

jQuery('.bus-scheme__bus .bus__row .place_Seat.place_yes').live('click',function() {		

	
	//
	var priceKey=$('input[name="date4-room-types-input"]:radio:checked').val();
	var NMen=parseInt($('.date4-price-nmen').first().html());
	if (!seatsValidate.validate($(this).html(), NMen)) return false;
	
	if ($('.bus-scheme__bus .place_Seat.place_yes.active').length < NMen || $(this).hasClass('active')){
		$(this).toggleClass('active');
		var arr=[];
		var i=0;
		$('.bus-scheme__bus .place_Seat.place_yes.active').each(function(){
			arr[i]=$(this).html();
			i++;
		});
		saveSeats(priceKey, arr);
	}
	
	if ($('.bus-scheme__bus .place_Seat.place_yes.active').length >=NMen){
		$('.bus-scheme__bus .place_Seat').addClass('disabled');
	}
	else 
		$('.bus-scheme__bus .place_Seat').removeClass('disabled');
	
	var selected=$('.bus-scheme__bus .place_Seat.place_yes.active').length;
	
	$('.seats-select-info').empty();
	
	if (selected){
		$('.seats-select-info').html(declOfNum(selected, ['место', 'места', 'мест'])+' выбрано, еще '+(NMen-selected)+' доступно');
	}
	
	return false;
});	

var getData=function(params){
	var parts = location.hostname.split('.');
	params.subdomain = parts.shift();
	var url="http://admin.tourtrans.ru?"+jQuery.param( params )+"&jsoncallback=?";
	return jQuery.getJSON(url);
};