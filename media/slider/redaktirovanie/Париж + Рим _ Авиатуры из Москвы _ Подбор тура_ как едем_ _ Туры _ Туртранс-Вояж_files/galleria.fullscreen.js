/*!
 * Galleria Fullscreen Theme
 * http://galleria.aino.se
 *
 * Copyright (c) 2010, Aino
 * Licensed under the MIT license.
 */

(function($) {

Galleria.addTheme({
    name: 'fullscreen',
    author: 'Galleria',
    version: '2.0',
    css: 'galleria.fullscreen.css',
    defaults: {
        transition: 'none',
        image_crop: true,
        thumb_crop: 'height'
    },
    init: function(options) {

        this.addElement('thumbnails-tab');
        this.appendChild('thumbnails-container','thumbnails-tab');
        this.appendChild('thumbnails-container','thumbnails-list');
        this.appendChild('thumbnails-container','citybutton');

        var tab = this.$('thumbnails-tab');
        var tab2 = $('.galleria-thumbnails-tab2');
        var loader = this.$('loader');
        var thumbs = this.$('thumbnails-container');
        var list = this.$('thumbnails-list');
        var button = this.$('citybutton');
        var infotext = this.$('info-text');
        var info = this.$('info');
        var OPEN = true;
        var OPEN2 = false;
        var POS = 0;
        var imgclick = 0;

        if (Galleria.IE) {
            this.addElement('iefix');
            this.appendChild('container','iefix');
            this.setStyle(this.get('iefix'), {
                zIndex:3,
                position:'absolute',
                backgroundColor: '#000',
                opacity:.4
            })
        }

        if (options.thumbnails === false) {
            thumbs.hide();
        }

        thumbs.append('<div class="galleria-citybutton"><div class="galleria-cityclick close"></div></div>');
        thumbs.append('<div class="galleria-thumbnails-list2" style="display:none;"></div>');
        showcitythumbs();
        cityclick=0;
        $('#citylink'+rndgalerycty).addClass('active');
        var fixCaption = this.proxy(function(img) {
            if (!(img || img.width)) {
                return;
            }
            var w = Math.min(img.width, $(window).width());
            infotext.width(w-40);
            if (Galleria.IE && this.options.show_caption) {
                this.$('iefix').width(info.outerWidth()).height(info.outerHeight());
            }
        });

        this.bind(Galleria.RESCALE, function() {
            POS = this.stageHeight - tab.height()-2;

            var img = this.getActiveImage();
            if (img) {
                fixCaption(img);
            }
        });

        this.bind(Galleria.LOADSTART, function(e) {
            if (!e.cached) {
                loader.show().fadeTo(100, 1);
            }
            $(e.thumbTarget).css('opacity',1).parent().siblings('.active').children().css('opacity',.5);
        });

        this.bind(Galleria.LOADFINISH, function(e) {
            loader.fadeOut(300);
            this.$('info,iefix').toggle(this.hasInfo());
            if (OPEN && imgclick==0) {
                    tab.click();
                }
        });

        this.bind(Galleria.IMAGE, function(e) {
            fixCaption(e.imageTarget);
        });

        this.bind(Galleria.THUMBNAIL, function(e) {
            $(e.thumbTarget).click(function() {
            	imgclick++;
            	//alert (imgclick);
                if (imgclick>0) {
                    //tab.click();
                }
            });
        });

        this.trigger(Galleria.RESCALE);

        this.addIdleState(thumbs, { opacity:1 });
        this.addIdleState(this.get('info'), { opacity:1 });

        if (Galleria.IE) {
            this.addIdleState(this.get('iefix'), { opacity:1 });
        }

        this.$('image-nav-left, image-nav-right').css('opacity',0.01).hover(function() {
            $(this).animate({opacity:1},100);
        }, function() {
            $(this).animate({opacity:0});
        }).show();


        tab.click(this.proxy(function() {
            tab.toggleClass('open', !OPEN);
            if (!OPEN) {
              tab.animate({
                    top:0
                },4000,'galleria');
                $('.galleria-thumb-nav-left').toggle();
                $('.galleria-thumb-nav-right').toggle();
                $('.galleria-citybutton').toggle();
                $('.galleria-thumbnails-list').toggle();
                //$('.galleria-info').toggle();
                $('.galleria-info').css('bottom',40);
            } else {
             tab.animate({
                    top:0
                },4000,'galleria');
                $('.galleria-thumb-nav-left').toggle();
                $('.galleria-thumb-nav-right').toggle();
                $('.galleria-citybutton').toggle();
                $('.galleria-thumbnails-list').toggle();
                $('.galleria-thumbnails-list2').hide();
             	$('.galleria-thumbnails-list').removeClass('withlist');
				$('.galleria-info').removeClass('withlist');
				$('.galleria-cityclick.open').click();
				$('.galleria-info').css('bottom',0);

            }
            OPEN = !OPEN;
        }));
        this.$('thumbnails').children().hover(function() {
            $(this).not('.active').children().css('opacity', 1);
        }, function() {
            $(this).not('.active').children().fadeTo(200, .5);
        }).children().css('opacity',.5)

        this.enterFullscreen();
    }
});

})(jQuery);