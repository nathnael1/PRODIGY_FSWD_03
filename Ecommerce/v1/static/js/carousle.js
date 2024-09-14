
document.addEventListener( 'DOMContentLoaded', function() {
    var splide = new Splide('.splide', {
        type       : 'loop',
        perPage    : 1,
        autoplay   : true,
        interval   : 3000,
        speed      : 800,
        pauseOnHover: true,
        arrows     : true,
        pagination : true,
        easing     : 'ease-in-out',
      });
splide.mount();
});
