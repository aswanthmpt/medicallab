window.addEventListener("scroll", function() {
    var navbar = document.querySelector(".navbartwo");
    if (window.scrollY > 0) { // Change 0 to the scroll position where you want the navbar to shrink
      navbar.classList.add("shrink");
    } else {
      navbar.classList.remove("shrink");
    }
  });



  $(document).ready(function () {
    $('.scroll').slick({
        lazyLoad: 'ondemand',
        slidesToShow: 5,
        slidesToScroll: 3,
        autoplay: true,
        autoplaySpeed: 4000,
  
        infinite: true,
        arrows: false,
        responsive: [{
            breakpoint: 1280,
            settings: {
                
                arrows: false,
                slidesToShow: 4,
                slidesToScroll: 4,
            }
        },
        {
            breakpoint: 770,
            settings: {
                arrows: false,
                slidesToShow: 3,
                slidesToScroll: 3,
            }
        },
        {
            breakpoint: 520,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                centerPadding: '0px',

            }
        }
        ]
    });
});




$(document).ready(function () {
  $('.healthscroll').slick({
      lazyLoad: 'ondemand',
      slidesToShow: 3,
      slidesToScroll: 3,
      autoplay: true,
      autoplaySpeed: 4000,
       
      infinite: true,
      arrows: false,
      responsive: [{
          breakpoint: 1280,
          settings: {
              arrows: false,
              slidesToShow: 3,
              slidesToScroll: 2,
          }
      },
      {
          breakpoint: 770,
          settings: {
              arrows: false,
              slidesToShow: 2,
              slidesToScroll: 1,
          }
      },
      {
          breakpoint: 520,
          settings: {
              slidesToShow: 2,
              slidesToScroll: 1,
              centerPadding: '0px',

          }
      }
      ]
  });
});



$(document).ready(function () {
    $('.testscroll').slick({
        lazyLoad: 'ondemand',
        slidesToShow: 3,
        slidesToScroll: 3,
        autoplay: true,
        autoplaySpeed: 2500,
  
        infinite: true,
        arrows: false,
        responsive: [{
            breakpoint: 1280,
            settings: {
                arrows: false,
                slidesToShow: 3,
                slidesToScroll: 3,
            }
        },
        {
            breakpoint: 770,
            settings: {
                arrows: false,
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
        {
            breakpoint: 520,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
                centerPadding: '0px',
  
            }
        }
        ]
    });
  });

  

  