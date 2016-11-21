$(document).ready(function () {
    $('a[href*=#]').bind("click", function (e) {
        var anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $(anchor.attr('href')).offset().top-49
        }, 1000);
        e.preventDefault();
    });
    $(window).scroll(function () {
        if ($(this).scrollTop() > 0) {
            $('#scroller').fadeIn();
        } else {
            $('#scroller').fadeOut();
        }
    });
    $('#scroller').click(function () {
        $('body,html').animate({scrollTop: 0}, 400);
        return false;
    });
});

$(document).ready(function(){
      $('.head-slider').slick({
        dots: true
      });
    });

    $('.head-slider').slick({
      dots: true,
      infinite: true,
      speed: 500,
      arrows: false,
      fade: true,
      cssEase: 'linear',
      autoplay: true,
      autoplaySpeed: 5000,
    });